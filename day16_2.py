from day16_1 import apply_fft


def main(in_number, num_phases, num_digits):
    offset = int(in_number[:7])
    big_number = apply_fft(in_number * 10000, num_phases)
    return big_number[offset:offset + num_digits]
