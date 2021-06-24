import matplotlib.pyplot as plt
import numpy as np
import wave
import matplotlib.image as mpimg

# 생성해보기
#plt.plot([0,1,2], [4,10,6])
#plt.show()

# figure() 함수 생성
# 피규어라는 공간을 생성하고
# add_subplot(x, y, a)은 x행 y열의 a번째 subplot을 추가합니다. ax1는 2행 1열의 첫 번째
# subplot, ax2는 2행 1열의 두 번째 subplot이 됩니다
# 세로 정렬
# fig = plt.figure()
# ex1 = fig.add_subplot(2,1,1)
# ex2 = fig.add_subplot(2,1,2)
# 가로정렬
# fig = plt.figure()
# ax1 = fig.add_subplot(1,2,1)
# ax2 = fig.add_subplot(1,2,2)
# plt.show()

#subplot
#subplot은 위에서 보았듯이 하나의 figure에서 여러 개의 그래프를 만들 수 있습니다.

fig = plt.figure()
# ax1 = fig.add_subplot(2,1,1)
# ax1.plot([1,2,3], [4,10,6])
# ax2 = fig.add_subplot(2,1,2)
# ax2.plot([1,10,100], [1, 100, 10])
#
# plt.show()

#subplots
#subplots()는 figure를 따로 만들고 add_subplot으로 axes를 추가할 필요 없이 간결한 코드로 여
#러 그래프를 그릴 수 있습니다

# fig, ax = plt.subplots(2,1)
#한 줄의 코드로 2행 1열의 axes를 만들었습니다. subplots()는 바로 인덱스로 접근이 가능합니다.
# ax[0].plot([1,2,3], [4,10,6])
# ax[1].plot([1,10,100], [1, 100, 10])
# plt.show()

# 2 * 2개의 그래프를 만들고 싶은 경우 ax[행, 열]에 각각 들어갈 내용을 지정해 주면 한번에 여러 그
# 래프를 그릴 수 있습니다

# fig, ax = plt.subplots(2,2)
# ax[0, 0].plot([1,2,3], [4,10,6])
# ax[0, 1].plot([1,10,100], [1, 100, 10])
# ax[1, 0].plot([4,10,6], [1,2,3])
# ax[1, 1].plot([1,100,10], [1, 10, 100])
# plt.show()

# numpy & matplotlib
# numpy 함수 중 linspace()로 0부터 15까지 1000개의 간격으로 1차원 리스트를 만들고
# subplots()로 2행 1열의 두 그래프를 만들었습니다. 그 후 numpy의 cosine과 sine함수를 사용하
# 여 두 그래프를 그렸습니다. 이렇게 numpy뿐만 아니라 pandas나 다양한 라이브러리와 함께 사용
# 하여 원하는 데이터들을 쉽게 시각화 시킬 수 있습니다
# x = np.linspace(0, 15, 1000)
# fig, ax = plt.subplots(2,1)
# ax[0].plot(x, np.cos(x))
# ax[1].plot(x, np.sin(x))
# plt.show()

#한 그래프에서 여러 선 나타내기
# 알아보기 쉽게 속성 추가하기
#  title() : 그래프 위에 제목을 추가합니다
# • xlabel() : x축 아래에 축의 이름을 추가합니다
# • ylabel() : y축 왼쪽에 축의 이름을 추가합니다
# • legend() : 그래프에 범례를 추가합니다.
# 범례는 기본적으로 최대한 그래프와 겹치지 않는 위치에 만들어줍니다. 직접 설정하고 싶다면 범례
# 를 추가하는 함수에 loc이라는 인자를 추가하고 값을 넣어주면 됩니다.
# ex) plt.lejent(loc = 'upper right')
# x = np.linspace(0, 15, 1000)
# plt.plot(x, np.cos(x),color = 'red', label = 'cos')
# plt.plot(x, np.sin(x),color = 'blue', label = 'sin')
# plt.title('Cosine & Sine')
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.legend()
# plt.show()

#scatter plot(산점도)
#scatter()로 산점도 그래프를 나타낼 수 있으며, plot()과는 다르게 데이터들을 점으로만 나타나게
# 됩니다.
# x = np.arange(0,10,1)
# plt.scatter(x, x+1)
# plt.title('scatter flot')
# plt.show()

#bar chart(막대그래프)
# Bar Chart는 막대그래프로 선 그래프와 비슷하게 변화 추이를 보거나 두 개 이상의 값을 비교할 때
# 사용합니다. Bar Chart는 bar() 함수를 이용하여 그릴 수 있습니다
# data = [10,13,20,16]
# x = range(len(data))
# plt.bar(x,data)
# plt.title('bar chart')
# plt.show()

#error bar chart
# Error Bar Chart는 오차 막대그래프로 데이터의 편차를 시각화하기 위한 그래프입니다. Error Bar
# Chart는 errorbar() 함수로 그릴 수 있습니다
# yerr의 값은 위, 아래로 대칭인 오차를 의미하며, 하나로 모든 데이터에 균일하게 설정할 수도 있고,
# N개의 데이터에 대한 오차를 각각 다르게 설정할 수도 있습니다. 또한 비대칭으로 편차를 표시하기
# 위해서는 아래와 같이 먼저 아래 방향 편차를 작성하고, 그 다음 위 방향 편차를 작성해주면 됩니다.
# x = [1,2,3,4,5]
# y = [10, 20, 30, 40, 50]
# year = [1, 3, 5, 5, 10]
# plt.errorbar(x, y, year)
# plt.title('error bar chart')
# plt.show()

#histogram
# 히스토그램은 도수분포표를 그래프로 나타낸 것으로 연속된 자료의 분포를 보기 위해 사용됩니다.
# 히스토그램은 hist() 함수를 사용하여 그릴 수 있습니다
# x = np.random.normal(0, 1, size=5000)
# plt.hist(x)
# plt.title('historygram')
# plt.xlabel('x가 속하는구간')
# plt.ylabel('구간에 속하는 x 개수')

#오디파일 파형 출력
# wav = wave.open('audio.wav', 'r')
# signal = wav.readframes(-1)
# signal = np.frombuffer(signal,np.int16)
# plt.plot(signal)
# plt.show()

#이미지 파일열기
img = mpimg.imread('lena.png')
plt.imshow(img)
plt.show()