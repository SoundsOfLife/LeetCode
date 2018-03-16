public class Solution {
    public String reverseWords(String s) {
        StringBuffer sb = new StringBuffer();
        int l = 0,r = s.length() - 1;
        while(l <= r && s.charAt(l) == ' ')
            l++;
        while(l <= r && s.charAt(r) == ' ')
            r--;
        sb.append(s.substring(l, r+1));
        for(int i = 0;i < sb.length() - 1;){
            if(sb.charAt(i) == ' ' && sb.charAt(i + 1) == ' '){
                sb.deleteCharAt(i);
            }else{
                i++;
            }
        }
        String[] ans = sb.toString().split(" ");
        sb.delete(0, sb.length());
        for(int i = ans.length - 1;i >= 0;i--){
            sb.append(ans[i]);
            sb.append(" ");
        }
        sb.deleteCharAt(sb.length() - 1);
        return sb.toString();
    }
}