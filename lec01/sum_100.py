from lec01.odd_even import is_even

def main():
    #total = 0

    #for i in range(1, 101):
    #    # total = total + i
    #    if is_even(i):
    #        total += i

    even_100 = [i for i in range(1, 101) if is_even(i)]
    #total = 0
    #for i in even_100:
    #    total += i
    #print(f"1부터 100까지 짝수의 합은 {total}입니다.")

    print(f"1부터 100까지 짝수의 합은 {sum(even_100)}")


if __name__ == "__main__":
    main()