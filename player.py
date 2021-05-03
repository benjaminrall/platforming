class Player:
    def __init__(self, x, y, size):
        self.startPos = (x, y)
        self.pos = (x, y)
        self.alive = True
        self.size = size
        self.xVelocity = 400
        self.yVelocity = 0
        self.acceleration = 0
        self.maxVelocity = 1.2
        self.maxVerticalVelocity = 10
        self.jumping = False
        self.jumpForce = 1000
        self.canJump = True

    def draw(self, cam):
        cam.draw_circle(self.pos, self.size, (255, 0, 0))

    def move(self, n):
        self.pos = (self.pos[0] + (n[0] * self.xVelocity), self.pos[1])

    def jump(self, jumping, delta):
        ay = 30
        if jumping and not self.jumping and self.canJump:
            ay -= self.jumpForce 
            self.canJump = False
            self.yVelocity = 0
        self.jumping = jumping

        self.yVelocity = min(self.yVelocity + ay * delta, self.maxVerticalVelocity)
        self.pos = (self.pos[0], self.pos[1] + self.yVelocity)

        self.canJump = False

    def get_collider(self):
        return ((self.pos[0] - self.size, self.pos[1] - self.size), (self.pos[0] + self.size, self.pos[1] + self.size))

    def get_pos(self):
        return self.pos

    def collided(self, obj, collision):
        collider = obj.get_collider()
        if collision[0]:
            self.pos = (collider[0][0] - self.size, self.pos[1])
        if collision[1]:
            self.pos = (collider[1][0] + self.size, self.pos[1])
        if collision[2]:
            self.canJump = True
            self.yVelocity = 0
            self.pos = (self.pos[0], collider[0][1] - self.size)
        if collision[3]:
            self.yVelocity = 0
            self.pos = (self.pos[0], collider[1][1] + self.size)

    def die(self):
        self.pos = self.startPos
        self.yVelocity = 0