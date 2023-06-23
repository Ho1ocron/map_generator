import pygame
import random
import json
import sys


all_sprites = pygame.sprite.Group()
shop_room_sprite = pygame.sprite.Group()


class Shop_room(pygame.sprite.Sprite):
    def __init__(self, size, coords):
        super().__init__(all_sprites)
        self.coords = coords
        self.image = pygame.Surface(size)
        self.image.fill((102, 178, 255))
        self.rect = pygame.Rect(self.coords[0], self.coords[1], 16, 8)
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
        coords.append([0, 0])
        for _ in range(0, 56):
            x+=16
            coords.append([x, y])
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


class Json_data:
    def __init__(self):
        with open("room_map.json") as room_map_json:
            self.data = json.load(room_map_json)
    
    def map_data(self):
        map_size = self.data["map_size"]
        return map_size

    def shop_data(self):
        s = random.randint(0, len(self.data["room_shop"]["shop_room_size"]))
        #print(s)
        shop_size = self.data["room_shop"]["shop_room_size"][s-1]
        #print(f"shop size is {shop_size}")
        return shop_size


class Maingen:
    def shop_spawn(self):
        self.shops = []
        for _ in range(8):
            self.shop_rand_coords = line.line_coords()[random.randint(0, len(line.line_coords())-1)]
            shop_size = json_data.shop_data()
            line.line_coords().remove(self.shop_rand_coords)
            shop_room = Shop_room(shop_size,  self.shop_rand_coords)
            self.shops.append((shop_size, self.shop_rand_coords))
        print(self.shops)



json_data = Json_data()
maingen = Maingen()
maingen.shop_spawn()

pygame.init()
size = json_data.map_data()
WHITE = (255,255,255)
screen = pygame.display.set_mode(size)


line.line_coords()
#print(line.line_coords())
#print(len(line.line_coords()))


if __name__ == "__main__":
    start(screen)