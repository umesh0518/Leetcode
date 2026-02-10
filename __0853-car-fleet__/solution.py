class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [[p, s] for p , s in zip(position, speed)]
        pair.sort(reverse=True) # you could do it in for looping like for p, s in sorted(pair)[::-1]

        """
        we only update the stack if we find bottle neck that is car behind will arrive destination 
        before the car front means it will collide before target
        """
        stack = []

        for p , s in pair:
            
            # we append the stack if its empty or we find a bottleneck
            # we are also sure that bottleneck actually will create a fleet because 
            #the car behind is going to meet ahead before target not at target 
            #because if meets at target then timetake === for both car.

            time_taken = (target - p )/s
        
            if not stack or time_taken > stack[-1]:
                stack.append(time_taken)

        return len(stack)