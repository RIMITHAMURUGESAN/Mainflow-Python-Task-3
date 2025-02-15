def second_largest(lst):
    unique_numbers = list(set(lst))  # Remove duplicates
    if len(unique_numbers) < 2:
        return "No second largest number"
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]

# Input list
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Find second largest
print(f"Second largest number: {second_largest(numbers)}")