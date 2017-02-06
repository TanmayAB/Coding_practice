import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int a[] = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
      
        int[] output = new int[n];
        output = arrayLeftRotation(a, n, k);
        for(int i = 0; i < n; i++)
            System.out.print(output[i] + " ");
      
        System.out.println();
      
    }
    public static int[] arrayLeftRotation(int[] a,int size, int rot)
    {
        int temp; 
        for(int n = 0 ; n < rot ; n++)
        {
            temp = a[0];
            for(int i =0 ; i < size-1 ; i++ )
            {
                a[i] = a[i+1];
            }
            a[size-1] = temp;
        }
        return a;
    }
}
