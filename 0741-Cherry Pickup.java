class Solution {
    public int cherryPickup(int[][] grid) {
        if (grid==null || grid.length==0 || grid[0].length==0) return 0;
        int n=grid.length;
        
        int[][][] dp=new int[n+1][n+1][n+1];
        for (int i=0;i<=n;i++)
            for (int j=0;j<=n;j++)
                Arrays.fill(dp[i][j], -1);
        
        dp[1][1][1]=grid[0][0];
        for (int x1=1;x1<=n;x1++){
            for (int y1=1;y1<=n;y1++){
                for (int x2=1;x2<=n;x2++){
                    int y2=x1+y1-x2;
                    if (dp[x1][y1][x2]>=0 || y2<1 || y2>n || grid[x1-1][y1-1]<0 || grid[x2-1][y2-1]<0) continue;
                    int max1 = Math.max(dp[x1-1][y1][x2],   dp[x1][y1-1][x2]);
                    int max2 = Math.max(dp[x1-1][y1][x2-1], dp[x1][y1-1][x2-1]);
                    int max  = Math.max(max1, max2);
                    if (max == -1) continue;
                    
                    dp[x1][y1][x2] = max+grid[x1-1][y1-1];
                    if (x2!=x1) dp[x1][y1][x2] += grid[x2-1][y2-1];
                }
            }
        }
        return Math.max(0, dp[n][n][n]);
    }
}