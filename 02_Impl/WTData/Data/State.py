# Standard
import dataclasses
from dataclasses import dataclass, field

# External

# Local
from .DataInterface import DataInterface


@dataclass(frozen=True)
class State(DataInterface):
    valid: bool = False
    aileron: float = field(default_factory=float)
    elevator: float = field(default_factory=float)
    rudder: float = field(default_factory=float)
    flaps: float = field(default_factory=float)
    h_m: float = field(default_factory=float)
    tas: float = field(default_factory=float)
    ias: float = field(default_factory=float)
    m: float = field(default_factory=float)
    aoa_deg: float = field(default_factory=float)
    aos_deg: float = field(default_factory=float)
    ny: float = field(default_factory=float)
    vy: float = field(default_factory=float)
    wx: float = field(default_factory=float)
    mfuel: float = field(default_factory=float)
    mfuel_0: float = field(default_factory=float)
    throttle_1: float = field(default_factory=float)
    throttle_2: float = field(default_factory=float)
    throttle_3: float = field(default_factory=float)
    mixture_1: float = field(default_factory=float)
    mixture_2: float = field(default_factory=float)
    mixture_3_: float = field(default_factory=float)
    magneto_1: float = field(default_factory=float)
    magneto_2: float = field(default_factory=float)
    magneto_3: float = field(default_factory=float)
    power_1: float = field(default_factory=float)
    power_2: float = field(default_factory=float)
    power_3: float = field(default_factory=float)
    rpm1: float = field(default_factory=float)
    rpm_2: float = field(default_factory=float)
    rpm_3: float = field(default=float)
    manifold_pressure_1: float = field(default_factory=float)
    manifold_pressure_2: float = field(default_factory=float)
    manifold_pressure_3: float = field(default_factory=float)
    oil_temp_1: float = field(default_factory=float)
    oil_temp_2: float = field(default_factory=float)
    oil_temp_3: float = field(default_factory=float)
    pitch_1_deg: float = field(default_factory=float)
    pitch_2_deg: float = field(default_factory=float)
    pitch_3_deg: float = field(default_factory=float)
    thrust_1: float = field(default_factory=float)
    thrust_2: float = field(default_factory=float)
    thrust_3: float = field(default_factory=float)
    efficiency_1: float = field(default_factory=float)
    efficiency_2: float = field(default_factory=float)
    efficiency_3: float = field(default_factory=float)
