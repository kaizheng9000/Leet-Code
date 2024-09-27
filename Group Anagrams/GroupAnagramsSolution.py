
example = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

def groupAnagrams(strs):
    if len(strs) == 1:
        return [strs]

    result = dict()

    for string in strs:
        letter_count = [0] * 26

        # Find the occurrences of each letter and use that as a key
        for letter in string:
            letter_count[ord(letter) - ord('a')] += 1

        key = tuple(letter_count)

        if key in result:
            result[key].append(string)
        else:
            result[key] = [string]

    return result.values()

print(groupAnagrams(example))



