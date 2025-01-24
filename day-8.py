class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        # Calculate the initial sum of the first B elements from the front
        current_sum = sum(A[:B])
        max_sum = current_sum

        # Use a sliding window to adjust the sum by removing elements from the front
        # and adding elements from the back
        for i in range(1, B + 1):
            current_sum = current_sum - A[B - i] + A[-i]
            max_sum = max(max_sum, current_sum)

        return max_sum

# Example usage
if __name__ == "__main__":
    solution = Solution()
    A1 = [5, -2, 3, 1, 2]
    B1 = 3
    print(solution.solve(A1, B1))  
    A2 = [1, 2]
    B2 = 1
    print(solution.solve(A2, B2))  
