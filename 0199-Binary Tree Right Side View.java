import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}


public class Solution {
    class Node{
        TreeNode tNode;
        Node next;
        Node(TreeNode x){tNode = x;}
    }

    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> ans = new ArrayList<Integer>();
        Node list = null;
        if(root == null){
            return ans;
        }else{
            list = new Node(root);
        }
        while(list != null){
            Node temp = new Node(list.tNode);
            Node head = temp;
            ans.add(list.tNode.val);
            while(list != null){
                if(list.tNode.right != null){
                    temp.next = new Node(list.tNode.right);
                    temp = temp.next;
                }
                if(list.tNode.left != null){
                    temp.next = new Node(list.tNode.left);
                    temp = temp.next;
                }
                list = list.next;
            }
            list = head.next;
        }
        return ans;
    }
    public static void main(String[] args) {
        
    }
}