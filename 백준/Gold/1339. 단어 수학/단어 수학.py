from collections import defaultdict

def main():
    N = int(input())
    words = [input() for _ in range(N)]
    
    letter_weight = defaultdict(int)
    
    for word in words:
        length = len(word)
        for i, ch in enumerate(word):
            letter_weight[ch] += 10 ** (length - i - 1)

    # 가중치 높은 순으로 숫자 배정
    sorted_letters = sorted(letter_weight.items(), key=lambda x: -x[1])
    number = 9
    letter_to_number = {}
    for letter, _ in sorted_letters:
        letter_to_number[letter] = number
        number -= 1
    
    total = 0
    for word in words:
        num = int(''.join(str(letter_to_number[ch]) for ch in word))
        total += num

    print(total)

if __name__ == "__main__":
    main()
