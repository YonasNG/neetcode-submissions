class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        count = Counter(students)
        result = len(students)

        for s in sandwiches:
            if count[s] > 0:
                result -= 1
                count[s] -= 1
            else:
                break
        
        return result
            

