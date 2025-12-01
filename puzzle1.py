start_point = 50

# Part 1
def place(order, point) : 
    letter = list(order)[0]
    num = int(order.split(letter)[1].split("\n")[0])
    if (letter == "L"):
        point -= num
        point = point%100
    else: 
        point += num
        point = point%100
        
    return point

def main_part1():
    count = 0
    with open("input_1.txt", "r") as f:
        point = start_point
        for line in f:
            point = place(line, point)
            if (point == 0):
                count += 1

    print(f"Total of 0 : {count}")


main_part1()

# Part 2
def main_part2():
    total = 0
    with open("input_1.txt", "r") as f:
        point = start_point
        for line in f:
            s = line.strip()
            if not s:
                continue
            direction = s[0]
            steps = int(s[1:])

            if direction == "L":
                k0 = point if point != 0 else 100
            else:
                k0 = (100 - point) % 100
                if k0 == 0:
                    k0 = 100

            if k0 <= steps:
                hits = 1 + (steps - k0) // 100
            else:
                hits = 0

            total += hits
            point = place(line, point)

    print(f"Total of 0 with method 0x434C49434B : {total}")

main_part2()