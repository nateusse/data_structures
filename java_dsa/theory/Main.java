import java.util.Arrays;

public class Main {
    public static void main(String[] args){
        int[] arr = new int[5]; 
        //arr[arr.length - 2] = 4;
        StaticArray.insertEnd(arr,1,0,5);
        StaticArray.insertEnd(arr,2,1,5);
        System.out.print(Arrays.toString(arr));
        StaticArray.removeEnd(arr, 2);
        System.out.print(Arrays.toString(arr));

        /*//Dinamic array
        DynamicArray dinoarr = new DynamicArray(5);
        System.out.print(Arrays.toString(arr));*/
    }
}


   