from day16_01 import apply_fft


def adjust_in_number(number):
    adjusted_string = str(number) * 10000
    return int(adjusted_string)


def main(in_number, num_phases, num_digits):
    adjusted_number = adjust_in_number(in_number)
    big_number = apply_fft(in_number, num_phases)
    return int(''.join(str(big_number)[:num_digits]))
