def findZigZagSequence(a, n):
    a.sort()
    # mid = int((n + 1)/2)
    mid = int((n - 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        # ed = ed + 1
        ed -= 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input()) #1
for cs in range (test_cases):
    n = int(input()) #5
    a = list(map(int, input().split())) # 2 3 5 1 4
    findZigZagSequence(a, n)



