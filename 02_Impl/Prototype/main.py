# Standard
import time
from dataclasses import dataclass
import ast
import json
# External
import requests

# Local

url = 'http://localhost:8111'
request = '/state'


def main():
    """Start of the program"""

    while True:
        response = requests.get(url + request)
        print(response.text)
        data = json.loads(response.text)

        state: State = decode(State, state_map, data)
        print(state)
        time.sleep(1 / 60)  # 60 fps


@dataclass
class State:
    valid: bool
    aileron: float
    elevator: float


state_map = {
    "valid": "valid",
    "aileron, %": "aileron",
    "elevator, %": "elevator"
}


def decode(obj: type, map: dict[str, str], data: dict[str, str]):
    kwargs = {}
    for key in data.keys():
        if key in map:
            kwargs[map[key]] = data[key]

    return obj(**kwargs)


if __name__ == "__main__":
    main()
