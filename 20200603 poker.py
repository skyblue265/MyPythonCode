size=5
ans=0
card=[]
for i in range(size):
    card.append(input())
    if card[i] == 'a' or card[i]=='A' :
        ans = ans+1
    elif card[i] == 'j' or card[i]=='J':
        ans = ans+11
    elif card[i] == 'q' or card[i]=='Q':
        ans = ans+12
    elif card[i] == 'k' or card[i]=='K':
        ans = ans+13
    else:
        ans = ans + int(card[i])
print(ans)
