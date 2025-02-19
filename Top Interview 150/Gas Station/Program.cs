

public class Solution
{
    public static void Main(string[] args)
    {
        int[] gas = [1,2,3,4,5];
        int[] cost = [3,4,5,1,2];
;

        Solution solve = new Solution();
        Console.WriteLine(solve.CanCompleteCircuit(gas, cost));
    }

    public int CanCompleteCircuit(int[] gas, int[] cost)
    {
        if (gas.Sum() < cost.Sum())
        {
            return -1;
        }

        int currGas = 0;
        int startPos = 0;

        for(int i = 0; i < gas.Length; i++)
        {
            currGas += gas[i] - cost[i];
            if (currGas < 0)
            {
                currGas = 0;
                startPos = i + 1;
            }
        }

        return startPos;
    }
}
