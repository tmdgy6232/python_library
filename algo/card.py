def make_card(num):
    card_list = []
    for i in range(num):
        card_list.append(i+1)
    card_list.reverse()
    return card_list

def pic_card(card_list):
    if len(card_list) == 1:
        return card_list
    else:
        # 맨 위 카드 제거
        card_list.pop()
        # 그 다음카드 제일 아래로 옮기기
        last_card = card_list.pop()
        card_list.insert(0, last_card)
        #재귀 호출
        return pic_card(card_list)

card_list = make_card(4)
last = pic_card(card_list)
print(last)