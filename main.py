def solution(n):
    # TODO convert int to roman string
    converted = ''
    roman_numerals = {1000: 'M',
                    900: 'CM',
                    500: 'D',
                    400: 'CD',
                    100: 'C',
                    90: 'XC',
                    50: 'L',
                    40: 'XL',
                    10: 'X',
                    9: 'IX',
                    5: 'V',
                    4: 'IV',
                    1: 'I'}
    to_list = [int(x) for x in str(n)]
    notation = [v * 10**i for i, v in enumerate(to_list[::-1])]
    reversed_notation = reversed(notation)

    for i, v in enumerate(reversed_notation):
        if v in roman_numerals:
            converted += roman_numerals[v]
        else:
            for y in roman_numerals.keys():
                if v >= y:
                    if y == 1:
                        converted += roman_numerals[y] * v
                    else:
                        converted += roman_numerals[y]
                elif v <= 0:
                    break
                v -= y
    print(converted)

value = input("Enter num: ")
solution(int(value))