

public class Solution
{
    public static void Main(string[] args)
    {
        int[] nums = [1, 0, -1, 0, -2, 2];
        int target = 0;

        foreach (List<int> item in solve(nums, target))
        {
            Console.WriteLine("[{0}]", string.Join(", ", item));
        }
    }

    public static List<List<int>> solve(int[] nums, int target)
    {
        List<List<int>> result = new List<List<int>>();

        Array.Sort(nums);

        // Sliding Window problem?
        left = 0;
        right = 3;




        return result;
    }
}
