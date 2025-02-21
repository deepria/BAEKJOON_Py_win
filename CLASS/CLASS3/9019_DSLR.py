import sys
from collections import deque

transform = [[-1] * 4 for _ in range(10000)]
commands = "DSLR"

for num in range(10000):
    transform[num][0] = (num * 2) % 10000  # D
    transform[num][1] = num - 1 if num > 0 else 9999  # S
    transform[num][2] = (num % 1000) * 10 + num // 1000  # L
    transform[num][3] = (num % 10) * 1000 + num // 10  # R


def solve(A, B):
    if A == B:
        return ""

    queue = deque([A])
    visited = [-1] * 10000
    path = [""] * 10000

    visited[A] = A

    while queue:
        num = queue.popleft()

        for i in range(4):
            next_num = transform[num][i]
            if visited[next_num] == -1:
                visited[next_num] = num
                path[next_num] = path[num] + commands[i]
                queue.append(next_num)

                if next_num == B:
                    return path[next_num]


def sol():
    input_data = sys.stdin.read().split()
    T = int(input_data[0])
    result = []
    index = 1

    for _ in range(T):
        A, B = int(input_data[index]), int(input_data[index + 1])
        result.append(solve(A, B))
        index += 2

    sys.stdout.write("\n".join(result) + "\n")


sol()
