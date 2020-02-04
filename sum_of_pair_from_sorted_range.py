list1 = [1,2,4,4]
list2 = [1,2,4,4,5,9,10,12,15,16,17,19,22,25,26,27,28,29,30]
sum_pair = 8

def find_pair_for_sum(list,sum):
    list_length = len(list)
    print('len = ' , list_length)
    low = 0
    hi = list_length - 1
    print(hi)
    while low < hi :
        calc = list[low] + list[hi]
        print(list, calc, low, hi)
        if calc == sum:
            print ('solution found',list[low], "|",low, ',', list[hi], "|",hi)
            quit()
        elif calc > sum:
            hi = hi - 1
        elif calc < sum:
            low = low + 1
        else:
            print('No matched pairs')


find_pair_for_sum(list2,33)