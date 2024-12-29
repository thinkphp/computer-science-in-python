def farey_sequence(n):
    """Generate the Farey sequence of order n."""
    # Initialize the sequence with 0/1 and 1/1
    farey_seq = [(0, 1), (1, 1)]

    # Function to find the mediant of two fractions
    def mediant(a, b, c, d):
        return (a + c, b + d)

    # Use a while loop to generate the Farey sequence
    i = 0
    while i < len(farey_seq) - 1:
        a, b = farey_seq[i]
        c, d = farey_seq[i + 1]
        # Find the mediant fraction
        med_num, med_den = mediant(a, b, c, d)
        if med_den <= n:
            farey_seq.insert(i + 1, (med_num, med_den))
        else:
            i += 1

    return farey_seq

# Generate Farey sequence of order 5
n = 5
farey_seq = farey_sequence(n)
for numerator, denominator in farey_seq:
    print(f"{numerator}/{denominator}")
