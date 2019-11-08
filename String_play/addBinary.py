'''
问题描述：
    给定两个二进制字符串，返回他们的和（用二进制表示）。

    输入为非空字符串且只包含数字 1 和 0。
    输入: a = "11", b = "1"
    输出: "100"
    int(x, base=10) # x--字符串或者数字； base--进制数，默认十进制
'''

# 二进制求和
def Binary(a, b):
    a_int = int(a, 2)
    b_int = int(b, 2)
    ans = bin(a_int + b_int)
    print(ans)

Binary("11", "1")