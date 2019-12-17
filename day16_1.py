from copy import copy


PATTERN = [0, 1, 0, -1]


def get_modified_pattern(base_pattern, digit_index, len_needed):
    base_pattern_multiplied = []

    for p in base_pattern:
        base_pattern_multiplied += [p] * digit_index

    while len(base_pattern_multiplied) < len_needed:
        base_pattern_multiplied += base_pattern_multiplied

    base_pattern_multiplied.append(base_pattern[0])
    output = base_pattern_multiplied[1:]

    return output


def apply_fft(in_number, num_phases):
    in_list = [int(c) for c in in_number]
    working_list = copy(in_list)

    for _ in range(num_phases):
        temp_list = []

        for j in range(1, len(working_list) + 1):
            modified_pattern = get_modified_pattern(PATTERN, j, len(in_list))
            new_digit = 0

            for pattern_num, existing_num in zip(modified_pattern, working_list):
                new_digit += pattern_num * existing_num

            new_digit = abs(new_digit) % 10
            temp_list.append(new_digit)

        working_list = temp_list

    return ''.join([str(d) for d in working_list])


def main(in_number, num_phases, num_digits):
    big_number = apply_fft(in_number, num_phases)
    return big_number[:num_digits]


if __name__ == '__main__':
    with open('data/input16.txt') as f:
        content = f.read().strip()

    print(main(content, 100, 8))
