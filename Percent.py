from Unit import Unit
from typing import *

class Percent(Unit):
    def __init__(self, temperature: float, pressure: float) -> None:
        super().__init__(temperature, pressure)
        self.equip()

    def equip(self):
        self.solute_mass = float(input('용질의 질량(g): '))
        self.solution_mass = float(input('용액의 질량(g): '))
        self.commit()

    def commit(self) -> None:
        self.concentration = self.solute_mass / self.solution_mass * 100

    def increase_temperature(self, temperature_delta: float) -> None:
        self.temperature += temperature_delta

    def increase_pressure(self, pressure_delta: float) -> None:
        self.pressure += pressure_delta


    def add_solute_mass(self, solute_mass_delta: float) -> None:
        self.solute_mass += solute_mass_delta
        self.solution_mass += solute_mass_delta
        self.commit()

    def add_solvent_mass(self, solvent_mass_delta: float) -> None:
        self.solution_mass += solvent_mass_delta
        self.commit()

    def interpret(self, args: List[str]) -> None:
        target = args[0]
        value = float(args[1])
        action = args[2]

        if target == '온도':
            if action in ('감소', '줄이기'):
                self.increase_temperature(-value)

            elif action in ('증가', '올리기'):
                self.increase_temperature(value)

        elif target == '압력':
            if action in ('감소', '줄이기'):
                self.increase_pressure(-value)

            elif action in ('증가', '올리기'):
                self.increase_pressure(value)

        elif target == '용질':
            if action in ('덜기', ):
                self.add_solute_mass(-value)

            elif action in ('추가', '더하기'):
                self.add_solute_mass(value)

        elif target == '용매':
            if action in ('덜기', ):
                self.add_solvent_mass(-value)

            elif action in ('추가', '더하기'):
                self.add_solvent_mass(value)

    def print_status(self) -> None:
        print('온도:', self.temperature, 'K')
        print('압력: ', self.pressure, 'atm')
        print('용질:', self.solute_mass, 'g')
        print('용액:', self.solution_mass, 'g')
        print('농도:', self.concentration, '%')

