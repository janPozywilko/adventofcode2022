import typer
import re

test = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''


def find_unique(first_list, second_list):
    unique = list(set(first_list).intersection(second_list))
    return unique[0]

def find_unique_three(first_list, second_list, third_list):
    unique = list(set(first_list).intersection(second_list, third_list))
    return unique[0]

def calculate_value(string_value):
    ''' This function should return integer value converted from string with rule: Lowercase item types a through z have priorities 1 through 26, Uppercase item types A through Z have priorities 27 through 52'''

    value = 0

    if string_value.islower():
        value = ord(string_value) - 96
    elif string_value.isupper():
        value = ord(string_value) - 38

    return value

def part_one():
    with open('data.txt') as f:
        data = f.read().split('\n')
    unique = []
    sum = 0
    for row in data:
        first_compartment, second_compartment = row[:int(len(row)/2)], row[int(len(row)/2):]
        unique_val = find_unique(first_compartment, second_compartment)
        sum += calculate_value(unique_val)
        unique.append(unique_val)
    return sum

def part_two():
    with open('data.txt') as f:
        data = f.read()
    data = re.findall('((?:[^\n]+\n?){1,3})', data)
    unique = []
    sum = 0
    for row in data:
        first_rucksack, second_rucksack, third_rucksack = row.split('\n')[:3]
        unique_val = find_unique_three(first_rucksack, second_rucksack, third_rucksack)
        sum += calculate_value(unique_val)
        unique.append(unique_val)
    return sum


def main():
    part_one_res = part_one()
    print(f'Part one result: {part_one_res}')
    part_two_res = part_two()
    print(f'Part two result: {part_two_res}')


if __name__ == "__main__":
    typer.run(main)