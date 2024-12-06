with open("data_example.dat", "r") as f:
    example_data = f.read().split("\n\n")
    example_data_rules = example_data[0].split("\n")
    example_data_pages = example_data[1].rstrip().split("\n")

with open("data.dat", "r") as f:
    data = f.read().split("\n\n")
    data_rules = data[0].split("\n")
    data_pages = data[1].rstrip().split("\n")

def create_rulebook(rules: list[str]) -> dict[any, set]:
    rule_book = {}
    for rule in rules:
        index = rule.split("|")[1]
        if r := rule_book.get(index):
            r.add(rule.split("|")[0])
        else:
            rule_book[index] = {rule.split("|")[0]}
    return rule_book

def part_one(rulebook: dict[any, set], data: list[str]) -> int:
    total_count: int = 0
    for manual in data:
        current_manual_set = set()
        pages = manual.split(",")
        correct_order = True
        for index in range(len(pages),0,-1):
            current_page = pages[index-1]
            current_manual_set.add(current_page)
            if len(current_manual_set) > 0:
                rule = rulebook.get(current_page)
                if rule:
                    if len(rule.intersection(current_manual_set)):
                        correct_order = False
                        break
        if correct_order:
            total_count += int(pages[int(len(pages)/2)])
    return total_count


#assert(part_one(create_rulebook(example_data_rules), example_data_pages), 143)
#print(f"PART ONE COUNT TOTAL:{part_one(create_rulebook(data_rules), data_pages)}")


def part_two(rulebook: dict[any, set], data: list[str]) -> int:
    total_count: int = 0
    for manual in data:
        pages = manual.split(",")
        correct_order = True
        violation_exists = True
        while violation_exists:
            current_manual_set = set()
            for index in range(len(pages),0,-1):
                current_page = pages[index-1]
                current_manual_set.add(current_page)
                if len(current_manual_set) > 0:
                    rule = rulebook.get(current_page)
                    if rule:
                        violation_set = rule.intersection(current_manual_set)
                        if len(violation_set) > 0:
                            violation = violation_set.pop()
                            violation_index = pages.index(violation)
                            pages[violation_index], pages[index-1] = pages[index-1], pages[violation_index]
                            correct_order = False
                            violation_exists = True
                            break
                        else:
                            violation_exists = False
                    else:
                        violation_exists = False
        if not correct_order:
            total_count += int(pages[int(len(pages)/2)])
    return total_count


assert(part_one(create_rulebook(example_data_rules), example_data_pages), 123)
print(f"PART TWO COUNT TOTAL:{part_two (create_rulebook(data_rules), data_pages)}")
