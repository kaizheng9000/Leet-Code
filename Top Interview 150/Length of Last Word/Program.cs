

public class Solution
{
    public static int Main(string[] args)
    {
        string s = "luffy is still joyboy";

        Console.WriteLine(GetLastWordLength(s));

        return 0;
    }

    public static int GetLastWordLength(string sequence)
    {
        string trimmed = sequence.TrimEnd(' ');

        string[] split = trimmed.Split(' ');

        return split[split.Length - 1].Length;
    }
}