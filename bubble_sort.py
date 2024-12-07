def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

if __name__ == "__main__":
    numbers = list(map(int, input("Enter integer numbers separated by spaces: ").split()))
    sorted_numbers = bubble_sort(numbers)
    print("Sorted numbers are:", sorted_numbers)
