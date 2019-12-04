from day04_1 import LO, HI
from day04_1 import count_valid_pws

from collections import Counter


def is_valid_pw_stricter(num, ignore_range=False):
    if not ignore_range and (num < LO or num > HI):
        return False

    snum = str(num)
    if len(snum) != 6:
        return False

    counter = Counter(snum)
    if 2 not in counter.values():
        return False

    digits = [int(c) for c in str(num)]
    for i in range(1, 6):
        if digits[i] < digits[i-1]:
            return False

    return True


if __name__ == '__main__':
    print(count_valid_pws(LO, HI, algorithm=is_valid_pw_stricter))
