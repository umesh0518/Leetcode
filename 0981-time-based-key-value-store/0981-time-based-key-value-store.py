class TimeMap:

    def __init__(self):
        self.store = {} # is dictionary of key: list of [value, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # might be empty so we use 
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

        

    def get(self, key: str, timestamp: int) -> str:
        res = "" # incase its empty
        values = self.store.get(key, []) # if not found then return empty list

        # now need to seach the timestamp returned in the value:
        #binary search, why? because it sorted from left to right on time tamps always

        l, r = 0 , len(values) -1 

        while l <= r:
            mid = (l + r)//2
            #look at time stamp whihc is at 1 index , value is at 0
            if values[mid][1] <= timestamp:
                # means we found a valid time but 
                #might be even bigger and close on right side
                #also this was valid so we save this for now
                res = values[mid][0] # 0 index has value
                l = mid + 1
            else:
                # the value is bigger so go left , res candidate not found yet
                r = mid -1
        return res


        
