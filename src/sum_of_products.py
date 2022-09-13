#!/bin/python3

LED_LABELS = tuple('abcdefg')

def sum_of_products(table: dict[tuple: tuple]) -> tuple[str]:

    num_of_bits = len(list(table.keys())[0])
    for bit_indice in range(num_of_bits):

        sum = ''
        for bits, leds in table.items():
            if bits[bit_indice]:
                sum += ' + ' if sum else ''
                sum += ' '.join(LED_LABELS[i] if led else
                                f'!{LED_LABELS[i]}'
                                for i, led in enumerate(leds))
        print(sum + '\n')
