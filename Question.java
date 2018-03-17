import java.util.Set;

public class Question{

    public int[] topK(int[] nums,int k){
        
    }


    public static void main(String[] args) {
       
    }
}


class minHeap{

    private int[] heap;
    private int length = 0;

    public minHeap(int cap){
        if(cap > 0){
            heap = new int[cap];
            heap[0] = Integer.MIN_VALUE;
        }
    }

    public int getMin(){
        if(heap != null){
            return heap[0];
        }else{
            return 0;
        }
    }

    public boolean insert(int val){
        if (this.length < heap.length){
            this.length += 1;
            heap[this.length] = val;
            int temp = this.length;
            while(temp != 0){
                if(heap[temp] < heap[temp/2]){
                    heap[temp] = heap[temp/2] - heap[temp];
                    heap[temp/2] = heap[temp/2] - heap[temp];
                    heap[temp] = heap[temp/2] + heap[temp];
                }
                temp /= 2;
            }
            return true;
        }else{
            if(val > heap[0]){
                heap[0] = val; 
                int temp = 0;
                while(temp <= 10){
                    if(heap)
                }

                return true;
            }else{
                return false;
            }
        }
    }
}