class Phone:
    def __init__(self, **kwargs):
        self.number = kwargs['number']
        self.user = kwargs['user']
        self.company = kwargs['company']
        self.serial_number = kwargs['serial_number']

    def turnOn(self):
        print(f'{self.user}')
        print(f'{self.number}')
        print(f'{self.company}')
    def call(self, number):
        print(f'{number}로 전화를 겁니다.')
    def turnOff(self):
        print('전원을 끕니다')

class SmartPhone(Phone):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.os = kwargs['os']
    def turnOn(self):
        super().turnOn()
        print('LTE를 켭니다.')
    def init_internet(self):
        print('인터넷 시작')

    def writeImfomation(self):
        with open('test.txt', 'w', encoding='UTF-8') as f:
            f.write(f'사용자이름 : {self.user} \n')
            f.write(f'전화번호 : {self.number} \n')
            f.write(f'통신사 : {self.company} \n')
            f.write(f'일련번호 : {self.serial_number} \n')
    def read(self):
        with  open('test.txt', 'r', encoding='UTF-8') as f:
            data = f.readlines()
            print(data)
dictData = {
    'number' : '01075200858',
    'user' : 'lim',
    'company' : 'LG',
    'serial_number' : '35134513435',
    'os' : 'android'
}