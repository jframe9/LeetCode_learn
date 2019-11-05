'''
 问题描述：
        给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
        如果不存在最后一个单词，请返回 0 。
        说明：一个单词是指由字母组成，但不包含任何空格的字符串。
        输入: "Hello World"
        输出: 5
'''


strs = "a"

def get_last_str(strs):
    # 需要去除字符串两端的空格
    split_str_list = strs.strip().split(' ')
    print(split_str_list)
    if split_str_list[-1] == '':
        return 0
    return len(split_str_list[-1])
print(get_last_str(strs))