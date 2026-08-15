class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars  = list(zip(position,speed))
        cars = sorted(cars,key=lambda x: x[0], reverse=True)
        stack = []
        for i in range(len(cars)):
            t = (target - cars[i][0]) / cars[i][1] 
            if(len(stack) == 0 or stack[-1] < t):
                stack.append(t)
        print(stack)
        return len(stack)