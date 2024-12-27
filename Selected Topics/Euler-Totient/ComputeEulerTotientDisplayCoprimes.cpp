import math

# Function to compute the Euler's totient function for each number up to n
def compute_totient(n):
    phi = [i for i in range(n + 1)]
    
    for i in range(2, n + 1):
        if phi[i] == i:  # Check if i is prime
            for j in range(i, n + 1, i):
                phi[j] = phi[j] // i * (i - 1)
    
    return phi

# Function to find and display numbers that are relatively prime to each number up to n
def display_relatively_prime_numbers(n, phi):
    for i in range(1, n + 1):
        relatively_prime_numbers = [j for j in range(1, i) if math.gcd(i, j) == 1]
        print(f"phi({i}) = {phi[i]}: Relatively prime numbers are: {relatively_prime_numbers}")

def main():
    n = int(input("Enter the value of n: "))
    
    phi = compute_totient(n)
    
    display_relatively_prime_numbers(n, phi)

if __name__ == "__main__":
    main()
