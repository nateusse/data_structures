package java_dsa;

public class ArrayTheory {
    
    /* Print with for loo nested or method  */
    static void arrayMethod(){
        int[] simpleArray = {1,2,3,4,5};
        /*int[][] multiArray = new int[3][3];
        multiArray[0][1]= 1; 
        for (int i = 0; i < multiArray.length; i++) {
            for (int j = 0; j < multiArray[i].length; j++) {
                System.out.print(multiArray[i][j] + " ");
            }
           
            System.out.println();
        }*/

        //print simple aarray
        for (int k = 0; k < simpleArray.length; k++) {
             System.out.print(simpleArray[k]);
        }

        for (int element : simpleArray) {
            System.out.print(element);
        }
        
        // System.out.println(java.util.Arrays.deepToString(multiArray));
        
    }
    
}
