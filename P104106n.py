def count_of_negatives(numbers: int) ->int:
    negativ =  0
    for i in numbers:
        if i < 0:
            negativ += 1
        else:
            negativ += 0
    return negativ
def main():
    n = int(input())
    for i in range(n):
        numbers = []
        line = input()
        tokens = line.split(" ")
        for token in tokens:
            numbers.append(int(token))
    print(count_of_negatives(numbers))
if __name__ == "__main__":
    main()