#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

int main()
{
    const int target = 9;
    const vector<int> nums{2,7,11,15};
    
    unordered_map<int, int> numTracker;

    for (int index = 0; index < nums.size(); ++index)
    {
        int diff = target - nums[index];
        if(numTracker.count(diff))
        {
            cout << "The indicies are " << numTracker[diff] << " and " << index << endl;
        }
        numTracker[nums[index]] = index;
    }

    cout << "Finished!";
    
    return 0;
}