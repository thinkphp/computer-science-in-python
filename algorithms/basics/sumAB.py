'''
Find the sum of given two numbers A and B. if numberofDigit(A)==numberofDigit(A+B) then print A+B else Print A

Input Format

input contain two numbers(A and B) separated by space
'''
def number_of_digits(n):
    return len(str(n))

def find_sum_or_a(A, B):
    sum_result = A + B
    digits_A = number_of_digits(A)
    digits_sum = number_of_digits(sum_result)

    if digits_A == digits_sum:
        print(sum_result)
    else:
        print(A)

# Input
input_numbers = input().split()
if len(input_numbers) == 1:
    # If input is on separate lines
    A = int(input_numbers[0])
    B = int(input())
else:
    # If input is separated by spaces
    A = int(input_numbers[0])
    B = int(input_numbers[1])

# Output
find_sum_or_a(A, B)
