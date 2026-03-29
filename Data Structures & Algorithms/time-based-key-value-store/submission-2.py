class TimeMap:

    def __init__(self):
        self.time_map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))
        return None 

    def get(self, key: str, timestamp: int) -> str:
        stored = self.time_map[key] # Return a list of tuples

        # Find the exact one
        l, r = 0, len(stored) - 1
        result = ""
        while l <= r:
            mid = (l + r) // 2

            if timestamp == stored[mid][0]:
                result = stored[mid][1]
                break
            
            if timestamp > stored[mid][0]:
                result = stored[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return result
        
