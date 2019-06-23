import math
import argparse

class CountMinSketch():
    def __init__(self, width, depth):
        self.width      = width
        self.depth      = depth
        self.error_rate = 2 / self.width
        self.confidence = 1 - (1 / math.pow(2, self.depth))
        self.matrix     = [[0] * self.width for _ in range(self.depth)]

    def __hash(self, value):
        indexes = []
        for n in range(self.depth):
            hashed_value = hash(value + str(n))
            indexes.append(int(hashed_value) % self.depth)
        return indexes
        
    def __set(self, value, x):
        indexes = self.__hash(value)
        for i,j in enumerate(indexes):
            if x: 
                self.matrix[i][j] += x
            else:
                self.matrix[i][j] = x
    
    def insert(self, value):
        self.__set(value, 1)
        
    def delete(self, value):
        self.__set(value, 0)
        
    def get_frequency(self, value):
        indexes = self.__hash(value)
        values  = [] 
        for i,j in enumerate(indexes):
            values.append(self.matrix[i][j])
        return min(values)

def main():
    parser = argparse.ArgumentParser(description='count min sketch example')
    parser.add_argument('--file', type=str)
    parser.add_argument('--val', type=str)
    args = parser.parse_args()
    cms  = CountMinSketch(10_000, 10)
    with open(args.file, 'r', encoding='utf-8') as file:
        [cms.insert(line.strip('\n')) for line in file]
    print(cms.get_frequency(args.val))

if __name__ == '__main__':
    main()
