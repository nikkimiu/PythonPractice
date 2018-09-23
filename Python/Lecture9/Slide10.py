def get_part(digits, start, end):
    num = int(digits[start: end])
    return num
def num_fiddle(digit_str, length):
    part_way = length // 2
    part1 = get_part(digit_str, 0, part_way)
    part2 = get_part(digit_str, part_way, length)
    return part1 + part2
def display_results(num1, num2):
    print(num1, ", ", num2, sep = "")
def main():
    num = 3271
    fiddled = num_fiddle(str(num), len(str(num)))
    display_results(num - 5, fiddled)
main()
