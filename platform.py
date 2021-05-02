class Platform:
    def __init__(self, x, y, w, h):
        self.pos = (x, y)
        self.rect = (x, y, w, h)

    def draw(self, cam):
        cam.draw_rect(self.rect, (0, 0, 0))