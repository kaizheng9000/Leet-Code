

def customSortString(order, s):
    letter_count = {}
    for c in s:
        if c in letter_count:
            letter_count[c] += 1
        else:
            letter_count[c] = 1

    prefix = ""
    index = 0
    while index < len(order) and letter_count:
        char = order[index]
        if char in letter_count:
            prefix += char
            letter_count[char] -= 1
            if letter_count[char] == 0:
                del letter_count[char]
                index += 1
        else:
            index += 1

    postfix = ""
    for key, value in letter_count.items():
        postfix += key * value

    result = prefix + postfix
    return result


exampleOrder = "cba"
exampleString = "abcd"

exampleOrder2 = "bcafg"
exampleString2 = "abcd"

print(customSortString(exampleOrder, exampleString))
print(customSortString(exampleOrder2, exampleString2))