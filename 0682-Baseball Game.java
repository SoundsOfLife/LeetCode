class Solution {
    public int calPoints(String[] ops) {
         int ans = 0;
         int[] temp = new int[ops.length];
         int nums = 0;
         for(int i = 0;i < ops.length;i++){
             if(ops[i].equals("+")){
                 temp[nums] = temp[nums-1] + temp[nums-2];
                 nums++;
             }else if(ops[i].equals("D")){
                 temp[nums] = 2 * temp[nums-1];
                 nums++;
             }else if(ops[i].equals("C")){
                 nums--;
             }else{
                 int score = Integer.parseInt(ops[i]);
                 temp[nums] = score;
                 nums++;
             }
         }
         for(int i = 0;i < nums;i++){
             ans += temp[i];
         }
         return ans;
     }
 }