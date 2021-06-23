import numpy as np
import pandas as pd
from random import *
import seaborn as sns
s = pd.Series([1, 3, 5, 6], index=[
    '하나','둘','셋','넷'
])

list_data = [1,2,3,4,5]
series = pd.Series(list_data)

list_index = ['하나', '둘', '셋', '넷', '다섯']
new_series = pd.Series(list_data, index = list_index)

dict_data = {'a' : 1, 'b' : 2}
sr = pd.Series(dict_data)


series_data = pd.Series(['홍길동', '26', '01075200858', '광주'], index=['가','나','다','라'])

#정수형 위치 인덱스
num_index_data = series_data[1]

#인덱스 이름으로 가져오기

#여러개의 원소 가져오기
new = series_data[['가','라']]

#슬라이싱

new = series_data[0:2]
new = series_data['나':'라']

#new.index
#new.values

#data frame 만들기
list_data_2d = [[23, '남', '부산'],[21, '여', '서울'],[25, '남', '광주'],[27, '여', '대전'],[24, '여', '광주']]

df = pd.DataFrame(list_data_2d, columns=['나이', '성별', '지역'], index=['상우', '지원', '민기', '정민', '수림'])

#딕셔너리로 dataFrame 만들기
dict_data = {'나이':[23,21,25,27,24], '성별':['남','여','남','여','여'], '지역':['부산', '서울', '광주', '대전', '광주']}
df = pd.DataFrame(dict_data, index=['상우', '지원', '민기', '정민', '수림'])

#데이터프레임 열선택
df_row = df[['나이', '성별']]
#데이터프레임 행선택
df_col = df.loc[['상우']]
df_col = df.iloc[[2]]
df_cols = df.loc[['상우', '민기']]
df_col = df.나이

#원소선택
test_Ddata = {
    '이름': ['준선','동훈','수찬','승호','경석'],
    '국어':[85, 88, 90, 50, 70],
    '수학':[57, 90, 100, 78, 66],
    '영어':[85, 89, 67, 98, 90],
    '과학':[93, 79, 92, 50, 70],
    '체육':[94, 80, 99, 69, 100],
}
df = pd.DataFrame(test_Ddata)
#이름으로 인덱스 선택
df.set_index('이름', inplace=True)
#print(df.loc[['동훈'],['영어','체육']])
#print(df.iloc[[0,1],[0,1,2,3]])

#행, 열 추가하기
df['코딩'] = 90
df['html'] = [100, 20, 30, 40, 50]
df.loc['승효'] = [ 100, 100 ,100, 100, 100, 100, 100]

#데이터 프레임 reshaping
test_data = {
    '상호명' : ['상우네', '현정이네', '문영이네', '동엽이네', '우제네'],
    '사과' : [1000, 900, 1200, 500, 800],
    '배' : [1100, 900, 1000, 1100, 2000],
    '딸기' : [800, 900, 600, 900, 1200],
    '포도' : [1500, 900, 1000, 800, 900]
}
df = pd.DataFrame(test_data)

#setindex
df.set_index(['상호명'], inplace=True)

#reindex
test_data = {
    '상호명' : ['상우네', '현정이네', '문영이네', '동엽이네', '우제네'],
    '사과' : [1000, 900, 1200, 500, 800],
    '배' : [1100, 900, 1000, 1100, 2000],
    '딸기' : [800, 900, 600, 900, 1200],
    '포도' : [1500, 900, 1000, 800, 900]
}
new_index = [0,1,2,3,4, 5]
df = pd.DataFrame(test_data, index = [4, 2, 1, 0, 3])
new_df = df.reindex(new_index)
new_df2 = df.reindex(new_index, fill_value=200)

#resetIndex
test_data = {
    '상호명' : ['상우네', '현정이네', '문영이네', '동엽이네', '우제네'],
    '사과' : [1000, 900, 1200, 500, 800],
    '배' : [1100, 900, 1000, 1100, 2000],
    '딸기' : [800, 900, 600, 900, 1200],
    '포도' : [1500, 900, 1000, 800, 900]
}
df = pd.DataFrame(test_data)
df.set_index('상호명', inplace=True)

rs = df.reset_index()
rs = rs.sort_values(by='딸기', ascending=False)


rs = rs.drop(2)

df = pd.read_csv('testData.csv')

test_data = {
    '상호명' : ['상우네', '현정이네', '문영이네', '동엽이네', '우제네'],
    '사과' : [1000, 900, 1200, 500, 800],
    '배' : [1100, 900, 1000, 1100, 2000],
    '딸기' : [800, 900, 600, 900, 1200],
    '포도' : [1500, 900, 1000, 800, 900]
}
df = pd.DataFrame(test_data)
df.set_index('상호명', inplace=True)

df.to_csv('./df_to_csv.csv')

df = pd.read_json('json_to_df.json')
df.to_json('df_to_json')

dict_data = {'c0' : [1,2,3], 'c1' : [4,5,6], 'c2': [7,8,9]}
df = pd.DataFrame(dict_data)

add = df + 10
sub = df - 10
mul = df * 10
div = df / 10

