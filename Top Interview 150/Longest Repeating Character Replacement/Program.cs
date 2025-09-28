
public class Solution()
{
    public static int Main(string[] args)
    {
        string example = "AAABABB";
        int rep = 1;

        Console.WriteLine(Solve(example, rep));
        return 0;
    }


    public static int Solve(string s, int k)
    {
        Dictionary<char, int> freq = new();

        int res = 0;
        int maxFreq = 0;

        int l = 0;

        for (int r = 0; r < s.Length; r++)
        {
            char cur = s[r];
            if (freq.ContainsKey(cur))
            {
                freq[cur] += 1;
            }
            else
            {
                freq.Add(cur, 1);
            }
            maxFreq = Math.Max(maxFreq, freq[cur]);

            while (((r - l + 1) - maxFreq) > k)
            {
                freq[s[l]] -= 1;
                l += 1;
            }

            res = Math.Max(res, r - l + 1);
        }

        return res;
    }
}
