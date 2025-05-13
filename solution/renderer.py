from abc import ABC, abstractmethod
import pandas as pd

class Renderer(ABC):
    """Abstract base class for rendering strategies."""

    @abstractmethod
    def render(self, data: pd.DataFrame) -> None:
        """Render processed data."""
        pass


class ASCIITextRenderer(Renderer):
    """Concrete renderer for ASCII text output."""

    def __init__(self, marker: str = "■"):
        self.marker = marker

    def render(self, data: pd.DataFrame) -> None:
        """Generate ASCII grid from coordinates."""
        unique_points = data[["y", "x"]].drop_duplicates()
        max_y = unique_points.y.max()
        max_x = unique_points.x.max()

        grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        for y, x in unique_points.itertuples(index=False, name=None):
            grid[y][x] = self.marker

        for row in grid:
            print("".join(row))