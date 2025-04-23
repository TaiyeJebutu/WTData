# Standard
import dataclasses
from dataclasses import dataclass

# External

# Local
from .DataInterface import DataInterface


@dataclass(frozen=True)
class State(DataInterface):
    valid: bool = dataclasses.Field(default=False)
    aileron: float = dataclasses.Field(default=0.0)
    elevator: float = dataclasses.Field(default=0.0)
    rudder: float = dataclasses.Field(default=0.0)
    flaps: float = dataclasses.Field(default=0.0)
    h_m: float = dataclasses.Field(default=0.0)
    tas: float = dataclasses.Field(default=0.0)
    ias: float = dataclasses.Field(default=0.0)
    m: float = dataclasses.Field(default=0.0)
    aoa_deg: float = dataclasses.Field(default=0.0)
    aos_deg: float = dataclasses.Field(default=0.0)
    ny: float = dataclasses.Field(default=0.0)
    vy: float = dataclasses.Field(default=0.0)
    wx: float = dataclasses.Field(default=0.0)
    mfuel: float = dataclasses.Field(default=0.0)
    mfuel_0: float = dataclasses.Field(default=0.0)
    throttle_1: float = dataclasses.Field(default=0.0)
    throttle_2: float = dataclasses.Field(default=0.0)
    throttle_3: float = dataclasses.Field(default=0.0)
    mixture_1: float = dataclasses.Field(default=0.0)
    mixture_2: float = dataclasses.Field(default=0.0)
    mixture_3_: float = dataclasses.Field(default=0.0)
    magneto_1: float = dataclasses.Field(default=0.0)
    magneto_2: float = dataclasses.Field(default=0.0)
    magneto_3: float = dataclasses.Field(default=0.0)
    power_1: float = dataclasses.Field(default=0.0)
    power_2: float = dataclasses.Field(default=0.0)
    power_3: float = dataclasses.Field(default=0.0)
    rpm1: float = dataclasses.Field(default=0.0)
    rpm_2: float = dataclasses.Field(default=0.0)
    rpm_3: float = dataclasses.Field(default=float)
    manifold_pressure_1: float = dataclasses.Field(default=0.0)
    manifold_pressure_2: float = dataclasses.Field(default=0.0)
    manifold_pressure_3: float = dataclasses.Field(default=0.0)
    oil_temp_1: float = dataclasses.Field(default=0.0)
    oil_temp_2: float = dataclasses.Field(default=0.0)
    oil_temp_3: float = dataclasses.Field(default=0.0)
    pitch_1_deg: float = dataclasses.Field(default=0.0)
    pitch_2_deg: float = dataclasses.Field(default=0.0)
    pitch_3_deg: float = dataclasses.Field(default=0.0)
    thrust_1: float = dataclasses.Field(default=0.0)
    thrust_2: float = dataclasses.Field(default=0.0)
    thrust_3: float = dataclasses.Field(default=0.0)
    efficiency_1: float = dataclasses.Field(default=0.0)
    efficiency_2: float = dataclasses.Field(default=0.0)
    efficiency_3: float = dataclasses.Field(default=0.0)
