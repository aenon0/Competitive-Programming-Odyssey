# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        adj_list = defaultdict(list)
        def dfs(node):
            if not node:
                return 
                
            if node.left:
                adj_list[node.left.val].append(node.val)
                adj_list[node.val].append(node.left.val)
                left = dfs(node.left)
            if node.right:
                adj_list[node.right.val].append(node.val)
                adj_list[node.val].append(node.right.val)
                dfs(node.right)
        
        # building adjacency list for the tree
        node = root
        dfs(node)
        # for key in adj_list.keys():
        #     print(key, adj_list[key])

        def bfs(queue, visited):
            _k = 0 
            ans = [ ]
            while queue:
                _k += 1
                size = len(queue)
                for _ in range(size):
                    curr = queue.popleft()
                    for neighbor in adj_list[curr]:
                        if neighbor not in visited:
                            if _k == k:
                                print(neighbor)
                                ans.append(neighbor)
                            visited.add(neighbor)
                            queue.append(neighbor)
            # print(visited)
            return ans
        if k == 0:
            return [target.val]
        queue = deque()
        visited = set()
        visited.add(target.val)
        queue.append(target.val)
        return bfs(queue, visited)