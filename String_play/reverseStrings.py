'''
    执行用时 :172 ms, 在所有 python 提交中击败了94.81%的用户
    内存消耗 :18.8 MB, 在所有 python 提交中击败了31.23%的用户
    题目描述：编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

    不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
    你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
'''


ls = 'ss'
s = ['h', 'e', 'e', 'l']

def reverseString(s):
    i = 0
    j = len(s) - 1

    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s
t = reverseString(s)
print(t)