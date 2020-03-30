class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0


    def computeDifference(self):
        absolutes = []
        for i in range(0, len(self.__elements) - 1):
            for j in range(i + 1, len(self.__elements)):
                absolutes.append(abs(self.__elements[i] - self.__elements[j]))
        self.maximumDifference=max(absolutes)


    _ = input()
    a = [int(e) for e in input().split(' ')]

    d = Difference(a)
    d.computeDifference()

    print(d.maximumDifference)