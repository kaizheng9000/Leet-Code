namespace ProductOfArrayExceptSelfSolution;

public class ProductOfArrayExceptSelfSolution
{
    public static void Main(string[] args)
    {
        int[] values = {1,2,3,4};

        Console.WriteLine("-------------USING SPACE O(n) METHOD-----------------");
        foreach(int num in CalculateProducts(values))
        {
            Console.WriteLine(num);
        }

        Console.WriteLine("-------------USING SPACE O(1) METHOD-----------------");
        foreach(int num in CalculateProductsSpaceEfficient(values))
        {
            Console.WriteLine(num);
        }
    }

    private static int[] CalculateProducts(int[] nums)
    {
        int[] result = new int[nums.Length];
        int[] prefix = new int[nums.Length];
        int[] suffix = new int[nums.Length];

        // Initialize prefix and suffix arrays
        prefix[0] = 1;
        suffix[nums.Length - 1] = 1;

        // Populate the prefix and suffix arrays to contain the products of the left and right of nums[i] 
        for(int i = 1; i < nums.Length; i++)
        {
            prefix[i] = prefix[i - 1] * nums[i - 1];
        }

        for(int i = nums.Length - 2; i >= 0; i--)
        {
            suffix[i] = suffix[i + 1] * nums[i + 1];
        }

        // Multiply the indicies from the two arrays to get the final result
        for(int i = 0; i < nums.Length; i++)
        {
            result[i] = prefix[i] * suffix[i];
        }

        return result;
    }

    private static int[] CalculateProductsSpaceEfficient(int[] nums)
    {
        // Initialize array for multiplication
        int[] result = new int[nums.Length];
        Array.Fill<int>(result, 1);

        // Calculate the products for the prefix of all elements
        int currVal = 1;
        for(int i = 0; i < nums.Length; i++)
        {
            result[i] *= currVal;
            currVal *= nums[i];
        }

        // Calculate the products for the suffix of all elements
        currVal = 1;
        for(int i = nums.Length - 1; i >= 0; i--)
        {
            result[i] *= currVal;
            currVal *= nums[i];
        }

        return result;
    }
}
