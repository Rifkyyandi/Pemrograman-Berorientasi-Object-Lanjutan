def count_down(n):
    if n == 0:
        return
    else:
        print(n)
        count_down(n-1)

count_down(10000) # This will raise a RecursionError since the maximum recursion depth will be exceeded
