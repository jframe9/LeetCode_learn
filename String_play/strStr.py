

def strs(haystack, needle):

    if needle not in haystack:
        return -1
    elif needle == '':
        return 0
    else:
        result_list = haystack.split(needle)
        return len(result_list[0])

    # sao taolu
    # return haystack.find(needle)

ls = strs('hellp', 'p')
print(ls)