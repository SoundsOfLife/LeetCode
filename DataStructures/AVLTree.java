public class AVLTree{
    private Node root = null;

    public void AVLTree(){}
    
    public void AVLTree(Node root){
        this.root = root;
    }

    public Node getRoot(){
        return this.root;
    }

    public void insert(int x){
        Node v = new Node(x);
        if(root == null){
            root = v;
        }else{
            if(root.val > x){
                root.left = insert(x);
            }
        }
    }

    public int getHeight(Node n){
        if(n == null){
            return 0;
        }else{
            return 1 + Math.max(getHeight(n.left),getHeight(n.right));
        }
    }

    public void delete(int x){

    }
}


class Node{
    int val;
    int height = 0;
    Node left = null;
    Node right = null;
    public void Node(int val){
        this.val = val;
    }

    public int getHeight(){
        return this.height;
    }
}