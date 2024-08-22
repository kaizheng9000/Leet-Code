using System;

namespace RomanToIntegerSolution;

public class RomanToIntegerSolution
{

    public static void Main(string[] args)
    {
        string roman = "XVII";
        Console.WriteLine(Solve(roman));
    }

    private static int Solve(string romanNumeral)
    {
        Dictionary<char, int> mapConversion = new Dictionary<char, int>();
        int result = 0;

        // Add in the Roman numerals and their corresponding values
        mapConversion.Add('I', 1);
        mapConversion.Add('V', 5);
        mapConversion.Add('X', 10);
        mapConversion.Add('L', 50);
        mapConversion.Add('C', 100);
        mapConversion.Add('D', 500);
        mapConversion.Add('M', 1000);

        for(int i = 0; i < romanNumeral.Length; i++)
        {
            if(i < romanNumeral.Length - 1 && mapConversion[romanNumeral[i]] < mapConversion[romanNumeral[i+1]])
            {
                result -= mapConversion[romanNumeral[i]];
            }
            else
            {
                result += mapConversion[romanNumeral[i]];
            }
        }

        return result;
    }
}
