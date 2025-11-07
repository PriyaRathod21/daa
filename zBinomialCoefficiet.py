# Program to generate Binomial Coefficients using Dynamic Programming

def binomial_coefficient(n, k):
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    return dp[n][k]


# Print Pascal's Triangle up to n
def print_pascals_triangle(n):
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(i + 1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            print(dp[i][j], end=" ")
        print()


# Example usage
if __name__ == "__main__":
    n = 5
    k = 2
    print(f"Binomial Coefficient C({n}, {k}) =", binomial_coefficient(n, k))
    print("\nPascal's Triangle up to row", n, ":")
    print_pascals_triangle(n)
