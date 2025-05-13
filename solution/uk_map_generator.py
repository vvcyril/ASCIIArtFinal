import argparse
import sys
from pathlib import Path
from map_generator import MapGeneratorFactory

def main() -> None:
    """Command-line interface configuration."""
    parser = argparse.ArgumentParser(
        description="Generate UK map ASCII art from postcode data"
    )
    parser.add_argument(
        "-w",
        "--width",
        type=int,
        default=80,
        help="Output width in characters",
    )
    parser.add_argument(
        "-ht",
        "--height",
        type=int,
        default=24,
        help="Output height in characters",
    )
    parser.add_argument(
        "-m",
        "--marker",
        type=str,
        default="*",
        help="Character to use for land markers",
    )
    args = parser.parse_args()

    try:
        generator = MapGeneratorFactory.create_generator(
            width=args.width,
            height=args.height,
            marker=args.marker,
        )
        data_path = Path("ukpostcodes.csv")
        generator.generate(data_path)
    except (IOError, ValueError) as e:
        print(f"Generation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()