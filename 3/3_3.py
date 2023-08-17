import math

class Vector:
    def __init__(self, size, data):
        self.size = size
        self.data = data

    def add(self, data):
        for i in range(self.size):
            self.data[i] = int(self.data[i]) + int(data[i])

    def sub(self, data):
        for i in range(self.size):
            self.data[i] = int(self.data[i]) - int(data[i])

    def mul(self, data):
        for i in range(self.size):
            self.data[i] = float(self.data[i]) * data

    def div(self, data):
        for i in range(self.size):
            self.data[i] = float(self.data[i]) / data

    def get_length(self):
        return math.sqrt(float(self.data[0])*float(self.data[0])
                         +float(self.data[1])*float(self.data[1])
                         +float(self.data[2])*float(self.data[2]))

    def get_data(self):
        return self.data

# get data
line = input().split()
vector_A = Vector(3, line)
line = input().split()
vector_B = Vector(3, line)

action = input()
if action == "add":
    vector_A.add(vector_B.data)
    print("%d %d %d" % (int(vector_A.data[0]), int(vector_A.data[1]), int(vector_A.data[2])))
if action == "sub":
    vector_A.sub(vector_B.data)
    print("%d %d %d" % (int(vector_A.data[0]), int(vector_A.data[1]), int(vector_A.data[2])))
if action == "mul":
    number = int(input())
    vector_A.mul(number)
    print("%d %d %d" % (int(vector_A.data[0]), int(vector_A.data[1]), int(vector_A.data[2])))
if action == "div":
    number = int(input())
    vector_A.div(number)
    print("%.2f %.2f %.2f" % (float(vector_A.data[0]), float(vector_A.data[1]), float(vector_A.data[2])))
if action == "get_length":
    print("%.2f" % (vector_A.get_length()))