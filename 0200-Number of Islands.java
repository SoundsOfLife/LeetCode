import java.util.*;
import java.lang.*;

public class Solution {
    public int numIslands(char[][] grid) {
        if(grid.length == 0){
            return 0;
        }
        int ans = 0;
        int[][] visit = new int[grid.length][grid[0].length];
        for(int i = 0;i < visit.length;i++){
            for(int j = 0;j < visit[0].length;j++){
                visit[i][j] = 1;
            }
        }
        
        for(int i = 0;i < grid.length;i++){
            for(int j = 0;j < grid[0].length;j++){
                if(grid[i][j] == '1' && visit[i][j] == 1){
                    ans++;
                    visit = DFS(i, j, grid, visit);
                }
                
            }
        }
        return ans;
    }

    public static int[][] DFS(int a,int b,char[][] grid,int[][] visit){
        if(a >= 0 && b >= 0 && a < visit.length && b < visit[0].length && visit[a][b] == 1 &&  grid[a][b] == '1'){
            visit[a][b] = -1;
            visit = DFS(a + 1, b, grid,visit);
            visit = DFS(a - 1, b, grid,visit);
            visit = DFS(a, b - 1, grid,visit);
            visit = DFS(a, b + 1, grid,visit);
        }
        return visit;
    }
    public static void main(String[] args) {
        
    }
}