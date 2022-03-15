import sys
def is_strictly_monotone_decreasing(numbers: int) ->int:
    for i in numbers:
        if numbers[1] > numbers[2]:
            return "True"
        else:
            return "False"
def main():
    szamok = sys.stdin.readline()
    for i in szamok:
        numbers = []
        line = szamok.strip()
        tokens = line.split(" ")
        for token in tokens:
            numbers.append(int(token))
    print(is_strictly_monotone_decreasing(numbers))
if __name__ == "__main__":
    main()
