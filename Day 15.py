def main():
    shoes = list(map(int, input().split()))
    distinct = len(set(shoes))
    duplicates = 4 - distinct
    print(duplicates)

if __name__ == "__main__":
    main()