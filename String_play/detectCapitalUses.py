def detectCapitalUse(word):
    if word.isupper():
        return True
    if word.istitle():
        return True
    if word.islower():
        return True
    return False

ls = detectCapitalUse('RDF')
print(ls)

word = 'aaa'

print(word.istitle())

exam = [1, 2, 3, 4, 4, 3]

print(exam.index(4))