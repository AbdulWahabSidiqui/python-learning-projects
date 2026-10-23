import pygame

pygame.init()

display_info = pygame.display.Info()

WIDTH = int(display_info.current_w * 0.85)
HEIGHT = int(display_info.current_h * 0.85)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

BACKGROUND = (8, 12, 30)
ALIEN_COLORS = [
    (255, 80, 120),
    (180, 80, 255),
    (80, 180, 255),
    (80, 255, 180),
    (120, 255, 100)
]

pygame.display.set_caption("Space Invaders")

running = True

class Alien:
    def __init__(self):
        self.aliens = []

        self.speed = 2
        self.direction = 1
        self.drop_distance = 25

        self.formation_width = 8 * 40 + 7 * 20
        self.horizontal_gap = 20
        self.vertical_gap = 20
        self.start_x = (WIDTH - self.formation_width) // 2
        self.start_y = 50

        for row in range(5):
            y = self.start_y + row * (30 + self.vertical_gap)
            for col in range(8):
                x = self.start_x + col * (40 + self.horizontal_gap)
                alien = pygame.Rect(x,y, 40, 30)
                self.aliens.append((alien, ALIEN_COLORS[row]))

    def move(self):
        for alien, color in self.aliens:
            alien.x += self.direction * self.speed

        leftmost = min(alien.x for alien,color in self.aliens)
        rightmost = max(alien.x + alien.width for alien,color in self.aliens)

        if rightmost >= WIDTH or leftmost <= 0:
            self.direction *= -1

            for alien,color in self.aliens:
                alien.y += self.drop_distance


class Player:
    def __init__(self):
        self.width = 50
        self.height = 30

        self.x = (WIDTH - self.width) // 2
        self.y = HEIGHT - 70

        self.speed = 8

    def draw(self,screen):
        pygame.draw.polygon(screen,(80, 200, 255),[(self.x + self.width //2,self.y),(self.x, self.y + self.height),(self.x + self.width, self.y + self.height)])

    def move(self,keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        if self.x < 0:
            self.x = 0

        if self.x > WIDTH - self.width:
            self.x = WIDTH - self.width

class Bullet:
    def __init__(self,player):
        self.width = 5
        self.height = 15

        self.x = player.x + player.width // 2 - self.width // 2
        self.y = player.y - self.height
        self.speed = 8

    def draw(self,screen):
        bullet = pygame.Rect(self.x,self.y,self.width,self.height)
        pygame.draw.rect(screen,"WHITE",bullet)

    def move(self):
        self.y -= self.speed

    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.width,self.height)

player = Player()
bullets = []
alien_fleet = Alien()
aliens = alien_fleet.aliens
clock = pygame.time.Clock()

shoot_cooldown = 250  # milliseconds
last_shot = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)
    alien_fleet.move()

    current_time = pygame.time.get_ticks()

    if keys[pygame.K_SPACE]:
        if current_time - last_shot >= shoot_cooldown:
            bullets.append(Bullet(player))
            last_shot = current_time

    for bullet in bullets:
         bullet.move()

    bullets = [bullet for bullet in bullets if bullet.y + bullet.height > 0]

    for bullet in bullets:
        for alien,color in aliens:
            if bullet.get_rect().colliderect(alien):
                aliens.remove((alien, color))
                bullets.remove(bullet)
                break
    if not aliens:
        running = False

    screen.fill(BACKGROUND)

    for alien, color in aliens:
        pygame.draw.rect(screen, color, alien)

    player.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()