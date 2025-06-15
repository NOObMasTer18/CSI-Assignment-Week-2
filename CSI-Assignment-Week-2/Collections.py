from collections import Counter

# Input number of shoes and the shoe sizes
X = int(input())
shoe_sizes = list(map(int, input().split()))
shoe_count = Counter(shoe_sizes)

# Input number of customers
N = int(input())
earnings = 0

# For each customer
for _ in range(N):
    size, price = map(int, input().split())
    if shoe_count[size] > 0:
        earnings += price
        shoe_count[size] -= 1

print(earnings)