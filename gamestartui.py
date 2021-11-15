import pygame

pygame.init()
ck = pygame.display.set_mode((600, 480))  # 游戏窗口
pygame.display.set_caption("贪吃蛇")  # 给窗口取个名 我小时候喜欢双截龙和拳皇
clock = pygame.time.Clock()
start_ck = pygame.Surface(ck.get_size())    #   充当开始界面的画布
start_ck2 = pygame.Surface(ck.get_size())  #  充当第一关的画布界面暂时占位
start_ck = start_ck.convert()
start_ck2 = start_ck2.convert()
start_ck.fill((0,0,0))
start_ck2.fill((0,0,0))

i1 = pygame.image.load("D:/i1.png")
i1.convert()

i2 = pygame.image.load("D:/i2.png")
i2.convert()

bg = pygame.image.load('D:/bj.png')
bg.convert()

n1 = True
while n1:
    clock.tick(30)
    buttons = pygame.mouse.get_pressed()
    x1, y1 = pygame.mouse.get_pos()
    if x1 >= 160 and x1 <= 410 and y1 >= 150 and y1 <= 200:
        start_ck.blit(i1, (160, 150))
        if buttons[0]:
             n1 = False
    elif x1 >= 160 and x1 <= 410 and y1 >= 230 and y1 <= 280:
        start_ck.blit(i2, (160, 230))
        if buttons[0]:
             pygame.quit()
             exit()
    else:
        start_ck.blit(i1, (160, 150))
        start_ck.blit(i2, (160, 230))

    ck.blit(start_ck, (0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出...")
            pygame.quit()
            exit()

ck.blit(start_ck2,(0,0))
pygame.display.update()

n2 = True
while n2:
    clock.tick(30)
    ck.blit(start_ck2, (0, 0))
    start_ck2.blit(bg, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出...")
            pygame.quit()
            exit()


