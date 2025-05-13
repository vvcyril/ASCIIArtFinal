from pathlib import Path

from data_fetcher import DataFetcher, RemoteDataFetcher
from data_processor import DataProcessor, PostcodeDataProcessor
from renderer import Renderer, ASCIITextRenderer


class UKMapGenerator:
    """Facade for map generation process."""

    def __init__(
            self,
            fetcher: DataFetcher,
            processor: DataProcessor,
            renderer: Renderer
    ):
        self.fetcher = fetcher
        self.processor = processor
        self.renderer = renderer

    def generate(self, data_path: Path) -> None:
        """Orchestrate the generation process."""
        self.fetcher.fetch_data()
        processed_data = self.processor.process_data(data_path)
        self.renderer.render(processed_data)


class MapGeneratorFactory:
    """Create configured map generator instances."""

    @staticmethod
    def create_generator(
            width: int,
            height: int,
            marker: str
    ) -> UKMapGenerator:
        """Factory method for creating configured generators."""
        data_path = Path("ukpostcodes.csv")
        fetcher = RemoteDataFetcher(
            url=(
                "https://github.com/dwyl/uk-postcodes-latitude-longitude-"
                "complete-csv/raw/master/ukpostcodes.csv.zip"
            ),
            local_path=data_path,
        )
        processor = PostcodeDataProcessor(width=width, height=height)
        renderer = ASCIITextRenderer(marker=marker)
        return UKMapGenerator(fetcher, processor, renderer)