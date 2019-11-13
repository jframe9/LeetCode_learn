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