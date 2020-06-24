# 实现ADT Map
class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self, key):
        return key % self.size

    # 线性探测
    def rehash(self, oldhash):
        return (oldhash + 1) % self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key)
        ##key不存在，未冲突
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        ##key已存在，替换val
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                # 散列冲突，再散列，直到找到空槽或者key
                nextslot = self.rehash(hashvalue)
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def get(self, key):
        # 标记散列值为查找起点
        startslot = self.hashfunction(key)
        data = None
        stop = False
        found = False
        position = startslot
        # 找key直到空槽或回到起点
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            # 未找到key，再散列继续找
            else:
                position = self.rehash(position)
                if position == startslot:
                    stop = True  # 回到起点，停
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        return self.put(key, data)


H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[20] = "chicken"
print(H.slots)
print(H.data)
print(H[20])
