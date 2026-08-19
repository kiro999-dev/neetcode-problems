class TimeMap:
    def __init__(self):
      self.myMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.myMap:
            self.myMap[key] = []
        self.myMap[key].append([value,timestamp])
    def get(self, key: str, timestamp: int) -> str:
       l = 0
       if( key not in self.myMap):
        return ""
       array = self.myMap[key]
       r = len(array) - 1
       m = (l + r )// 2
       res = ""
       while l <= r:
        m = l + (r - l) // 2
        if(array[m][1] == timestamp):
            return array[m][0]
        if(array[m][1] <= timestamp):
            res = array[m][0]
            l = m + 1
        else:
            r = m - 1
        
        
       return res