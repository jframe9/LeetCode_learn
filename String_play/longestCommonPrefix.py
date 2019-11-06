'''
问题描述：
        编写一个函数来查找字符串数组中的最长公共前缀。
        如果不存在公共前缀，返回空字符串 ""。

'''

strs = ["fllower", "flow", "fwight"]
# min(str) 返回字符串中最小的字母，列表中为返回最大的字符串
print(min(strs))
# strs = ["c", "c"]
# 判断两个字符串的相同部分
def compareStrs(str1, str2):
    result_str = ''
    if len(str1) >= len(str2):
        for i, s in enumerate(str2):
            if s == str1[i]:
                result_str = result_str + s
            else:
                break
    else:
        for i, s in enumerate(str1):
            if s == str2[i]:
                result_str = result_str + s
            else:
                break
    return result_str

# l = compareStrs('abcde', 'abddec')
# print(l)
def getLongest(strs):
    # if len(strs) == 2:
    #     result_str = compareStrs(strs[0], strs[1])
    #     return result_str
    # else:
    #     result_str = compareStrs(strs[0], strs[1])
    #     for i in range(2, len(strs))
    #         result = compareStrs(result_str, strs[i])
    #     return result
    result = ''
    if len(strs) <= 1:
        return ''.join(strs)
    if len(strs) == 2:
        resules = compareStrs(strs[0], strs[1])
        return resules
    else:
        for i in range(1, len(strs)):
            if i == 1:
                result_str = compareStrs(strs[0], strs[1])
            else:
                result = compareStrs(strs[i], result_str)
        return result
l = getLongest(strs)
print(l)

def yangli(strs):
    if not strs: return ""
    s1 = min(strs)
    s2 = max(strs)
    for i, x in enumerate(s1):
        if x != s2[i]:
            return s2[:i]
    return s1
s = yangli(strs)
print(s)