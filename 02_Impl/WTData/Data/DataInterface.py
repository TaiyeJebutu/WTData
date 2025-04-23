# Standard
from dataclasses import dataclass


# External

# Local
@dataclass(frozen=True)
class DataInterface:
    time_stamp: int = 0
