import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("datafile", type=str)

args = parser.parse_args()



with open(args.datafile, 'r') as f:
    count = 0
    for row in f:
        row = row.rstrip().split(" ")
        result = True
        vector = False
        breaker_tripped = False
        next_value = None
        i = 0
        while len(row) >= 2:
            print(f"ROW:{row}")
            new_vector = int(row[0]) - int(row[1])
            change_result = 0 < abs(new_vector) < 4
            if vector:
                direction_result = (vector * new_vector) > 0
            else:
                direction_result = True
            if not(change_result and direction_result):
                if breaker_tripped:
                    result = False
                    break
                else:
                    breaker_tripped = True
                    del row[1]
            else:
                del row[0]
            vector = new_vector
        if result:
            count = count + 1
        print(f"RESULT:{result}")
    print(f"RESULT:{count}")

