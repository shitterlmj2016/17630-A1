test_list = [1, 1,0,2,2]

num = 4


def swap(list, a, b):
    list[a], list[b] = list[b], list[a]


def find_zero(list):
    for i in range(len(list)):
        if list[i] == 0:
            return i
    return 0


def do_job(list, num):
    # start
    half=int(num/2)
    zero_index = find_zero(list)
    swap(list, zero_index, zero_index - 1)  # s1
    print(list)
    for i in range (half):
        swap(list,zero_index+i+1,zero_index+i-1)
        print(list)
        swap(list,zero_index+i+1,zero_index+i)
        print(list)

    # Move 2 two the right
    if list[0]==2 and list[int(num/2)]==0:
        print("Now return")
        return True
    swap_cont = int(num / 2 - 2)
    for i in range(int(num / 2)):
        swap(list, zero_index + swap_cont - i, zero_index + swap_cont + 1 - i)
        print(list)
    return False




print(test_list)
while True:
        if do_job(test_list, num):
            break
