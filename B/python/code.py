def get_card_count(n, k, cards) -> int:
    # your code goes here
    s_max = s_left = sum(cards[:k])
    s_right = 0
    for i in range(1, k+1):
        s_left -= cards[k-i]
        s_right += cards[n-i]
        s_max = max(s_max, s_left+s_right)
    return s_max


n = int(input())
k = int(input())
cards = list(map(int, input().split()))

print(get_card_count(n, k, cards))
