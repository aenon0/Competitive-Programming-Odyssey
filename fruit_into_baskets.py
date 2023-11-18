class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        tree_types = defaultdict(int)
        left = 0
        max_fruit = 1
        fruit = 0 
        tree_types[fruits[0]] += 1
        for right in range(1, len(fruits)):
            tree_types[fruits[right]] += 1 
            while len(tree_types) > 2:   
                tree_types[fruits[left]] -= 1
                if tree_types[fruits[left]] == 0:
                    del tree_types[fruits[left]]
                left += 1
        
            max_fruit = max(max_fruit, right - left + 1)
        
        return max_fruit
