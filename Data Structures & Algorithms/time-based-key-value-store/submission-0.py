class TimeMap:
    def __init__(self):
        self.myMap = dict() 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.myMap:
            self.myMap[key] = []
        self.myMap[key].append([timestamp, value])   

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.myMap:
            return ""
        arr = self.myMap[key]
        l, r = 0, len(arr) - 1
        result = ""
        while l <= r:
            m = l + (r - l) // 2
            if arr[m][0] <= timestamp:
                result = arr[m][1]   
                l = m + 1
            else:
                r = m - 1
        return result