def insertion_sort(num_list):
    # 각각의 요소를 이미 정렬된 앞 배열부분과 비교하여 삽입한다.
    for i in range(1, len(num_list)):
        print('insertion')
        if num_list[i] < num_list[i-1]:
            index = i
            while index > 0:
                if num_list[index] < num_list[index-1]:
                    num_list[index], num_list[index-1] = num_list[index-1], num_list[index]
                    index -= 1
                    print('insertion')
                else:
                    break
    return num_list

def selection_sort(num_list):
    for i in range(len(num_list) - 1):
        print('selection')
        min_index = i
        for j in range(i + 1, len(num_list)):
            if num_list[j] < num_list[min_index]:
                print('selection')
                min_index = j
        num_list[i], num_list[min_index] = num_list[min_index], num_list[i]
    return num_list

def bubble_sort(num_list):
    for i in range(len(num_list)):
        for j in range(i, len(num_list)):
            print('bubble')
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    return num_list


# n = int(input())

num_list = [1,2,5,4,3]

# for _ in range(n):
#     num = int(input())
#     num_list.append(num)


insertion_sorted_list = insertion_sort(num_list)
print(" ".join(map(str, insertion_sorted_list)))

bubble_sorted_list = bubble_sort(num_list)
print(" ".join(map(str, bubble_sorted_list)))

selection_sorted_list = selection_sort(num_list)
print(" ".join(map(str, selection_sorted_list)))

