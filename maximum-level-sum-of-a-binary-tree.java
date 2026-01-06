/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxLevelSum(TreeNode root) {
        Queue<TreeNode> q=new LinkedList<>();
        q.add(root);
        int mxsum=Integer.MIN_VALUE;
        int level=0;
        int ans=0;
        while(!q.isEmpty()){
            level++;
            int x=q.size();
            int levelsum=0;
            for(int i=0;i<x;i++){
                TreeNode node=q.poll();
                levelsum+=node.val;
                if(node.left!=null){
                    q.add(node.left);
                }
                if(node.right!=null){
                    q.add(node.right);
                }
            }
            if(levelsum>mxsum){
                mxsum=levelsum;
                ans=level;
            }
        }
        return ans;
    }
}
