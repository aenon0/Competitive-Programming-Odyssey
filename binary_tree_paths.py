class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # if empty tree
        if not root:
            return []
        ans = []  # answer
        
        def dfs(node: Optional[TreeNode], path: str) -> None:
            # add val to path
            path += str(node.val)
            # leaf node
            if (not node.left) and (not node.right):
                ans.append(path)
                return
            # left child exists
            if node.left:
                dfs(node.left, path + "->")
            # right child exists
            if node.right:
                dfs(node.right, path + "->")

        dfs(root, "")
        return ans
