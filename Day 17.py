def main():
    n = int(input().strip())
    cards = list(map(int, input().split()))

    left = 0
    right = n - 1
    sereja_score = 0
    dima_score = 0
    turn = 0  # 0 for Sereja, 1 for Dima

    while left <= right:
        if cards[left] > cards[right]:
            chosen = cards[left]
            left += 1
        else:
            chosen = cards[right]
            right -= 1

        if turn == 0:
            sereja_score += chosen
            turn = 1
        else:
            dima_score += chosen
            turn = 0

    print(sereja_score, dima_score)


if __name__ == "__main__":
    main()