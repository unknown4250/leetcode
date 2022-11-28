from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        # key가 캐시에 없는 경우
        if key not in self.cache:
            return -1
        
        # key가 캐시에 있는 경우
        else:
            # 해당 key를 캐시의 마지막으로 이동(업데이트)
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # key가 캐시에 없는 경우
        if key not in self.cache:
            # capacity 초과하면 가장 앞에 있는 key 제거
            if len(self.cache) == self.capacity:
                self.cache.popitem(last=False)
        
        # key가 캐시에 있는 경우
        else:
            # 새로운 값으로 업데이트하기 위해 기존 key를 가장 뒤로 이동
            self.cache.move_to_end(key)
            
        # (key: value) 쌍 업데이트
        self.cache[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)