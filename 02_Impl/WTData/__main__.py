# Standard
import argparse
import logging
import time
import datetime

# External

# Local
from WTData.WT_Data import WTData
from Utilities.Shutdown import Shutdown


def main():
    """Start the program"""
    logger.info("WTData Started")


# Setup arguments
parser = argparse.ArgumentParser(prog="WTData",
                                 description="Retrieves data from a Locally host War Thunder Server")

parser.add_argument('-l', '--log-level',
                    default="DEBUG",
                    choices=["DEBUG, INFO, WARNING"],
                    type=str)

parser.add_argument('-u', '--url',
                    default="http://localhost:8111",
                    type=str)

args = parser.parse_args()

# Setup logger

logger = logging.getLogger(__name__)
logging.basicConfig(filename=f"WTData_{datetime.datetime.now().strftime('%I_%M_%S')}",
                    format="%(asctime)s:%(message)s",
                    datefmt="%I:%M:%S",
                    level=args.log_level)

# Start WTData
wt_data = WTData(args.url)
wt_data.start()

while not Shutdown.shutting_down():

    key_press = input(': ')

    match key_press.lower():
        case 's':
            Shutdown.shutdown()
        case _:
            pass

if __name__ == "__main__":
    main()
