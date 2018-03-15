public class Solution {

    public int[] qSort(int[] nums,int left,int right){
        if(left < right){
            int flag = nums[left];
            int i = left,j = right;
            while(i < j){
                while(i < j && compare(flag, nums[j]))
                    j--;
                nums[i] = nums[j];
                while(i < j && compare(nums[i], flag))
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

    public static boolean compare(int a,int b){
        String x = String.valueOf(a) + String.valueOf(b);
        String y = String.valueOf(b) + String.valueOf(a);
        for(int i = 0;i < x.length();i++){
            if(x.charAt(i) < y.charAt(i)){
                return false;
            }else if(x.charAt(i) > y.charAt(i)){
                return true;
            }
        }
        return true;
    }

    public String largestNumber(int[] nums) {
        StringBuffer sb = new StringBuffer();
        int[] ret = qSort(nums, 0, nums.length - 1);
        for(int i = 0;i < ret.length;i++){
            sb.append(String.valueOf(ret[i]));
        }
        int j = 0;
        while(j < sb.length() - 1 && sb.charAt(j) == '0'){
            j++;
        }
        return sb.substring(j).toString();
    }

    public static void main(String[] args) {
        int[] p = {3, 30, 34, 5, 9};
        Solution s  = new Solution();
        System.out.println(s.largestNumber(p));
    }
}