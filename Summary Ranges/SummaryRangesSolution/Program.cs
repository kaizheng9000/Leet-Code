namespace SummaryRangesSolution;

public class SummaryRangesSolutionFactory
{
    public static void Main(String[] args)
    {

        int[] input = {0,1,2,4,5,7};

        foreach(string smallRange in FindSmallestSortedRange(input))
        {
            Console.WriteLine(smallRange);
        }
    }

    private static List<string> FindSmallestSortedRange(int[] nums)
    {
        List<string> result = [];

        // Must check for empty
        if (nums.Length == 0)
        {
            return result;
        }

        // Initial values
        int prev = nums[0];
        int startingValue = nums[0];
        int endingValue = nums[0];

        for(int i = 1; i < nums.Length; i++) 
        {
            // Compare the current value and see if it's the next value in the sequence, adjust variables accordingly
            if(nums[i] == prev + 1)
            {
                prev = endingValue = nums[i];
            }
            else
            {
                if(startingValue != endingValue)
                {
                    string range = startingValue + "->" + endingValue;
                    result.Add(range);
                }
                else
                {
                    result.Add(startingValue.ToString());
                }

                prev = startingValue = endingValue = nums[i];
            }
        }

        // Handles the entry for the final range
        if(startingValue != endingValue)
        {
            string range = startingValue + "->" + endingValue;
            result.Add(range);
        }
        else
        {
            result.Add(startingValue.ToString());
        }


        return result;
    }
}