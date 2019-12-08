from collections import Counter


def main():
    layers = get_layers()
    counters = [Counter(l) for l in layers]
    num_zero_digits = [c.get('0', 0) for c in counters]
    fewest_zeros = min(num_zero_digits)
    print(fewest_zeros)
    fewest_zeros_loc = num_zero_digits.index(fewest_zeros)
    print(fewest_zeros_loc)
    return counters[fewest_zeros_loc]['1'] * counters[fewest_zeros_loc]['2']


def get_layers():
    with open('./data/input08.txt') as f:
        content = f.read().strip()
    layers = []
    for i in range(100):
        layers.append(content[150 * i:150 * (i + 1)])
    return layers


if __name__ == '__main__':
    print(main())

