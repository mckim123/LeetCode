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
        self.flattened_list = []
        for nestInteger in nestedList:
            self.flattened_list.extend(self.flatten(nestInteger))
        self.index = 0

    def flatten(self, nestInteger):
        if nestInteger.isInteger():
            return [nestInteger.getInteger()]

        answer = []
        for nested in nestInteger.getList():
            answer.extend(self.flatten(nested))
        return answer
    
    def next(self) -> int:
        self.index += 1
        return self.flattened_list[self.index-1]
    
    def hasNext(self) -> bool:
        return self.index != len(self.flattened_list)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())