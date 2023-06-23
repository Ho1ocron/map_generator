import pygame
import random
import sys


class shop_room(pygame.sprite.Sprite):
     def __init__(self):
          self.rand_coords = line.line_coords()[random.randint(0, len(line.line_coords())+1)]
          super().__init__(all_sprites)
          self.image = pygame.Surface((16, 8))
          self.image.fill((102, 178, 255))
          self.rect = pygame.Rect(self.rand_coords[0], self.rand_coords[1], 16, 8)
          pygame.draw.rect(self.image, (102, 178, 255), self.rect, 1)
          self.add(shop_room_sprite)



class line:
    def __init__(screen):
        kx = 0
        ky = 0
        for _ in range(0, 8):
            pygame.draw.line(screen, (0, 0, 0), (0, ky), (256, ky), 1)
            ky+=16
        for _ in range(0, 8):
            pygame.draw.line(screen, (0, 0, 0), (kx, 0), (kx, 256), 1)
            kx+=16

    def line_coords():
        coords = []
        x = 0
        y = 0
        coords.append((0, 0))
        for _ in range(0, 56):
            x+=16
            coords.append((x, y))
            if x == 112:
                x = 0
                y += 16
        return coords
              


def start(screen):
    while True:
        screen.fill(WHITE)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        line.__init__(screen)
        all_sprites.draw(screen)
        pygame.display.flip()


all_sprites = pygame.sprite.Group()
shop_room_sprite = pygame.sprite.Group()

pygame.init()
size = (128, 128)
WHITE = (255,255,255)
screen = pygame.display.set_mode(size)

shop_room()
line.line_coords()
print(line.line_coords())
print(len(line.line_coords()))

if __name__ == "__main__":
     start(screen)