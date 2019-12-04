LO = 123257
HI = 647015


def is_valid_pw(num, ignore_range=False):
    if not ignore_range and (num < LO or num > HI):
        return False

    if len(str(num)) != 6:
        return False

    digits = [int(c) for c in str(num)]
    repeater = False

    for i in range(1, 6):
        if digits[i] < digits[i-1]:
            return False
        if digits[i] == digits[i-1]:
            repeater = True

    return repeater


def count_valid_pws(lo, hi):
    num_valid = 0
    for i in range(lo, hi+1):
        if is_valid_pw(i):
            num_valid += 1

    return num_valid


if __name__ == '__main__':
    print(count_valid_pws(LO, HI))
