import pandas as pd

#글번호
number_list = []
#제목
title_list = []
#작성자
writer_list = []
#날짜
date_list = []
#좋아요
like_list = []

# 제목 못가져옴
# with open('sourcetext.txt', 'r', encoding='UTF-8') as f:
#     print(len(f.readlines()))
#     for line in f.readlines():
#         if '<div class="inner_number">' in line:
#             text = line.split('<div class="inner_number">')
#             #print(text[1][0:6])
#             number_list.append(text[1][0:6])
with open('sourcetext.txt', 'r', encoding='UTF-8') as f:
    temp = f.read()

    #글번호
    splited = temp.split('<div class="inner_number">')
    splited.pop(0)
    for i in splited:
        text = (i.split('</div>'))
        number_list.append(text[0])

    #제목
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
        result = result.strip()
        title_list.append((result))

    #작성자
    splited = temp.split('<a href="#" class="m-tcol-c"')
    del splited[0:2]
    for i in splited:
        second_splited = i.split('>')
        result = second_splited[1].split('</a')[0]
        writer_list.append(result)
    #날짜
    splited = temp.split('class="td_date">')
    del splited[0:2]
    for i in splited:
        result = i.split('</td>')[0]
        date_list.append(result)

    # 좋아요
    splited = temp.split('class="td_likes">')
    del splited[0:2]
    for i in splited:
        result = i.split('</td>')[0]
        like_list.append(result)


dict_data = {
    '글번호' : number_list,
    '제목' : title_list,
    '작성자' : writer_list,
    '날짜' : date_list,
    '좋아요' : like_list
}
df = pd.DataFrame(dict_data)
print(df)

