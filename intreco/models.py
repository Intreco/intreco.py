from dataclasses import dataclass
import datetime

@dataclass
class User:
    id: str
    first_name: str
    last_name: str
    email: str
    staff: bool
    created_at: datetime.datetime

@dataclass
class TempHumSensor:
    serial_number: str
    created_at: datetime.date
    last_updated: datetime.datetime
    state: list
    activated_at: datetime.datetime
    name: str

    @property
    def temperature(self) -> int:
        return self.state["temp"]

    @property
    def humidity(self) -> int:
        return self.state["humidity"]