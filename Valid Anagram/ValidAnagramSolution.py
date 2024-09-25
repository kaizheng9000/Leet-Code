
match1 = "anagram"
mixed1 = "nagaram"

match2 = "rat"
mixed2 = "car"

def is_anagram(to_match, letters):
    if len(to_match) != len(letters):
        return False

    letter_count = {}

    for letter in letters:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

    for char in to_match:
        if char in letter_count and letter_count[char] > 0:
            letter_count[char] -= 1
        else:
            return False

    return True

print(is_anagram(match1, mixed1))
print(is_anagram(match2, mixed2))