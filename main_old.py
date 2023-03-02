import pygame, sys

print(pygame.__version__)
res = (1200, 1200)
pygame.init()
fake_screen = pygame.display.set_mode(res,pygame.RESIZABLE)
screen = fake_screen.copy()
box = pygame.Rect(50, 50, 50, 50)
clock = pygame.time.Clock()
board = pygame.image.load("C:\\Users\\hubertitymon\\Desktop\\alpha\\board.png").convert()
bp = pygame.image.load("z\\bp.png").convert_alpha()
br = pygame.image.load("z\\br.png").convert_alpha()
bn = pygame.image.load("z\\bn.png").convert_alpha()
bb = pygame.image.load("z\\bb.png").convert_alpha()
bq = pygame.image.load("z\\bq.png").convert_alpha()
bk = pygame.image.load("z\\bk.png").convert_alpha()
wp = pygame.image.load("z\\wp.png").convert_alpha()
wr = pygame.image.load("z\\wr.png").convert_alpha()
wn = pygame.image.load("z\\wn.png").convert_alpha()
wb = pygame.image.load("z\\wb.png").convert_alpha()
wq = pygame.image.load("z\\wq.png").convert_alpha()
wk = pygame.image.load("z\\wk.png").convert_alpha()
pygame.display.set_caption("Szachy")
programIcon = pygame.image.load("z\\bk.png").convert_alpha()
pygame.display.set_icon(programIcon)
a, b = 0, 0
wrence = False

def xval(posval):
    x = ((posval % 10) - 1) * 150
    return x


def yval(posval):
    y = (posval // 10 - 1) * 150
    return y


startpos = {

    11: br, 12: bn, 13: bb, 14: bq, 15: bk, 16: bb,  17: bn, 18: br,
    21: bp, 22: bp, 23: bp, 24: bp, 25: bp, 26: bp,  27: bp, 28: bp,
    81: wr, 82: wn, 83: wb, 84: wq, 86: wb, 85: wk, 87: wn, 88: wr,
    71: wp, 72: wp, 73: wp, 74: wp, 76: wp, 75: wp, 77: wp, 78: wp,
}
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
        elif event.type == pygame.VIDEORESIZE:
            fake_screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            (a, b) = pos
            a, b = (a // 150+1), (b // 150+1)*10
            clickval = a+b
            if not wrence:
                if clickval in startpos:
                    fig_wrence = startpos[clickval]
                    del startpos[clickval]
                    wrence = True
            elif wrence:
                startpos[clickval] = fig_wrence
                wrence = False

    # cheackig input
    keys = pygame.key.get_pressed()
    # if keys[pygame.K_d]:
    #     box.x += 1
    # if keys[pygame.K_a]:
    #     box.x += -1
    # if keys[pygame.K_s]:
    #     box.y += 1
    # if keys[pygame.K_w]:
    #     box.y += -1

    # Ticking
    dt = clock.tick()

    # render
    screen.fill((0, 255, 0))
    #  pygame.draw.circle(screen,(255,0,0),)
    screen.blit(board, (0, 0))
    for i in startpos:
        screen.blit(startpos[i], (xval(i), yval(i)))

    if wrence:
        x = pygame.mouse.get_pos()[1]-75
        y = pygame.mouse.get_pos()[0]-75
        screen.blit(fig_wrence,(y,x))
    # pygame.draw.rect(screen, (255, 255, 255), box)

    fake_screen.blit(pygame.transform.scale(screen, fake_screen.get_rect().size), (0, 0))
    pygame.display.flip()
