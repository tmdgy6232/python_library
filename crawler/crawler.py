import pandas as pd
class Cafe_crawler(object):
    limit = 4
    status = 0
    def __new__(cls, *args, **kwargs):
        print('인스턴스 생성')
        return super().__new__(cls)
    def __init__(self, page):
        self.page = page
    def crawling_page(self):
        # 글번호
        self.number_list = []
        # 제목
        self.title_list = []
        # 작성자
        self.writer_list = []
        # 날짜
        self.date_list = []
        # 좋아요
        self.like_list = []
        with open(self.page, 'r', encoding='UTF-8') as f:
            temp = f.read()

            # 글번호
            splited = temp.split('<div class="inner_number">')
            splited.pop(0)
            for i in splited:
                text = (i.split('</div>'))
                self.number_list.append(text[0])

            # 제목
            splited = temp.split(' <a class="article"')
            splited.pop(0)
            for i in splited:
                result = ''
                second_splited = i.split('>')
                if '<span class="head' in second_splited[1]:
                    third_splited = second_splited[3].split('</a')
                else:
                    third_splited = second_splited[1].split('</a')
                result = third_splited[0]
                result = result.replace('\n', '').replace('\t', '').strip()
                self.title_list.append((result))

            # 작성자
            splited = temp.split('<a href="#" class="m-tcol-c"')
            del splited[0:2]
            for i in splited:
                second_splited = i.split('>')
                result = second_splited[1].split('</a')[0]
                self.writer_list.append(result)
            # 날짜
            splited = temp.split('class="td_date">')
            del splited[0:2]
            for i in splited:
                result = i.split('</td>')[0]
                self.date_list.append(result)

            # 좋아요
            splited = temp.split('class="td_likes">')
            del splited[0:2]
            for i in splited:
                result = i.split('</td>')[0]
                self.like_list.append(result)
    def make_df(self):
        dict_data = {
            '글번호': self.number_list,
            '제목': self.title_list,
            '작성자': self.writer_list,
            '날짜': self.date_list,
            '좋아요': self.like_list
        }
        df = pd.DataFrame(dict_data)
        df = df.set_index('글번호')
        return df
