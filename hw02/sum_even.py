from hw02.odd_even import is_even


def main():
    n = int(input("숫자를 입력하세요. : "))
    total = 0
    # 1
    for i in range(1, n+1):
        if is_even(i):
            total += i
    print(f"1부터 {n}까지 짝수의 합은 {total}입니다.")

    # 2
    even_total = [i for i in range(1, n+1) if is_even(i)]
    print(f"1부터 {n}까지 짝수의 합은 {sum(even_total)}입니다.")


if __name__ == "__main__":
    main()