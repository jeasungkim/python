import pygame
import random

# 게임 화면 크기 설정
WIDTH = 800
HEIGHT = 400

# 색상 설정
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# 패들 설정
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_SPEED = 5

# 공 설정
BALL_RADIUS = 10
BALL_SPEED_X = 3
BALL_SPEED_Y = 3

# 블록 설정
BLOCK_WIDTH = 60
BLOCK_HEIGHT = 20
BLOCK_ROWS = 5
BLOCK_COLS = 10
BLOCK_GAP = 10
BLOCK_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

# 게임 초기화
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("1인용 핑퐁 게임")
clock = pygame.time.Clock()

# 패들 생성
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)

# 공 생성
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed_x = BALL_SPEED_X * random.choice([-1, 1])
ball_speed_y = BALL_SPEED_Y * random.choice([-1, 1])

# 블록 생성
blocks = []
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        x = col * (BLOCK_WIDTH + BLOCK_GAP)
        y = row * (BLOCK_HEIGHT + BLOCK_GAP) + 50
        color = random.choice(BLOCK_COLORS)
        block = pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)
        blocks.append((block, color))

# 점수 초기화
score = 0

# 목숨 초기화
lives = 3

# 게임 종료 상태 초기화
game_over = False

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # 패들 이동 처리
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.x > 0:
            paddle.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and paddle.x < WIDTH - PADDLE_WIDTH:
            paddle.x += PADDLE_SPEED

        # 공 이동 처리
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # 벽과의 충돌 처리
        if ball.x <= 0 or ball.x >= WIDTH - BALL_RADIUS * 2:
            ball_speed_x = -ball_speed_x
        if ball.y <= 0:
            ball_speed_y = -ball_speed_y

        # 패들과의 충돌 처리
        if ball.colliderect(paddle):
            ball_speed_y = -ball_speed_y

        # 블록과의 충돌 처리
        for block, color in blocks:
            if ball.colliderect(block):
                ball_speed_y = -ball_speed_y
                blocks.remove((block, color))
                score += 10
                break

        # 공이 바닥으로 떨어질 때
        if ball.y >= HEIGHT:
            lives -= 1
            if lives == 0:
                game_over = True
            else:
                ball.x = WIDTH // 2 - BALL_RADIUS
                ball.y = HEIGHT // 2 - BALL_RADIUS
                ball_speed_x = BALL_SPEED_X * random.choice([-1, 1])
                ball_speed_y = BALL_SPEED_Y * random.choice([-1, 1])
                paddle.x = WIDTH // 2 - PADDLE_WIDTH // 2

    # 게임 화면 그리기
    screen.fill(BLACK)

    # 패들 그리기
    pygame.draw.rect(screen, WHITE, paddle)

    # 공 그리기
    pygame.draw.circle(screen, RED, (ball.x + BALL_RADIUS, ball.y + BALL_RADIUS), BALL_RADIUS)

    # 블록 그리기
    for block, color in blocks:
        pygame.draw.rect(screen, color, block)

    # 목숨 표시
    font = pygame.font.Font(None, 36)
    lives_text = font.render("Lives: " + str(lives), True, WHITE)
    screen.blit(lives_text, (WIDTH - 120, 10))

    # 점수 표시
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # 게임 종료 처리
    if game_over:
        game_over_text = font.render("GAME OVER", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2))

    # 블록 모두 제거 처리
    if len(blocks) == 0:
        you_win_text = font.render("YOU WIN", True, WHITE)
        screen.blit(you_win_text, (WIDTH // 2 - 80, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)

# 게임 종료
pygame.quit()