data_1 = {'c0' : [1,2,3], 'c1' : [4,5,6], 'c2': [7,8,9]}
data_2 = {'c0' : [10,11,12], 'c1':[13,14,15], 'c2':[16,17,np.nan]}
df_1 = pd.DataFrame(data_1)
df_2 = pd.DataFrame(data_2)
#pandas 간단한 통계 메소드
#난수생성
data_1 = []
data_2 = []
data_3 = []

for i in range(0,10):
    data_1.append(uniform(0,1))
for i in range(0,10):
    data_2.append(uniform(0,2))
for i in range(0,10):
    data_3.append(uniform(0,2))

#DataFrame 생성
dict_data = {'first' : data_1, 'second' : data_2}
index_data = ['zero','1st','2nd','3rd','4th','5th','6th','7th','8th','9th']

df = pd.DataFrame(dict_data, index = index_data)

#전체평균
mean_val = df.mean()
#first평균
first_mean = df['first'].mean()
#second평균
second_mean = df['second'].mean()

#중간값

#전체중간값
median_val = df.median()
#first중간값
first_median = df['first'].median()
#second중간값
second_median = df['second'].median()

#최댓값
max_val = df.max()
first_max = df['first'].max()
second_max = df['second'].max()

#최솟값
min_val = df.min()
first_min = df['first'].min()
second_min = df['second'].min()

#표쥰편차
std_val = df.std()
first_std = df['first'].std()
second_std = df['second'].std()

#상관계수
#DataFrame 생성
dict_data = {'first' : data_1, 'second' : data_2, 'third' : data_3}
index_data = ['zero','1st','2nd','3rd','4th','5th','6th','7th','8th','9th']

ndf = pd.DataFrame(dict_data, index=index_data)

#전체 상관계수
corr_val = ndf.corr()

first_third_corr = ndf[['first', 'third']].corr()

#판다스 활용기초
df = sns.load_dataset('titanic')
#df.tail()

#누락데이터 확인
#info method
#df.info()

#valueCount Method
#nan_df = df['deck'].value_counts(dropna=False)

#isnull()은 원소가 Null 데이터나 NaN 데이터일 경우 해당 원소를 True로 반환하며 유효 데이터일
#경우 False를 반환합니다 notnull은 반대
#print(df.head().isnull())

#다음과 같이 isnull() 과 sum() 을 이용하면 한 번에 누락 데이터의 개수를 파악할 수 있습니다.
#print(df.isnull().sum(axis=0))

#누락데이터 제거
ndf = df.dropna(axis=0, thresh=445)

ndf2 = ndf.dropna(subset=['age'], how='any', axis=0)
#print(ndf2.isnull().sum(axis=0))
#print(ndf2.notnull().sum(axis=0))
#데이터 중 age 열에 177개의 누락 데이터가 있었습니다. dropna() 메소드에서 how 옵션을 이용
#하여 age 열에서 누락 데이터를 가진 행들을 제거해보도록 하겠습니다. how=any 옵션을 사용하면
#NaN 데이터가 존재하는 모든 행을 제거하게 됩니다.

#누락데이터 채우기

#누락 데이터 445개 이상인 열 제거
df.dropna(axis=1, thresh=445, inplace=True)

#age열의 누락 데이터를 평균값으로 채우기
age_median = df['age'].median(axis=0)
#print(df['age'].isnull().sum(axis=0))
df['age'].fillna(age_median, inplace=True)
#print(df['age'].isnull().sum(axis=0))

data = {
    'c0' : ['a', 'a','c','d','e','f','c'],
    'c1' : [1,1,2,3,4,5,2],
    'c2' : [1,1,2,3,4,5,2],
    'c3' : ['a', 'a','c','d','e','f','c']
}
df = pd.DataFrame(data)

#중복된 레이블 판별
duplicated_df = df.duplicated()

df.drop_duplicates(inplace=True)

#시계열 객체 변환

corona_df = pd.read_csv('PatientRoute.csv')

corona_df.head()

corona_df['new_date'] = pd.to_datetime(corona_df['date'])

# to_period()를 이용하여 Timstamp 객체를 일정 기간을 나타내는 Period 객체로 바꿀 수 있습니
# 다. freq 옵션을 사용하여 반복되는 기간을 설정할 수 있습니다.
# • freq = 'D' : 1일
# • freq = 'M' : 1달
# • freq = 'A' : 1년
data = corona_df['new_date'].dt
freq_d = data.to_period(freq='D')
freq_m = data.to_period(freq='M')
freq_a = data.to_period(freq='A')

corona_df['Year'] = corona_df['new_date'].dt.year
corona_df['Month'] = corona_df['new_date'].dt.month
corona_df['Day'] = corona_df['new_date'].dt.day

corona_df.set_index('new_date', inplace=True)
corona_df_ym = corona_df.loc['2020-02']
#print(corona_df_ym)

#날짜벙위 슬라이싱
corona_df_ymd_range = corona_df.loc['2020-02-22' : '2020-02-23']
print(corona_df_ymd_range)