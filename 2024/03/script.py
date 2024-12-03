import re
from typing import Any

with open("data_example.dat", "r") as f:
    example_data = f.read().strip()

with open("data.dat", "r") as f:
    data = f.read().strip()

with open("data_example_02.dat", "r") as f:
    example_data_2 = f.read().strip()

with open("data_02.dat", "r") as f:
    data_2 = f.read().strip()

def part_one(memory_string:str) -> int:
    regular_expression = "mul\(([0-9]{1,3}),([0-9]{1,3})\)"
    total = 0
    for instruction in (re.findall(regular_expression, memory_string)):
        total += int(instruction[0]) * int(instruction[1])
    return(total)

assert(part_one(example_data) == 161)
print(f"PART ONE RESULT: {part_one(data)}")

def part_two(memory_string:str) -> int:
    regular_expression = "(don't\(\)|do\(\))|mul\(([0-9]{1,3}),([0-9]{1,3})\)"
    total = 0
    powered: bool = True
    for instruction in (re.findall(regular_expression, memory_string)):
        if instruction[0] == "don't()":
            powered = False
        if instruction[0] == "do()":
            powered = True
        if (len(instruction[1]) > 0) and (len(instruction[2]) > 0) and powered:
            total += int(instruction[1]) * int(instruction[2])
    return(total)

assert(part_two(example_data_2) == 48)
print(f"PART TWO RESULT: {part_two(data_2)}")
