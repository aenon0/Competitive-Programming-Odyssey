class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # Create a list of indices
        indices = list(range(len(scores)))

        # #Sort indices based on ages
        sorted_indices = sorted(indices, key=lambda i: (ages[i], scores[i]))

        # Use sorted indices to rearrange scores and ages
        sorted_ages = [ages[i] for i in sorted_indices]
        sorted_scores = [scores[i] for i in sorted_indices]
        
        

        print(sorted_ages)
        print(sorted_scores)

        result = [0] * len(sorted_scores)
        ans = result[0] = sorted_scores[0]
        
        for i in range(len(sorted_scores)):
            _max = -inf
            for j in range(0, i):
                # print(i, j)
                if (sorted_scores[j] <= sorted_scores[i]):
                    _max = max(_max, result[j] + sorted_scores[i]) 
            # print(_max)
            result[i] = max(_max, sorted_scores[i])
            ans = max(ans, result[i])
        
        print(result)
        return ans