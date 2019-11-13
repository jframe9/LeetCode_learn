

def lfd(ransomNote, magazine):
    i = 0
    for item in ransomNote:
        if item in magazine:
            i = i + 1
    if i == len(ransomNote):
        return True

    return False


