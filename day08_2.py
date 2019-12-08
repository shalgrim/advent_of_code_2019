from day08_1 import get_layers


def find_locations_colors(location, layers):
    for layer in layers:
        if layer[location] == '2':
            continue
        return int(layer[location])


def convert_row(row):
    return ['X' if r == 1 else ' ' for r in row]


def main():
    layers = get_layers()
    colors = [find_locations_colors(i, layers) for i in range(150)]
    rows = [colors[i*25:(i+1)*25] for i in range(6)]
    converted_rows = [convert_row(row) for row in rows]
    for cr in converted_rows:
        print(''.join(cr))


if __name__ == '__main__':
    main()