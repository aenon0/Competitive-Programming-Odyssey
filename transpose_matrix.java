class Solution {
    public int[][] transpose(int[][] matrix) {
        /*
         int temp;
        for (int i=0; i<matrix.length; i++){
            for (int j=0; j<matrix[0].length; j++){
                temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        return matrix;
         */
         int [][] ans= new int [matrix[0].length] [matrix.length];
         for (int i=0; i<matrix.length; i++){
             for (int j=0; j<matrix[0].length; j++){
                 ans[j][i] = matrix[i][j];

             }
         }
       return ans;
    }
}
