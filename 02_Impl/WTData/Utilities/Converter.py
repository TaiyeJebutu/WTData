# Standard

# External

# Local
from WTData.Data.DataInterface import DataInterface
from WTData.Data.State import State
from WTData.Data.Map.StateMap import STATE_MAP

data_mapping: dict[DataInterface, dict[str, str]] = {}
data_mapping[State] = STATE_MAP


def convert(data: dict[str, str], target: DataInterface) -> DataInterface:
    """Converts data into its target type"""
    kwargs = {}
    for key in data.keys():
        if key in STATE_MAP:
            kwargs[STATE_MAP[key]] = data[key]

    return target(**kwargs)
