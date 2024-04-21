## 7번 ##
class Car :
    speed = 0

    def upSpeed(self, value) :
        self.speed = self.speed + value

class RV(Car) :
    seatNum = 0

    def getSeatNum(self) :
        return self.seatNum
