
example1 = "nlaebolko"
example2 = "loonbalxballpoon"
example3 = "leetcode"

def count_balloons(letters):
    letter_count = { "b":0, "a":0, "l":0, "o":0, "n":0}
    balloon_count = 0
    keep_spelling = True

    for letter in letters:
        if letter in letter_count:
            letter_count[letter] += 1

    while keep_spelling:
        for char in "balloon":
            if letter_count[char] < 1:
                keep_spelling = False
                break
            else:
                if char == "n":
                    balloon_count += 1
                letter_count[char] -= 1

    return balloon_count

print(count_balloons(example1))
print(count_balloons(example2))
print(count_balloons(example3))