def monotonic(a):
    n = len(a)
    return (all(a[i]<=a[i+1] for i in range (n-1))) or all(a[i]>= a[i + 1] for i in ramge(n-1))
a = [6, 5, 4 3, 2]
print(monotonic(a))

