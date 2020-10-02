class Solution {
    public int minPathSum(int[][] grid) {
        
        // moving right and down but need to check left and up for previous path
        
        int m = grid.length;
        int n = grid[0].length;
        
        // tmp grid holds sums of path for each index
        int [][] tmp_grid = new int [m][n];
        
        for (int i = 0; i < tmp_grid.length; i++){
            
            for (int j = 0; j < tmp_grid[i].length; j++){
                
                // add current number to tmp grid
                tmp_grid[i][j] += grid[i][j];
                
                // if bounds are ok to look up and left and choose min of both
                if (i > 0 && j > 0){
                    tmp_grid[i][j] += Math.min(tmp_grid[i-1][j] , tmp_grid[i][j-1]);
                    
                }
                // if can't look left, just look up
                else if (i > 0){
                    tmp_grid[i][j] += tmp_grid[i-1][j];
                }
                // if can't look up just look left
                else if (j > 0){
                    tmp_grid[i][j] += tmp_grid[i][j-1];
                }
            }
            
        }
        return tmp_grid[tmp_grid.length - 1][tmp_grid[0].length -1];
    }
}
