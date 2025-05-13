from abc import ABC, abstractmethod
from pathlib import Path
import urllib.request
import zipfile


class DataFetcher(ABC):
    """Abstract base class for data fetching strategies."""

    @abstractmethod
    def fetch_data(self) -> None:
        """Fetch and prepare data source."""
        pass


class RemoteDataFetcher(DataFetcher):
    """Fetch data from remote source with caching."""

    def __init__(self, url: str, local_path: Path):
        self.url = url
        self.local_path = local_path

    def fetch_data(self) -> None:
        if self.local_path.exists():
            return

        print("Downloading dataset...")
        zip_path, _ = urllib.request.urlretrieve(self.url)

        try:
            with zipfile.ZipFile(zip_path, "r") as archive:
                csv_files = [f for f in archive.namelist() if f.endswith(".csv")]
                if not csv_files:
                    raise ValueError("No CSV file found in archive")

                archive.extract(csv_files[0])
                extracted = Path(csv_files[0])
                extracted.rename(self.local_path)
        finally:
            Path(zip_path).unlink()