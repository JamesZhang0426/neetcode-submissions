from collections import defaultdict
class TimeMap:
    
    def __init__(self):
        self.keyvalue = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyvalue[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyvalue:
            return ""

        values = self.keyvalue[key]
        results = ""
        left = 0
        right = len(values)-1

        while left<=right:
            mid = (left+right) //2 

            if values[mid][0] <= timestamp:
                results =  values[mid][1]
                left = mid +1 
            else :
                right = mid -1 
        
        return results 

