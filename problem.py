def sum(n):
    return n * (n + 1) // 2  # Using integer division for Python 3

t = int(input())
for _ in range(t):
    k, l, r = map(int, input().split())
    ans = -1
    while r >= l:
        if k == 1:
            if (sum(r) - sum(l - 1)) % 2 == 1:
                ans = r
                break  # Exit the loop once we find the answer
        else:
            if (sum(r) - sum(l - 1)) % 2 == 0:  # Corrected condition for even summation
                ans = r
                break  # Exit the loop once we find the answer
        r -= 1
    print(ans)
