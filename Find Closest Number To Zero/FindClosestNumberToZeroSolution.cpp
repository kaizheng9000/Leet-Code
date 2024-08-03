#include <iostream>
#include <vector>
#include <cstdlib>
#include <unordered_map>
#include <algorithm>

int solve(std::vector<int> nums)
{
    int closest = nums[0];
    for(int i = 1; i < nums.size(); i++)
    {
        if(std::abs(nums[i]) < std::abs(closest))
        {
            closest = nums[i];
        }
    }

    if(closest < 0)
    {
        int find = std::count(nums.begin(), nums.end(), std::abs(closest));
        if(find > 0)
        {
            closest = std::abs(closest);
        }
    }
    
    return closest;
}





int main()
{
    std::vector<int> list {-4, -10, 4, -5};
    std::cout << solve(list);
    return 0;
}