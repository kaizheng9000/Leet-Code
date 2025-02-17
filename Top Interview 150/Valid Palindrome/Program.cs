using System.Text.RegularExpressions;

public class Solution
{
    public static int Main(string[] args)
    {
        string sequence = "1a2";

        Solution solve = new Solution();

        Console.WriteLine(solve.isPalindrome(sequence));

        return 0;
    }

    public bool isPalindrome(string s)
    {
        string cleaned = Regex.Replace(s, @"[^A-Za-z0-9]+", "");
        string lowered = cleaned.ToLower();

        int left = 0;
        int right  = lowered.Length - 1;

        while (left < right)
        {
            if (lowered[left].CompareTo(lowered[right]) != 0)
            {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
}


