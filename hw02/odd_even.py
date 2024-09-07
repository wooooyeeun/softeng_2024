def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def main():
    n = int(input("숫자를 입력하세요. : "))
    if is_even(n):
        print(f"{n}은 짝수입니다.")
    else:
        print(f"{n}은 홀수입니다.")


if __name__ == "__main__":
    main()