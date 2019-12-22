from day22_1 import shuffle


if __name__ == '__main__':
    with open('data/input22.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    deck = shuffle(lines, 119315717514047)
    print(deck.index(2020))

    # I need to figure out how to apply it 101741582076661 times tho
