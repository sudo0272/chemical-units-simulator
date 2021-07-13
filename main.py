from Percent import Percent
from PPM import PPM
from Mol import Mol
from Molal import Molal

print('화학 농도 시뮬레이션')
temperature = float(input('초기 온도(K): '))
pressure = float(input('초기 압력(atm): '))
units = [
    (Percent, '퍼센트 농도'),
    (PPM, 'PPM 농도'),
    (Mol, '몰 농도'),
    (Molal, '몰랄 농도')
]

for index, item in enumerate(units):
    print(index + 1, ':', item[1])

unit_index = None
while True:
    try:
        unit_index = int(input('번호 입력: ')) - 1

        if unit_index < len(units):
            break

        else:
            print('다시 입력해주세요')

    except ValueError:
        print('다시 입력해주세요')

unit = units[unit_index][0](temperature, pressure)
print('-' * 20)
unit.print_status()
while True:
    try:
        args = input(' > ')

        if args == 'q':
            break

        unit.interpret(args.split())
        unit.print_status()

    except:
        pass

