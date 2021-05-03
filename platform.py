class Platform:
    def __init__(self, x, y, w, h):
        self.pos = (x, y)
        self.rect = (x, y, w, h)

    def draw(self, cam):
        cam.draw_rect(self.rect, (0, 0, 0))

    def get_collider(self):
        return ((self.rect[0], self.rect[1]), (self.rect[0] + self.rect[2], self.rect[1] + self.rect[3]))

    def overlap(self, obj):
        collision = [False, False, False, False]
        collider1 = self.get_collider()
        collider2 = obj.get_collider()
        if collider2[1][0] > collider1[0][0] and collider2[1][1] > collider1[0][1] + 5 and collider2[0][1] < collider1[1][1] - 5 and collider2[0][0] < collider1[0][0]:
            collision[0] = True
        if collider2[0][0] < collider1[1][0] and collider2[1][1] > collider1[0][1] + 5 and collider2[0][1] < collider1[1][1] - 5 and collider2[1][0] > collider1[1][0]:
            collision[1] = True
        if collider2[1][1] >= collider1[0][1] and collider2[1][0] > collider1[0][0] and collider2[0][0] < collider1[1][0] and collider2[0][1] < collider1[0][1]:
            collision[2] = True
        if collider2[0][1] <= collider1[1][1] and collider2[1][0] > collider1[0][0] and collider2[0][0] < collider1[1][0] and collider2[1][1] > collider1[1][1]:
            collision[3] = True
        return collision

    def get_rect(self):
        return self.rect