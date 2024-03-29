'''
题目描述：
    给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
    说明：本题中，我们将空字符串定义为有效的回文串。

    输入: "A man, a plan, a canal: Panama"
    输出: true
    回文串定义，正读反读都是一样的。
'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        else:
            strs = ''
            for sm in s:
                if sm.isalpha() or sm.isdigit():
                    strs = strs + sm
            l = list(strs.upper())
            l.reverse()
            res = ''.join(l)
            return strs.upper() == res

def pair_str(s):
    strs = ''
    for sm in s:
        if sm.isalpha() or sm.isdigit():
            strs = strs + sm
    l = list(strs.upper())
    l.reverse()
    m = ''.join(l)
    return m == strs.upper()
l = pair_str("A man, a 1plan, a canal: P1anama")
print(l)
