class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        distance = [0, 0]
        _dir = [0, 1]
        turn = {
            (0, -1) : (1, 0),
            (0, 1) : (-1, 0),
            (-1, 0) : (0, -1),
            (1, 0) : (0, 1)
        }
       

        for ins in instructions * 1000:
            if ins == "G":
                distance[0] += _dir[0]
                distance[1] += _dir[1]
            elif ins == "L":
                _dir = list(turn[tuple(_dir)])
            else:
                x, y = turn[tuple(_dir)]
                _dir = [-1 * x, -1 * y]
    
            # print(ins, distance, _dir)

        if _dir == [0, 1] and (distance[0] != 0 or distance[1] != 0):
            return False
        return True