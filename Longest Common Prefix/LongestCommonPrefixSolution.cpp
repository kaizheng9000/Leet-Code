#include <iostream>
#include <vector>
#include <algorithm>
#include <format>

std::string findLongestCommonPrefix(std::vector<std::string> strs)
{
    if(strs.empty())
    {
        return "";
    }

    sort(strs.begin(), strs.end());
    std::string lcp = "";
    std::string firstWord = strs[0];
    std::string lastWord = strs[strs.size() - 1];

    for(int i = 0; i < std::min(firstWord.size(), lastWord.size()); i++)
    {
        if(firstWord[i] != lastWord[i])
        {
            return lcp;
        }

        lcp += firstWord[i];
    }

    return lcp;
}

// There's gotta be a better way to write tests for this
int tests()
{
    std::vector<std::string> example1 {"flower","flow","flight"};
    std::vector<std::string> example2 {"dog","racecar","car"};
    std::vector<std::string> example3 {"bananas", "bantang", "band"};

    std::string ans1 = "fl";
    std::string ans2 = "";
    std::string ans3 = "ban";

    if(findLongestCommonPrefix(example1) != ans1)
    {
        return 1;
    }

    if(findLongestCommonPrefix(example2) != ans2)
    {
        return 2;
    }
    
    if(findLongestCommonPrefix(example3) != ans3)
    {
        return 3;
    }

    return 0;
}

int main()
{
    int result = tests();

    if(result == 0)
    {
        std::cout << "Tests Passed!";
    }
    else
    {
        std::cout << "Test number " << result << " did not pass!";
    }


    return 0;
}