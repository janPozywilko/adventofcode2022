import typer

shapes_value = {'X': 1, 'Y': 2, 'Z': 3}
shapes_conversion = {'X': 'A', 'Y': 'B', 'Z': 'C'}

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
    pass


def main():
    part_one_res = part_one()
    print(f'Part one result: {part_one_res}')
    #part_two_res = part_two()
    #print(f'Part two result: {part_two_res}')
    print()


if __name__ == "__main__":
    typer.run(main)