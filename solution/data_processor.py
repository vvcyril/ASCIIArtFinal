import pandas as pd
from pathlib import Path
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    """Abstract base class for data processing pipelines."""

    @abstractmethod
    def process_data(self, data_path: Path) -> pd.DataFrame:
        """Process raw data into usable format."""
        pass


class PostcodeDataProcessor(DataProcessor):
    """Concrete processor for UK postcode data."""

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def process_data(self, data_path: Path) -> pd.DataFrame:
        """Process data through pipeline."""
        df = self._load_data(data_path)
        df = self._clean_data(df)
        df = self._calculate_coordinates(df)
        return df

    def _load_data(self, path: Path) -> pd.DataFrame:
        return pd.read_csv(
            path,
            usecols=["latitude", "longitude"],
            dtype={"latitude": "float32", "longitude": "float32"},
        )

    def _clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.dropna().drop_duplicates()

    def _calculate_coordinates(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calculate grid coordinates from geographic data."""
        min_lat, max_lat = df.latitude.agg(["min", "max"])
        min_lon, max_lon = df.longitude.agg(["min", "max"])

        df["y"] = (
            ((max_lat - df.latitude) * (self.height - 1) / (max_lat - min_lat))
            .clip(0, self.height - 1)
            .astype(int)
        )
        df["x"] = (
            ((df.longitude - min_lon) * (self.width - 1) / (max_lon - min_lon))
            .clip(0, self.width - 1)
            .astype(int)
        )
        return df