import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Arrays;

public class Solution {
    static int pairs(int[] a,int k) {
        int res,count = 0;
/*
        for(int i = a.length -1; i > 0 ;i--)
        {
            if(a[i] < k)
            {
                break;
            }
            else
            {
                for(int j = i-1; j >= 0; j--)
                {
                    if(a[i] - a[j] == k)
                    {
                        count++;
                        break;
                    }
                }
            }
        }
        return count;
        */
        for(int i = 0; i < a.length -1; i++)
        {
         //   System.out.println("a[i] is : " + a[i] + "Searching for :" + a[i] + k);
            res = binSearch(a,0,a.length -1,a[i]+k);
            if(res == 1)
            {
                count++;    
            }
        }
        return count;
    }
    public static int binSearch(int[] a, int min, int max,int n)
    {
        int mid = (max + min)/2;
        if(min > max)
        {
       //     System.out.println(n+" not found in the array");
           return -1;
        }
        if(a[mid] == n)
        {
       //     System.out.println("Found : " + n);
            return 1;
        }
        else if(a[mid] > n)
        {
            return binSearch(a,min,mid-1,n);
        }
        else
        {
            return binSearch(a,mid+1,max,n);
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int res;
        
        String n = in.nextLine();
        String[] n_split = n.split(" ");
        
        int _a_size = Integer.parseInt(n_split[0]);
        int _k = Integer.parseInt(n_split[1]);
        
        int[] _a = new int[_a_size];
        int _a_item;
        String next = in.nextLine();
        String[] next_split = next.split(" ");
        
        for(int _a_i = 0; _a_i < _a_size; _a_i++) {
            _a_item = Integer.parseInt(next_split[_a_i]);
            _a[_a_i] = _a_item;
        }
        Arrays.sort(_a);
        res = pairs(_a,_k);
        System.out.println(res);
        
    }
}
