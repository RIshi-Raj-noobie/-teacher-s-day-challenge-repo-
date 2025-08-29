def main():
    n = int(input().strip())
    dominoes = []
    for _ in range(n):
        x, y = map(int, input().split())
        dominoes.append((x, y))

    total_upper = sum(x for x, y in dominoes)
    total_lower = sum(y for x, y in dominoes)

    if total_upper % 2 == 0 and total_lower % 2 == 0:
        print(0)
        return

    # Check if we can flip one domino to change the parity of both sums
    for i in range(n):
        x, y = dominoes[i]
        # If we flip this domino, the new upper becomes y and new lower becomes x.
        new_upper = total_upper - x + y
        new_lower = total_lower - y + x
        if new_upper % 2 == 0 and new_lower % 2 == 0:
            print(1)
            return

    print(-1)


if __name__ == "__main__":
    main()