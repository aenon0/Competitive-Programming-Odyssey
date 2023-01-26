class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        teams =  [ ]
        left_ptr =  0
        right_ptr = len(skill) - 1
        constant = skill[left_ptr] + skill[right_ptr]
        while left_ptr < right_ptr:
            team = [0, 0]
            if skill[left_ptr] + skill[right_ptr] == constant:
                team[0] = (skill[left_ptr])
                team[1] = (skill[right_ptr])
                left_ptr += 1
                right_ptr -= 1
            else:
                return -1
            
            teams.append(team)
            
        sum_of_chemistry = 0 
        for team in teams:
            chemistry = (team[0] * team[1])
            sum_of_chemistry += chemistry
        
        return sum_of_chemistry
        
                
            

            
            

        
