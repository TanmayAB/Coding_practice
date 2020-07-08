import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;
import java.util.Arrays;

public class Solution {
    static int pairs(int[] a,int k) {
        int count = 0;

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