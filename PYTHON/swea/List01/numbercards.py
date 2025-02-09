T = int(input())

for t in range(T):
    N = int(input())
    cards = list(map(int, list(input())))
    card_freq = [0] * (max(cards) + 1)
    
    for card in cards:
        card_freq[card] += 1
        
    most_freq_card = [i for i, v in enumerate(card_freq) if v == max(card_freq)]
        
    print(f'#{t + 1} {max(most_freq_card)} {max(card_freq)}')