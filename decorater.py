
def deco(func):
    def wrapper():
        print(func.__name__, '함수시작 ㅗㅗ')
        func()
        print(func.__name__, '함수끝')
    return wrapper

@deco
def hello():
    print('hello')

@deco
def hi():
    print('hi')

hello()
hi()