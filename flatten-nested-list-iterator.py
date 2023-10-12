# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._list = [ ]
        for item in nestedList:
            self._list.extend(self.flatten(item))
        self.ptr = 0 
    
    def next(self) -> int:
        ans = self._list[self.ptr]
        self.ptr += 1
        return ans 

    def hasNext(self) -> bool:
        return self.ptr < len(self._list)        
         
    def flatten(self, item):
        if item.isInteger():
            return [item]
        res = [ ]
        for it in item.getList():
            res.extend(self.flatten(it))
        return res
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())