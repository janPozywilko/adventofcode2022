import typer

shapes_value = {'X': 1, 'Y': 2, 'Z': 3}
shapes_conversion = {'X': 'A', 'Y': 'B', 'Z': 'C'}

result_conversion = {'A X': 3, 'A Y': 1 + 3, 'A Z': 2 + 6, 'B X': 1, 'B Y': 2 + 3, 'B Z': 3 + 6, 'C X': 2, 'C Y': 3 + 3, 'C Z': 1 + 6}

test = '''A Y
B X
C Z'''


def part_one():
    with open('data.txt') as f:
        data = f.read().split('\n')
    score = 0
    for row in data:
        opponent, player = row.split(' ')
        print(f'{opponent},{player}')
        score += shapes_value.get(player)
        if opponent == 'A' and shapes_conversion.get(player) == 'B':
            score += 6
        elif opponent == 'B' and shapes_conversion.get(player) == 'C':
            score += 6
        elif opponent == 'C' and shapes_conversion.get(player) == 'A':
            score += 6
        elif opponent == shapes_conversion.get(player):
            score += 3
        print(score)
    return score

def part_two():
    with open('data.txt') as f:
        data = f.read().split('\n')

    score = 0

    for row in data:
        score += result_conversion.get(row)

    return score


def main():
    part_one_res = part_one()
    print(f'Part one result: {part_one_res}')
    part_two_res = part_two()
    print(f'Part two result: {part_two_res}')


if __name__ == "__main__":
    typer.run(main)