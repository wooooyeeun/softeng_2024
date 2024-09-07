def f2c(temp_f):
    return (temp_f - 32) * 5 / 9

def main():
    temp_f = int(input("화씨 온도를 입력하세요. : "))
    print(f"{temp_f} ℉ -> {f2c(temp_f):.2f} ℃")


if __name__ == "__main__":
    main()