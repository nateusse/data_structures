public class Arrays
{
    public static void  PrintArray()
    {
        int[] simpleArray = {1, 2, 3, 4, 5};
        foreach (int element in simpleArray)
        {
            Console.Write(element + " ");
        }
        
        for (int i = 0; i < simpleArray.Length; i++ ) {  Console.Write(simpleArray[i] +" "); }
    }
}