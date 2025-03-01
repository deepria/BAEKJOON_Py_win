from collections import deque


def min_jumps(n, arr):
    if n == 1:
        return 0

    queue = deque([(0, 0)])
    visited = [False] * n
    visited[0] = True

    while queue:
        pos, jumps = queue.popleft()

        for i in range(1, arr[pos] + 1):
            next_pos = pos + i
            if next_pos >= n:
                break
            if next_pos == n - 1:
                return jumps + 1
            if not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, jumps + 1))

    return -1


def sol():
    n = int(input())
    arr = list(map(int, input().split()))

    print(min_jumps(n, arr))


sol()
