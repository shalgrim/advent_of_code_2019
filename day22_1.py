def deal_with_increment(increment, deck):
    new_deck = [None] * len(deck)
    next_index = 0
    for card in deck:
        new_deck[next_index] = card
        if next_index + increment < len(deck):
            next_index += increment
        else:
            difference = next_index + increment - len(deck)
            next_index = difference

    return new_deck


def process_instruction(instruction, deck):
    if instruction.startswith('deal with increment'):
        return deal_with_increment(int(instruction.split()[-1]), deck)
    elif instruction == 'deal into new stack':
        deck.reverse()
        return deck
    elif instruction.startswith('cut'):
        cut_index = int(instruction.split()[-1])
        return deck[cut_index:] + deck[:cut_index]


def shuffle(instructions, deck_size):
    print('about to build deck')
    deck = [i for i in range(deck_size)]
    print('built deck')

    for instruction in instructions:
        print(f'{instruction=}')
        deck = process_instruction(instruction, deck)

    return deck


if __name__ == '__main__':
    with open('data/input22.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(shuffle(lines, 10007).index(2019))  # 2272 is wrong...I asked for val at index 2019
