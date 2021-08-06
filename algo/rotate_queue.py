from collections import deque
'''
    Function
        - make_dequeue(number) : number에 들어간 숫자만큼의 deque를 리턴해줌
        - pick_number(number, dequeue_list, total_moves) : dequeue_list에서 number를 찾아 뽑고 그 상태의 리스트를 리턴 
'''

def make_dequeue(number):
    deque_list = deque([i+1 for i in range(number)])
    return deque_list

def pick_number(number, dequeue_list, total_moves):
    return_list = []
    if number not in dequeue_list:
        if len(dequeue_list) > 1:
            print('리스트 안에 숫자가 없네요. 다음 숫자로 넘어갑니다.')
            return dequeue_list
        else:
            print('리스트 안에 숫자가 없네요. 종료합니다.')
            return dequeue_list
    else:
        #인덱스 추출
        n_idx = dequeue_list.index(number)
        # deque_list의 중앙을 중심으로 left로 옮길지 right로 옮길지 결정

        # 배열 옮기는 조건은 같음
        slice_left_list = list(dequeue_list)[:n_idx]
        slice_right_list = list(dequeue_list)[n_idx:]
        return_list = deque(slice_right_list + slice_left_list)
        return_list.popleft()
        if n_idx <= round(len(dequeue_list) / 2):
            # left로 옮기기
            total_moves += n_idx
        else:
            total_moves += len(dequeue_list) - n_idx
    return return_list, total_moves

number, pick_size = map(int, input().split())

#dequeue_list 생성
dequeue_list = make_dequeue(number)

# 전체이동수
total_moves = 0
# 두번째 입력으로 뽑을 숫자 리스트 생성
pick_numbers = list(map(int, input().split()))

# 넣기로한 사이즈와 입력값이 다르면 에러 발생
if len(pick_numbers) != pick_size:
    raise IndexError('리스트 사이즈 안맞다 ㅋ')

#아니면 루프돌면서 번호 뽑기
for i in range(len(pick_numbers)):
    dequeue_list, total_moves = pick_number(pick_numbers[i], dequeue_list, total_moves)

print(total_moves)



