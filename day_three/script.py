import typer

test = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''


def find_unique(first_list, second_list):
    unique = list(set(first_list).intersection(second_list))
    return unique[0]

def calculate_value(string_value):
    
    ''' This function should return integer value converted from string with rule: Lowercase item types a through z have priorities 1 through 26, Uppercase item types A through Z have priorities 27 through 52'''

    pass

def part_one():
    data = test.split('\n')
    unique = []
    sum = 0
    for row in data:
        first_compartment, second_compartment = row[:int(len(row)/2)], row[int(len(row)/2):]
        unique_val = find_unique(first_compartment, second_compartment)
        #sum += calculate_value(unique_val)
        unique.append(unique_val)
    return unique

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