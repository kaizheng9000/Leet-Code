using System;

public class ChristmasLights
{
    private readonly int lightCount;
    int nextLight = 1;
    bool forward = true;

    public ChristmasLights(int lightCount)
    {
        this.lightCount = lightCount;
    }

    public bool[] Next()
    {
        bool[] lights = new bool[lightCount];

        // Always-on lights
        lights[0] = true;
        lights[lightCount - 1] = true;

        // Moving light
        lights[nextLight] = true;

        // Move light index
        if (forward)
        {
            nextLight++;
            if (nextLight == lightCount - 2) // Stop before last
                forward = false;
        }
        else
        {
            nextLight--;
            if (nextLight == 1)
                forward = true;
        }

        return lights;
    }

    public static void Main(string[] args)
    {
        ChristmasLights lights = new ChristmasLights(8);

        for (int i = 0; i < 11; i++)
        {
            var result = lights.Next();
            Console.WriteLine("Step " + (i + 1) + ": " + string.Join(", ", result));
        }
    }
}





// [true, true, false, false, false, false, true]
