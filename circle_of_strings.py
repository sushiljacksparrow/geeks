# https://practice.geeksforgeeks.org/problems/circle-of-strings/0

for _ in range(int(input())):
    t = int(input())
    arr = list(map(str, input().split()))

    found = False
    for i in range(len(arr)):
        stack = []
        visited = [False]*len(arr);
        visited[i] = True
        stack.append(arr[i])
        count = 1
        last = arr[i]
        while stack:
            s = stack.pop()
            last = s
            for j in range(len(arr)):
                if (not visited[j]) and (s[-1:] == arr[j][:1]):
                    visited[j] = True
                    stack.append(arr[j])
                    count += 1

        if count == len(arr) and last[-1:] == arr[i][:1]:
            found = True
            break;
    if found:
        print(1)
    else:
        print(0)
