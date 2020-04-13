from math import sqrt
class Sudoku(object):
    def __init__(self, data):
        self.data = data
    def is_valid(self):
        n = sqrt(len(self.data))
        print(n)
        if n != int(n) or len(self.data) <= 1:
            print(False)
            return False
        else:
            for i in range(len(self.data)):
                if len(set(self.data[i])) != len(self.data[i]):
                    print("damn")
                    return False
            for i in range(len(self.data)):
                l = []
                for j in range(len(self.data)):
                    l.append(self.data[j][i])
                    print(l)
                if len(set(l)) != len(l):
                    print("so sad")
                    return False
        return True


sudoku = Sudoku([
  [1]
])

print(sudoku.is_valid())

