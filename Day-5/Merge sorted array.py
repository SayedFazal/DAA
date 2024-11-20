n = int(input("Enter the size of the array: "))
a = []
print("Enter the elements of the array:")
for i in range(n):
    a.append(int(input()))
for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print("Sorted array:")
for i in range(n):
    print(a[i], end="\t")
