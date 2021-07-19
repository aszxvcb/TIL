'''
    - 많은 조건 분기

    간단한 코드로 짤 수 있는 방법이 뭐가 있을까?
'''

class Rectangle:
    lx = 0
    ly = 0
    rx = 0
    ry = 0

    def __init__(self, lx, ly, rx, ry):
        self.lx = lx
        self.ly = ly
        self.rx = rx
        self.ry = ry

    def faceOverlap(self, target):
        ## 겹치지 않는 조건, 그 외는 겹침
        if ((self.rx < target.lx) or (self.lx > target.rx) or (self.ly > target.ry) or (self.ry < target.ly)):
            return False
        else:
            return True
            
    def pointOverlap(self, target):
        
        if ((self.lx == target.rx and self.ly == target.ry) or (self.rx == target.lx and self.ry == target.ly) \
            or (self.lx == target.rx and self.ry == target.ly) or (self.rx == target.lx and self.ly == target.ry)):
            return True

    def lineOverlap(self, target):

        if ((self.ly == target.ry and ((self.lx <= target.lx and target.lx <= self.rx) or (self.lx <= target.rx and target.rx <= self.rx))) or \
            (self.ry == target.ly and ((self.lx <= target.lx and target.lx <= self.rx) or (self.lx <= target.rx and target.rx <= self.rx))) or \
            (self.lx == target.rx and ((self.ly <= target.ly and target.ly <= self.ry) or (self.ly <= target.ry and target.ry <= self.ry))) or \
            (self.rx == target.lx and ((self.ly <= target.ly and target.ly <= self.ry) or (self.ly <= target.ry and target.ry <= self.ry)))):
            return True

def solution(arr):
    a = Rectangle(arr[0], arr[1], arr[2], arr[3])
    b = Rectangle(arr[4], arr[5], arr[6], arr[7])

    ## 점이 겹침
    if a.pointOverlap(b) or b.pointOverlap(a):
        print("c")
        return

    ## 선이 겹침
    if a.lineOverlap(b) or b.lineOverlap(a):
        print('b')
        return

    ## 면이 겹침
    if a.faceOverlap(b) or b.faceOverlap(a):
        print("a")
        return
    
    print('d')


if __name__ == "__main__":
    for _ in range(4):
        arr = list(map(int, input().split()))

        solution(arr)