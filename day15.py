# You are given an integer array . Your task is to calculate the sum of absolute difference of indices of first and last occurrence for every integer that is present in array .Formally, if element occurs times in the array at indices , then the answer for  will be  if array is sorted.You are required to calculate the sum of the answer for every such  that occurs in the array.


def cal_sum_diff(test_cases):
    results = []
    for case in test_cases:
        n, array = case
        first_occurrence = {}
        last_occurrence = {}
        
        for idx, num in enumerate(array):
            if num not in first_occurrence:
                first_occurrence[num] = idx
            last_occurrence[num] = idx
        
        total = 0
        for num in first_occurrence:
            total += last_occurrence[num] - first_occurrence[num]
        
        results.append(total)
    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    test_cases = []
    
    for _ in range(T):
        N = int(data[idx])
        idx += 1
        array = list(map(int, data[idx:idx+N]))
        idx += N
        test_cases.append((N, array))
    
    results = cal_sum_diff(test_cases)
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()