with open('data.txt') as data:
    elf_calories = data.read().split('\n\n')


for idx ,elf in enumerate(elf_calories):
    calories_str = elf.split('\n')
    elf_calories[idx] = sum([int(cal) for cal in calories_str])
   
print(max(elf_calories))