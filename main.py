#!/bin/python3


"""  0   1   2   3   4   5   6   7   8   9

 A   _       _   _       _   _   _   _   _
BDC | |   |  _|  _| |_| |_  |_    | |_| |_|
EGF |_|   | |_   _|   |  _| |_|   | |_|  _|

"""

LED_LABELS = tuple('ABCDEFG')

#      binary         seven segment
#   (2³ 2² 2¹ 1): (A  B  C  D  E  F  G)
TRUTH_TABLE = {
    (0, 0, 0, 0): (1, 1, 1, 0, 1, 1, 1),  # 0
    (0, 0, 0, 1): (0, 0, 1, 0, 0, 1, 0),  # 1
    (0, 0, 1, 0): (1, 0, 1, 1, 1, 0, 1),  # 2
    (0, 0, 1, 1): (1, 0, 1, 1, 0, 1, 1),  # 3
    (0, 1, 0, 0): (0, 1, 1, 1, 0, 1, 0),  # 4
    (0, 1, 0, 1): (1, 1, 0, 0, 1, 0, 1),  # 5
    (0, 1, 1, 0): (1, 1, 0, 1, 1, 1, 1),  # 6
    (0, 1, 1, 1): (1, 0, 1, 1, 0, 1, 0),  # 7
    (1, 0, 0, 0): (1, 1, 1, 1, 1, 1, 1),  # 8
    (1, 0, 0, 1): (1, 1, 1, 1, 0, 1, 1),  # 9
}

# TRUTH_TABLE_OUT = { value: key for key, value in TRUTH_TABLE_IN.items() }


def led_to_bin(table: dict[tuple: tuple]) -> str:

    num_of_bits = len(list(table.keys())[0])
    for bit_indice in range(num_of_bits):

        sum = ''
        print(1 + bit_indice)
        for bits, leds in table.items():
            if bits[bit_indice]:
                sum += ' + ' if sum else ''
                sum += ''.join(LED_LABELS[i].upper() if led else
                               LED_LABELS[i].lower()
                               for i, led in enumerate(leds))
        print(sum)

        """
            print(' + ' if i else '', end='')
            for i, led in enumerate(leds):
                print(LED_LABELS[i].upper() if led else
                      LED_LABELS[i].lower(),
                      end='')"""


print('\nLEDS TO BITS\n')
led_to_bin(TRUTH_TABLE)
print('\nBITS TO LEDS\n')
led_to_bin(dict(zip(TRUTH_TABLE.values(),
                    TRUTH_TABLE.keys())))
print()
