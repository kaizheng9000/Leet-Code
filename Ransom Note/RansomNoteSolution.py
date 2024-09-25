ransom_note1 = "a"
magazine1 = "b"

ransom_note2 = "aa"
magazine2 = "ab"

ransom_note3 = "aa"
magazine3 = "aab"

def decode(ransom_note, magazine):

    letter_count = {}

    for letter in magazine:
        if not letter in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

    for character in ransom_note:
        if character in letter_count and letter_count[character] > 0:
            letter_count[character] -= 1
        else:
            return False

    return True


print(decode(ransom_note1, magazine1))
print(decode(ransom_note2, magazine2))
print(decode(ransom_note3, magazine3))