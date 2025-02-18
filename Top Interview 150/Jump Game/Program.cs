public class Solution
{
    public static void Main(string[] args)
    {
        int[] example = [2,3,1,1,4];

        Solution solve = new Solution();
        Console.WriteLine(solve.CanJump(example));
    }

    public bool CanJump(int[] nums)
    {
        int jumpDistance = 0;

        for (int i = 0; i < nums.Length; i++)
        {
            if (jumpDistance < 0)
            {
                return false;
            }
            else if (nums[i] > jumpDistance)
            {
                jumpDistance = nums[i];
            }

            jumpDistance--;
        }

        return true;
    }
}