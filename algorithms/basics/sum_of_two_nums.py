def add_large_numbers(num1, num2):
    result = []
    carry = 0
 
    # Make the lengths of both numbers equal by adding leading zeros
    num1 = num1.zfill(max(len(num1), len(num2)))
    num2 = num2.zfill(max(len(num1), len(num2)))
 
    # Iterate through digits from right to left
    for i in range(len(num1) - 1, -1, -1):
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        result.append(str(digit_sum % 10))
        carry = digit_sum // 10
 
    # Add any remaining carry
    if carry:
        result.append(str(carry))
 
    # Reverse the result and join to get the final sum
    return ''.join(result[::-1])
 
# Example usage:
num1 = "987654321987654321"
num2 = "123456789123456789"
print(add_large_numbers(num1, num2))
