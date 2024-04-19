#include <iostream>
#include <vector>

int runSol(std::vector<int> prices)
{
    int buyPrice = prices[0];
    int maxProfit = 0;

    for(int i = 1; i < prices.size(); i++)
    {
        int currPrice = prices[i];
        if(currPrice < buyPrice)
        {
            buyPrice = currPrice;
        }
        else if(currPrice - buyPrice > maxProfit)
        {
            maxProfit = currPrice - buyPrice;
        }
    }

    return maxProfit > 0 ? maxProfit : 0;
}


int main()
{
    std::vector<int> examplePrices {7,15,3,18,5};
    std::cout << runSol(examplePrices);
    return 0;
}