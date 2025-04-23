# Standard
import json
import time

# External
import requests
# Local
from Utilities import (
    convert, Shutdown
)
from WTData.Data import (
    State
)


class WTData:
    RATE = 0.5

    def __init__(self, url: str):
        self._url = url

    def _start_cycle(self):
        while not Shutdown.shutting_down():
            response = requests.get(self._url + '/state')
            data = json.loads(response.text)
            data['time_stamp'] = time.time_ns() / 1e6

            state: State = convert(data, State)
            print(state)
            time.sleep(1 / 60)

    def start(self):
        self._start_cycle()

    def stop(self):
        Shutdown.shutdown()
