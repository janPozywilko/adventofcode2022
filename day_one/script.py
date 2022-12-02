import typer



def part_one():
    with open('data.txt') as data:
        elf_calories = data.read().split('\n\n')


    for idx ,elf in enumerate(elf_calories):
        calories_str = elf.split('\n')
        elf_calories[idx] = sum([int(cal) for cal in calories_str])

    return max(elf_calories)

def part_two():
    pass
   

def main():
    part_one_res = part_one()
    print(part_one_res)

if __name__ == "__main__":
    typer.run(main)