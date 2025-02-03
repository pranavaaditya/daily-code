# Calculate the sum of \( |X| + |Y| \) for all reachable positions of a robot moving along the X-axis in \( N \) moves.


def calculate_sum_of_positions(n):
    return n * (n + 1)

t = int(input())  
results = []

for _ in range(t):
    n = int(input()) 
    results.append(calculate_sum_of_positions(n))

for result in results:
    print(result)
