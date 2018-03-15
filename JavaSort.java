// Definition for a binary tree node.
import java.util.*;

import org.omg.PortableInterceptor.SYSTEM_EXCEPTION;

import java.lang.*;

public class Solution {

    public int[] qSort(int[] nums,int left,int right){
        if(left < right){
            int flag = nums[left];
            int i = left,j = right;
            while(i < j){
                while(i < j && nums[j] >= flag)
                    j--;
                nums[i] = nums[j];
                while(i < j && nums[i] <= flag)
                    i++;
                nums[j] = nums[i];
            }
            nums[i] = flag;
            qSort(nums, left, i - 1);
            qSort(nums, i + 1, right);
            return nums;
        }else{
            return nums;
        }
    }

    public int[] mergeSort(int[] nums,int left,int right){
        if(left < right){
            int[] ans = new int[right - left + 1];
            int mid = (left + right) / 2;
            int[] l = mergeSort(nums, left, mid);
            int[] r = mergeSort(nums, mid+1, right);
            int i = 0,j = 0,k = 0;
            while(i < l.length && j < r.length){
                if(l[i]<r[j]){
                    ans[k] = l[i];
                    k++;
                    i++;
                }else{
                    ans[k] = r[j];
                    k++;
                    j++;
                }
            }
            if(i == l.length){
                while(j < r.length){
                    ans[k] = r[j];
                    k++;
                    j++;
                }
            }
            if(j == r.length){
                while(i < l.length){
                    ans[k] = l[i];
                    k++;
                    i++;
                }
            }
            return ans;
        }else{
            return new int[]{nums[left]};
        }
    }

    public List<Integer> insertSort(int[] nums){
        List<Integer> ans = new ArrayList<>();
        ans.add(nums[0]);
        for(int i = 1;i < nums.length;i++){
            for(int j = 0;j < ans.size();j++){
                if(nums[i] <= ans.get(j)){
                    ans.add(j,nums[i]);
                    break;
                }   
                if(j == ans.size() - 1){
                    ans.add(nums[i]);
                    break;
                }
            }
        }
        return ans;
    }

    public int[] bubbleSort(int[] nums){
        for(int i = 0;i < nums.length;i++){
            for(int j = i+1;j < nums.length;j++){
                if(nums[i] > nums[j]){
                    nums[i] = nums[j] - nums[i];
                    nums[j] = nums[j] - nums[i];
                    nums[i] = nums[i] + nums[j];
                }
            }
        }
        return nums;
    }
    
    public static void main(String[] args) {
        int[] nums = {1,3,5,7,7,8,2,4,6,9,200,12};
        Solution s = new Solution();
        List<Integer> ans = s.insertSort(nums);
        for(int i = 0;i < ans.size();i++){
            System.out.println(ans.get(i));
        }
    }
}