from day11_1 import points_visited, run_program


points_visited[(0, 0)] = '#'  # starting panel is white


def print_map(point_colors):
    uppermost = min(k[1] for k in point_colors.keys())
    lowermost = max(k[1] for k in point_colors.keys())
    leftmost = min(k[0] for k in point_colors.keys())
    rightmost = max(k[0] for k in point_colors.keys())

    lines = []
    for y in range(uppermost, lowermost+1):
        line = ''.join([point_colors.get((x, y), '.') for x in range(leftmost, rightmost+1)])
        lines.append(line)

    for line in lines:
        print(line)


if __name__ == '__main__':
    with open('data/input11.txt') as f:
        content = f.read()
    program_instructions = [int(x) for x in content.split(',')]
    run_program(program_instructions)
    print_map(points_visited)  # BJRKLJUP
