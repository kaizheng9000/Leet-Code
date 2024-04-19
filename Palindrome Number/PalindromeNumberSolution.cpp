#include <iostream>
#include <algorithm>

// Converts to a string and compares the reversed version with original
bool isPalindrome(int x)
{
    std::string stringOfInt = std::to_string(x);
    std::string copy = stringOfInt;
    
    std::reverse(copy.begin(), copy.end());

    if(copy == stringOfInt)
    {
        return true;
    }

    return false;
}

// Rebuilds the number in reverse with math
bool isPalindromeNoStringConversion(int x)
{
    if(x < 0)
    {
        return false;
    }

    int og = x;
    int reversedNum = 0;

    while(x > 0)
    {
        reversedNum = reversedNum * 10 + x % 10;
        x /= 10;
    }

    if(og == reversedNum)
    {
        return true;
    }

    return false;
}


int main()
{
    int x = 101;
    std::cout << "Is " << x << " a palindrome?" << std::endl;
    std::cout << std::boolalpha;
    std::cout << isPalindromeNoStringConversion(x) << "!";
    return 0;
}