def first(a):
    b = 3
    print("1.", a)
    return second(a * b) + b
def second(a):
    print("2.", a)
    return a % 4
def main():
    a = 5
    b = first(a)
    print("3.", b)
    b = second(b)
    print("4.", b)
main()
