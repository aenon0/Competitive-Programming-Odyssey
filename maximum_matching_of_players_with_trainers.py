class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        
        p = 0 
        t = 0 
        count_match = 0
        while p < len(players) and t < len(trainers):
            if players[p] > trainers[t]:
                t += 1
            elif players[p] <= trainers[t]:
                count_match += 1
                t += 1
                p += 1
        return count_match
                
