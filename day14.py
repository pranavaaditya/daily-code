# Determine if a number 𝑥x can be represented as a sum of distinct powers of 𝑘k, given 𝑇 test cases.

def calculate_sum_of_positions(n):
    return n * (n + 1)

t = int(input())  
results = []

for _ in range(t):
    n = int(input()) 
    results.append(calculate_sum_of_positions(n))

for result in results:
    print(result)
def is_maths_beauty(x, k):
    while x > 0:
        remainder = x % k
        if remainder > 1: 
            return "NO"
        x //= k
    return "YES"
def main():
    import sys
    input = sys.stdin.read 
    data = input().splitlines()
    
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        x, k = map(int, data[i].split())
        results.append(is_maths_beauty(x, k))
    print("\n".join(results))

if __name__ == "__main__":
    main()
