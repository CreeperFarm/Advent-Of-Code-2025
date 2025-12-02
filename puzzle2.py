# Part 1

def main_part1():
    count = 0
    with open("input_2.txt", "r") as f:
        for line in f:
            li = line.strip().split(",")
            for item in li:
                spl = item.split('-')
                start = int(spl[0])
                end = int(spl[1])
                for i in range(start, end+1):
                    string = str(i)
                    firstpart, secondpart = string[:len(string)//2], string[len(string)//2:]
                    #print(f"i: {i}, {firstpart}, {secondpart}")
                    if (firstpart == secondpart):
                        count += i
    print(f"The sum of invalid id is : {count}")

main_part1()

# Part 2

def main_part2():
    count = 0
    with open("input_2.txt", "r") as f:
        for line in f:
            li = line.strip().split(",")
            for item in li:
                spl = item.split('-')
                start = int(spl[0])
                end = int(spl[1])
                for i in range(start, end+1):
                    s = str(i)
                    L = len(s)
                    invalid = False
                    for j in range(1, L//2 + 1):
                        if L % j != 0:
                            continue
                        sub = s[:j]
                        if sub * (L // j) == s:
                            invalid = True
                            break
                    if invalid:
                        print(f"i: {i}, repeated pattern: {s}")
                        count += i
    print(f"The sum of invalid id is : {count}")
    
main_part2()