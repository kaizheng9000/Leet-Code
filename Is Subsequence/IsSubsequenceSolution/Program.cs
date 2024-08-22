
namespace IsSubsequenceSolution;

public class IsSubsequenceSolution
{
    public static void Main(string[] args)
    {
        string sequence = "abc";
        string sub = "b";

        Console.WriteLine(Solve(sub, sequence));
    }

    private static bool Solve(string s, string t)
    {
        if(String.IsNullOrEmpty(s))
        {
            return true;
        }

        int matchCounter = 0;
        foreach(char letter in t)
        {
            if(matchCounter != s.Length && s[matchCounter].Equals(letter))
            {
                matchCounter++;
            }
        }
        return matchCounter == s.Length;
    }
    

}