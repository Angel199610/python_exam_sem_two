# a program to summ all numbers in a string
def sumOfList(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    numbers = [9, 2, 3, 5, 8]
    total_sum = sumOfList(numbers)
    print("The sum of all numbers in the list is:", total_sum)

if __name__ == "__main__":
    main()