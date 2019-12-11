from collections import Counter


LO = 123257
HI = 647015


def is_valid_pw(num, ignore_range=False, strict=False):
    if not ignore_range and (num < LO or num > HI):
        return False

    snum = str(num)
    if len(snum) != 6:
        return False

    if strict:
        counter = Counter(snum)
        if 2 not in counter.values():
            return False

    digits = [int(c) for c in str(num)]
    repeater = False

    for i in range(1, 6):
        if digits[i] < digits[i-1]:
            return False
        if digits[i] == digits[i-1]:
            repeater = True

    return repeater


def count_valid_pws(lo, hi, strict=False):
    num_valid = 0
    for i in range(lo, hi+1):
        if is_valid_pw(i, False, strict):
            num_valid += 1

    return num_valid


if __name__ == '__main__':
    print(count_valid_pws(LO, HI))
