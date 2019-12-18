from sensor import DroneSensor
import random


class BigQuad(DroneSensor):
    def __init__(self):
        super().__init__()
        self.dt = 0.1
        self.locate = [0, 0, 0]  # 맵에 따라 설정
        self.target = [random.randrange(-10, 11), random.randrange(-10, 11), random.randrange(-10, 11)]  # 맵에 따라 설정
        self.vel = [0, 0, 0]  # 초기 0
        self.ang = [0]  # 초기 0
        self.arrive = False
        self.stat_li = [self.locate, self.target, self.vel, self.ang, self.arrive]

    def getState(self):
        return self.stat_li

    def setMotors(self, action, finish, start):
        if finish is True:
            return
        if start is True:
            return
        x, y, z, speed = action[0], action[1], action[2], action[3]
        dx = x * speed * self.dt
        dy = y * speed * self.dt
        dz = z * speed * self.dt
        self.locate[0] += dx
        self.locate[1] += dy
        self.locate[2] += dz
        self.vel = speed * pow(x**2 + y**2 + z**2, 0.5)

    def chWall(self):
        for i in range(3):
            if self.locate[i] < self.thr[i][0] or self.locate[i] > self.thr[i][1]:
                return True
        return False

    def giveReward(self, obstacle):
        reward = 0
        terminal = False

        if self.chWall() is True:
            reward -= 200
            terminal = True
            return reward, terminal

        for obs in obstacle:
            if obs <= 0:
                reward -= 150
                terminal = True
                return reward, terminal

        dis_x = abs(self.target[0] - self.locate[0])
        dis_y = abs(self.target[1] - self.locate[1])
        dis_z = abs(self.target[2] - self.locate[2])

        if (dis_x+dis_y+dis_z) < 0.001:
            self.arrive = True
            reward += 150
            terminal = True
            return reward, terminal

        reward = 70/dis_x + 70/dis_y + 70/dis_z

        return reward, terminal


if __name__ == '__main__':
    print("QuadDrone")
