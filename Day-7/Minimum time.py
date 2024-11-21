def minimum_assembly_time(n, a1, a2, t1, t2, e1, e2, x1, x2):
    dp1 = e1 + a1[0]
    dp2 = e2 + a2[0]  
    for i in range(1, n):
        new_dp1 = min(dp1 + a1[i], dp2 + t2[i-1] + a1[i])
        new_dp2 = min(dp2 + a2[i], dp1 + t1[i-1] + a2[i])
        dp1, dp2 = new_dp1, new_dp2
    return min(dp1 + x1, dp2 + x2)
n = 4
a1 = [4, 5, 3, 2]
a2 = [2, 10, 1, 4]
t1 = [7, 4, 5]
t2 = [9, 2, 8]
e1 = 10
e2 = 12
x1 = 18
x2 = 7
result = minimum_assembly_time(n, a1, a2, t1, t2, e1, e2, x1, x2)
print(f"The minimum time required to process the product: {result}")

Output:The minimum time required to process the product: 35
