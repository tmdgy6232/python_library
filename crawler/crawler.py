import pandas as pd
class Cafe_crawler(object):
    limit = 4
    status = 0
    def __new__(cls, *args, **kwargs):
        print('인스턴스 생성')
        if cls.status < cls.limit:
            cls.status += 1
            return super().__new__(cls)
        else:
            raise ValueError("Cannot create more objects")
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
        #조회
        self.view_list = []
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
            # 조회
            splited = temp.split('class="td_view">')
            del splited[0:2]
            for i in splited:
                result = i.split('</td>')[0]
                self.view_list.append(result)
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
            '조회' : self.view_list,
            '좋아요': self.like_list
        }
        df = pd.DataFrame(dict_data)
        df = df.set_index('글번호')
        self.df = df
        return df

    def filtering(self, low, **kwargs):
        view_int_list = []
        for i in self.df['조회']:
            view_int_list.append((int(i)))
        self.df['조회int'] = view_int_list

        filter_data1 = self.df['조회int'] > low

        if kwargs.get('high'):
            filter_data2 = self.df['조회int'] < kwargs['high']
            return self.df[filter_data1 & filter_data2]
        else:
            return self.df[filter_data1]


# import pandas as pd
# class CafeCrawler:
#     def __init__(self, path):
#         f = open(path, "r", encoding='utf-8')
#         self.temp = f.read()
#         self.df = pd.DataFrame()
#     def make_num(self):
#         num = []
#         split = self.temp.split('<div class="inner_number">')
#         split.pop(0)
#         for i in split:
#             num.append(int(i.split('</div>')[0]))
#         self.df['번호'] = num
#     def make_title(self):
#         title = []
#         split = self.temp.split('<a class="article" ')
#         split.pop(0)
#         for i in split:
#             title.append(i.split('</a>')[0].split('>')[-1].strip())
#         self.df['제목'] = title
#     def make_writer(self):
#         writer = []
#         split = self.temp.split('<div class="article-board m-tcol-c">')[1].split('); return false;">')
#         split.pop(0)
#         for i in split:
#             writer.append(i.split('</a><span class="mem-level">')[0])
#         self.df['글쓴이'] = writer
    # def make_date(self):
    #     date = []
    #     split = self.temp.split('<div class="article-board m-tcol-c">')[1].split('<td class="td_date">')
    #     split.pop(0)
    #     for i in split:
    #         date.append(i.split('</td>')[0])
    #     self.df['날짜'] = date
    #
    #
    # def make_view(self):
    #     view = []
    #     split = self.temp.split('<div class="article-board m-tcol-c">')[1].split('<td class="td_view">')
    #     split.pop(0)
    #     for i in split:
    #         view.append(int(i.split('</td>')[0]))
    #     self.df['조회수'] = view
    #
    #
    # def make_likes(self):
    #     likes = []
    #     split = self.temp.split('<div class="article-board m-tcol-c">')[1].split('<td class="td_likes">')
    #     split.pop(0)
    #     for i in split:
    #         likes.append(int(i.split('</td>')[0]))
    #     self.df['좋아요'] = likes
    #
    # 데이터프레임 비교조건!!!!
    # def _split(self, keyword, **kwargs):
    #     list = []
    #     split = self.temp.split('<div class="article-board m-tcol-c">')[1].split(f'<td class="td_{keyword}">')
    #     split.pop(0)
    #     for i in split:
    #         if kwargs.get('casting'):
    #             list.append(int(i.split('</td>')[0]))
    #         else:
    #             list.append(i.split('</td>')[0])
    #     return list
    # def make_date(self):
    #     self.df['날짜'] = self._split('date')
    # def make_view(self):
    #     self.df['조회수'] = self._split('view', casting=True)
    # def make_likes(self):
    #     self.df['좋아요'] = self._split('likes', casing=True)
    # def generate_df(self):
    #     self.make_num()
    #     self.make_title()
    #     self.make_writer()
    #     self.make_date()
    #     self.make_view()
    #     self.make_likes()
    #     self.df.set_index('번호', inplace=True)
    #     return self.df
    # def filter_date(self, low, **kwargs):
    #     if kwargs.get('high'):
    #         return self.df[(self.df['날짜'] >= low)&(self.df['날짜'] < kwargs['high'])]
    #     else:
    #         return self.df[self.df['날짜'] >= low]
    # def filter_view(self, low, **kwargs):
    #     if kwargs.get('high'):
    #         return self.df[(self.df['조회수'] >= low)&(self.df['조회수'] < kwargs['high'])]
    #     else:
    #         return self.df[self.df['조회수'] >= low]
    # def filter_likes(self, low, **kwargs):
    #     if kwargs.get('high'):
    #         return self.df[low <= self.df['좋아요'] < kwargs['high']]
    #     else:
    #         return self.df[self.df['좋아요'] >= low]