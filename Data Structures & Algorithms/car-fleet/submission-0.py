class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [] # record the time of previous car fleet reached the target
        cars = sorted(zip(position, speed), reverse = True) 
        # I sorted the cars by positions in decending orders, so I can process the closest car to the target first. This way, when I look at a car, I already know the arrival time of the fleet directly ahead of it.

        for p, s in cars:
            hours = (target - p) / s
            if not stack or hours > stack[-1]:
                stack.append(hours)
        
        return len(stack)

