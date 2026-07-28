class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for operation in operations:
            if operation == "+":
                arr.append(arr[-1] + arr[-2])
            elif operation == "D":
                arr.append(2 * arr[-1])
            elif operation == "C":
                arr.pop()
            else:
                arr.append(int(operation))
         
        return sum(arr)

        