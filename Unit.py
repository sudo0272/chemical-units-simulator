from typing import *

class Unit:
    def __init__(self, temperature, pressure) -> None:
        self.concentration = None
        self.temperature = temperature
        self.pressure = pressure

    def equip(self) -> None:
        pass

    def commit(self) -> None:
        pass

    def increase_temperature(self, temperature_delta: float) -> None:
        pass

    def increase_pressure(self, pressure_delta: float) -> None:
        pass

    def interpret(self, args: List[str]) -> None:
        pass

    def print_status(self) -> None:
        pass

