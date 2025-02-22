import sys


def power_mod(a, n, c):
    a %= c
    if n == 0:
        return 1
    if n % 2 == 0:
        half = power_mod(a, n // 2, c)
        return (half * half) % c
    else:
        return (a * power_mod(a, n - 1, c)) % c


def sol():
    a, n, c = map(int, sys.stdin.read().strip().split())
    print(power_mod(a, n, c))


sol()