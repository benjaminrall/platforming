class Player:
    def __init__(self, x, y, size):
        self.pos = (x, y)
        self.alive = True
        self.size = size
        self.xVelocity = 400
        self.yVelocity = 0
        self.acceleration = 0
        self.maxVelocity = 1.2
        self.gravity = 9.8
        self.jumping = False
        self.jumpForce = 1000
        self.colliding = False

    def draw(self, cam):
        cam.draw_circle(self.pos, self.size, (255, 0, 0))

    def move(self, n):
        self.pos = (self.pos[0] + (n[0] * self.xVelocity), self.pos[1])

    def jump(self, jumping, delta):
        ay = 30
        if jumping and not self.jumping:
            ay -= self.jumpForce 
            self.yVelocity = 0
            print("jumped")
        self.jumping = jumping
        if self.pos[1] <= 0:
            self.yVelocity += ay * delta
            self.pos = (self.pos[0], self.pos[1] + self.yVelocity)

        if self.pos[1] > 0:
            self.pos = (self.pos[0], 0)
            self.yVelocity = 0

    def get_collider(self):
        return ((self.pos[0] - self.size, self.pos[1] - self.size), (self.pos[0] + self.size, self.pos[1] + self.size))

    def get_pos(self):
        return self.pos

    def collided(self, obj, collision):
        pass