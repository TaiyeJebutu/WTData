# Standard
import argparse
import logging
import time
import datetime


# External

# Local


def main():
    """Start the program"""
    logger.info("WTData Started")


# Setup arguments
parser = argparse.ArgumentParser(prog="WTData",
                                 description="Retrieves data from a Locally host War Thunder Server")

parser.add_argument('-l', '--log-level',
                    default="DEBUG",
                    choices=["DEBUG, INFO, WARNING"])

args = parser.parse_args()

# Setup logger

logger = logging.getLogger(__name__)
logging.basicConfig(filename=f"WTData_{datetime.datetime.now().strftime('%I_%M_%S')}",
                    format="%(asctime)s:%(message)s",
                    datefmt="%I:%M:%S",
                    level=args.log_level)

if __name__ == "__main__":
    main()
