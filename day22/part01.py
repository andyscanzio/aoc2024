from pathlib import Path


folder = Path(__file__).parent
test = folder / "test.txt"
input = folder / "input.txt"

with open(input, "r") as file:
    data = file.read()


def mix(num: int, secret: int) -> int:
    return num ^ secret


def prune(num: int) -> int:
    return num % 16777216


def next_secret(secret: int) -> int:
    secret = prune(mix(64 * secret, secret))
    secret = prune(mix(secret // 32, secret))
    secret = prune(mix(2048 * secret, secret))
    return secret


def nth_secret(secret: int, n: int) -> int:
    for _ in range(n):
        secret = next_secret(secret)
    return secret


secret_2000 = lambda secret: nth_secret(secret, 2000)

print(sum(map(secret_2000, map(int, data.splitlines()))))
