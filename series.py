def count_left_same_number(mylist):

    first = mylist[0]
    same_list = []
    for num in mylist:
        if num != first:
            break
        same_list.append(num)
    return same_list

def subtract_list(first, second):
    l1 = len(first)
    l2 = len(second)
    return second[l1:l2]

def generate_new_list(the_list):
    new_list = []
    while len(the_list) > 0:
        tmp = count_left_same_number(the_list)
        the_list = subtract_list(tmp, the_list)
        new_list.append(len(tmp))
        new_list.append(tmp[0])
    return new_list

line = int(input("输入数字："))

count = 0
series = [1]

print(series[0])
while count < line:
    series = generate_new_list(series)
    for num in series:
        print(num, end='')
    print('')
    count = count + 1
