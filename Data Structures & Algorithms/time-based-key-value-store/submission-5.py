class TimeMap:

    def __init__(self):
        self.stored = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.stored:
            self.stored[key] = []
        self.stored[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        stored = self.stored.get(key, []) # Return a list of tuples

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
        
