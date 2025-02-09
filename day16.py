
#You are given a number n. A supernatural number is a number whose product of digits is equal to n, and in this number there is no digit 1.

#Count the number of supernatural numbers for a given n.

def count_supernatural_numbers(n):
    def find_combinations(product, start):
        """Recursive function to find supernatural numbers."""
        if product == n:  
            return 1
        if product > n:  
            return 0
        count = 0
        for digit in range(start, 10): 
            count += find_combinations(product * digit, digit)  
        return count
    return find_combinations(1, 2)

n = int(input())
print(count_supernatural_numbers(n))
