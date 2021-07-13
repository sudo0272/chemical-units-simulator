from Unit import Unit
from typing import *

class Mol(Unit):
    def __init__(self, temperature: float, pressure: float) -> None:
        super().__init__(temperature, pressure)
        self.equip()

    def equip(self):
        self.solute_mol = float(input('용질(mol): '))
        self.solution_volume = float(input('용액의 부피(L): '))
        self.commit()

    def commit(self) -> None:
        self.concentration = self.solute_mol / self.solution_volume

    def increase_temperature(self, temperature_delta: float) -> None:
        self.solution_volume *= (1 + temperature_delta / 273)
        self.temperature += temperature_delta
        self.commit()

    def increase_pressure(self, pressure_delta: float) -> None:
        self.solution_volume = self.solution_volume * self.pressure / (self.pressure + pressure_delta)
        self.pressure += pressure_delta
        self.commit()

    def add_solute_mol(self, solute_mol_delta: float) -> None:
        self.solute_mol += solute_mol_delta
        self.commit()

    def interpret(self, args: List[str]):
        target = args[0]
        value = float(args[1])
        action = args[2]

        if target == '온도':
            if action in ('감소', '낮추기'):
                self.increase_temperature(-value)

            elif action in ('증가', '높이기'):
                self.increase_temperature(value)

        elif target == '압력':
            if action in ('감소', '낮추기'):
                self.increase_pressure(-value)

            elif action in ('증가', '높이기'):
                self.increase_pressure(value)

        elif target == '용질':
            if action in ('제거', '빼기'):
                self.add_solute_mol(-value)

            elif action in ('추가', '더하기'):
                self.add_solute_mol(value)

    def print_status(self) -> None:
        print('온도:', self.temperature, 'K')
        print('압력:', self.pressure, 'atm')
        print('용질:', self.solute_mol, 'mol')
        print('용액:', self.solution_volume, 'L')
        print('농도:', self.concentration, 'M')

