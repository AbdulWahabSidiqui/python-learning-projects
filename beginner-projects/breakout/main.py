import pygame
from paddle import Paddle
from ball import Ball
from brick import Brick


colors = [
    (239, 68, 68),     # Red
    (249, 115, 22),    # Orange
    (234, 179, 8),     # Yellow
    (34, 197, 94),     # Green
    (59, 130, 246),    # Blue
]
start_x = 330
start_y = 70

spacing_x = 110
spacing_y = 40

def create_bricks():
    bricks = []
    for row in range(5):
        for col in range(5):
            brick = Brick(start_x + col *spacing_x,
                          start_y + row *spacing_y,
                          colors[row]
                          )
            bricks.append(brick)
    return bricks

bricks = create_bricks()
pygame.init()

screen = pygame.display.set_mode((1200,600),pygame.RESIZABLE)
pygame.display.set_caption("Breakout")

width = screen.get_width()
height = screen.get_height()

paddle = Paddle(width,height)
ball = Ball(width,height)

clock = pygame.time.Clock()
FPS = 60

font = pygame.font.SysFont("Arial", 72,bold=True)
small_font = pygame.font.SysFont("Arial", 30)

game_over = False
running = True
score = 0
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                game_over = False
                paddle = Paddle(width,height)
                ball = Ball(width,height)
                bricks = create_bricks()


    if not game_over:

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            paddle.move_left()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            paddle.move_right()

        ball.move()
        ball.bounce(paddle)
        if ball.is_out():
            game_over = True

        for brick in bricks:
            if ball.rect.colliderect(brick.rect):
                bricks.remove(brick)
                ball.speed_y *= -1
                score += 10
                break

    screen.fill((15, 23, 42))
    score_text = small_font.render(f"Score: {score}",True,(255,255,255))
    screen.blit(score_text,(20,20))

    paddle.draw(screen)
    ball.draw(screen)

    for brick in bricks:
        brick.draw(screen)

    if game_over:

        text = font.render("GAME OVER",True,(255,255,255))
        text_rect = text.get_rect(center=(width//2,height//2))
        screen.blit(text,text_rect)

        restart_text = small_font.render("Press R to Restart", True, (255, 255, 255))
        restart_text_rect = restart_text.get_rect(center=(width//2,height//2 +70))
        screen.blit(restart_text,restart_text_rect)

        final_score_text = small_font.render(f"Final Score: {score}", True, (255, 255, 255))
        final_score_rect = final_score_text.get_rect(center=(width//2,height//2+140))
        screen.blit(final_score_text, final_score_rect)

    if len(bricks) == 0:

        restart_text = small_font.render("Press R to Restart", True, (255, 255, 255))
        restart_text_rect = restart_text.get_rect(center=(width//2,height//2))
        screen.blit(restart_text,restart_text_rect)

    pygame.display.update()

    clock.tick(FPS)



pygame.quit()
