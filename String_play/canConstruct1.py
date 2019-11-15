

def lfd(ransomNote, magazine):
    magazine_list = list(magazine)
    i = 0
    if ransomNote == '':
        return True
    for item in ransomNote:
        if item in magazine_list:
            magazine_list.remove(item)
            i = i+1
            if i == len(ransomNote):
                return True
        else:
            return False

print(lfd('', 'a'))


