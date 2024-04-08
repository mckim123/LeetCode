class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n1 = sum(students)
        n2 = len(students) - n1
        
        for s in sandwiches:
            if s == 1:
                if n1 == 0:
                    return n2
                n1 -= 1
            else:
                if n2 == 0:
                    return n1
                n2 -= 1
        return 0