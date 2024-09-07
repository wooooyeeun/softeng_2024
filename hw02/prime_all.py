from hw02.prime import prime


def main():
    n = int(input("숫자를 입력하세요. : "))
    prime_list = []
    for i in range(1,n+1):
        if prime(i):
            prime_list.append(i)
    print(f"1부터 {n} 사이의 소수는 {prime_list} 입니다.")


if __name__ == "__main__":
    main()