class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:          
    
        relation = defaultdict(list)
        for i, nums in enumerate(equations):
            num1, num2 = nums
            relation[num1].append((num2, values[i]))
            relation[num2].append((num1, 1 / values[i]))
        
        def calculate(num, res):
            if num == self.searched:
                self.ans = res
                return 
            for d, q in relation[num]:
                if (num, d) in visited:
                    continue
                visited.add((num, d))
                calculate(d, res * q)

        final_res = [ ]
        
        for num1, num2 in queries:
            self.searched = num2
            self.ans = 0
            visited = set()
            if num1 in relation and num2 in relation:
                calculate(num1, 1)
                final_res.append(self.ans) if self.ans != 0 else final_res.append(-1)
            else:
                final_res.append(-1)
        return final_res