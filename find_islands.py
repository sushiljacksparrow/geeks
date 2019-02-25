t, n, m = map(int, input().split())
direction = [[0, 1],[0, -1], [1, 0], [-1, 0]]

for i in range(t):
    matrix = [[0 for i in range(n)] for j in range(m)]
    arr = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            matrix[i][j] = arr[i* + j]

    result = 0
    print(matrix, matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                print(i, j)
                result = result + 1
                stack = []
                matrix[i][j] = 0
                stack.append((i, j))

                while stack:
                    x,y = stack.pop()
                    for d in range(4):
                        print(x + direction[d][0], y + direction[d][1])
                        print("Hello")
                        if (x + direction[d][0] < n) & (x + direction[d][0] >= 0) & (y + direction[d][1] < m) & (y + direction[d][1] >= 0) & (matrix[x + direction[d][0]][y + direction[d][1]] == 1):
                            stack.append((x + direction[d][0], y + direction[d][1]))
                            matrix[x + direction[d][0]][y + direction[d][1]] = 0
    print(result)
