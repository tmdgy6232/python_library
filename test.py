
list_cart = []
client = { 'name' : '임승효', 'cart' : list_cart}
menu_price = { '사과': '300원', '바나나': '680원', '블루베리': '1910원'}

list_cart.append('사과')
list_cart.append('바나나')
list_cart.append('블루베리')

def shopping_complete(client, menuprice):
    totalprice = 0
    print(f'{client["name"]} 님이 주문을 완료하셨습니다.')
    print('주문하신 내역은')
    for i in client['cart']:
        print(f'{i}이고 가격은 {menuprice[i]} 입니다.')
        totalprice += int(menuprice[i].split('원')[0])
    client.clear()
    print('주문이 완료되었습니다.')
    print(f'주문하신 총 금액은 {totalprice}원 입니다.')


shopping_complete(client, menu_price)

class Cart:
    def __init__(self, user):
        self.user = user
        self.total_price = 0
        self.cart_list = []
    def add_item(self, item):
        self.cart_list.append(item)
        print(f'{item.name}이 장바구니에 추가되었습니다.')
    def del_item(self, item):
        self.cart_list.remove(item)
        print(f'{item}이 장바구니에 삭제되었습니다.')
    def checkout(self):
        print('주문이 완료되었습니다')
        print('주문하신 내역은')
        for i in self.cart_list:
            print(f'{i.name},' , end='')
            self.total_price += i.price
        print(f'이며 총 가격은 {self.total_price} 입니다.')

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

user = Cart('임승효')
user.add_item(Item('사과', 300))
user.add_item(Item('바나나', 500))
user.add_item(Item('과자', 800))

user.checkout()

a_user_cart = []
b_user_cart = []
a_user = {'name' : 'a', 'cart' : a_user_cart}
b_user = {'name' : 'b', 'cart' : b_user_cart}

client = { 'name' : '임승효', 'cart' : list_cart}
사과 = {'가격' : 300, '신선도' : 9, '크기' : ''}
바나나 = { '가격' : 680, '신선도' : 4, '크기' : ''}
블루베리 = { '가격' : 1910, '신선도' : 8, '크기' : ''}
볼펜 = { '가격' : 1100, '신선도' : 0, '크기' : ''}
소파 = { '가격' : 39800, '신선도' : 0, '크기' : 450}

fruit_list = [사과, 바나나, 블루베리]

a_user_cart.append(사과)
a_user_cart.append(바나나)
a_user_cart.append(블루베리)
a_user_cart.append(볼펜)
a_user_cart.append(소파)

b_user_cart.append(바나나)
b_user_cart.append(사과)

def order_checckout(user):
    print(f'{user["name"]} 님의 주문이 완료되었습니다.')
    total_price = 0
    in_fruit = False
    total_fresh = 0
    order_fruit_size = 0
    for i in user['cart']:
        total_price += i['가격']
        if i in fruit_list:
            in_fruit = True
            order_fruit_size += 1
            total_fresh += i['신선도']
    print(f'주문하신 총 가격은 {total_price}원 입니다.')
    if in_fruit:
        print(f'주문하신 과일의 평균 신선도는 {total_fresh / order_fruit_size} 입니다.')

order_checckout(a_user)












