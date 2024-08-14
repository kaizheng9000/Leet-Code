#include <string>
#include <iostream>
#include <vector>
#include <sstream>


std::string solve(std::string word1, std::string word2)
{
    std::ostringstream result;
    
    int min = std::min(word1.length(), word2.length());

    for(int i = 0; i < min; i++)
    {
        result << word1[i] << word2[i];
    }

    if(min == word1.length())
    {
        result << word2.substr(min);
    }
    else
    {
        result << word1.substr(min);
    }

    return result.str();
}


int main()
{
    std::string word = "abc";
    std::string word2 = "pqrstuv";
    std::cout << solve(word, word2);
    return 0;
}