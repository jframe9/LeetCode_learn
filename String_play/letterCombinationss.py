'''
    执行用时 :
28 ms
, 在所有 python 提交中击败了
22.77%
的用户
内存消耗 :
11.9 MB
, 在所有 python 提交中击败了
10.31%
的用户
题目描述：
    给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

    给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

'''


def letterCombinations(digits):
    number_dict = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    # 首先获取输入
    # digits = digits.replace('1', '')
    # print(digits)
    if len(digits) == 0:
        return []
    if len(digits) < 2:
        res1 = number_dict[digits]
        res1_list = list(res1)
        return res1_list
    if len(digits) == 2:
        res2_list = []
        for i in number_dict[digits[0]]:
            for j in number_dict[digits[1]]:
                res2 = i + j
                res2_list.append(res2)
        return res2_list
    def dealStr(str1, str2):
        res3_list = []
        for i in str1:
            for j in str2:
                res3 = i + j
                res3_list.append(res3)
        return res3_list

    if len(digits) > 2:
        res = dealStr(number_dict[digits[0]], number_dict[digits[1]])
        print(res)
        for s in digits[2:]:
            res = dealStr(res, number_dict[s])
        return res




ls = letterCombinations('')
print(ls)

