import pygame, sys
print(pygame.__version__)
res = (800, 800)
pygame.init()
screen = pygame.display.set_mode(res, pygame.RESIZABLE)
rbiałych = True

clock = pygame.time.Clock()
board = pygame.image.load("z\\board.png").convert()
board = pygame.transform.scale(board, res)
bp = pygame.image.load("z\\bp.png").convert_alpha()
bp = pygame.transform.scale(bp, (res[0]/8, res[1]/8))
br = pygame.image.load("z\\br.png").convert_alpha()
br = pygame.transform.scale(br, (res[0]/8, res[1]/8))
bn = pygame.image.load("z\\bn.png").convert_alpha()
bn = pygame.transform.scale(bn, (res[0]/8, res[1]/8))
bb = pygame.image.load("z\\bb.png").convert_alpha()
bb = pygame.transform.scale(bb, (res[0]/8, res[1]/8))
bq = pygame.image.load("z\\bq.png").convert_alpha()
bq = pygame.transform.scale(bq, (res[0]/8, res[1]/8))
bk = pygame.image.load("z\\bk.png").convert_alpha()
bk = pygame.transform.scale(bk, (res[0]/8, res[1]/8))
wp = pygame.image.load("z\\wp.png").convert_alpha()
wp = pygame.transform.scale(wp, (res[0]/8, res[1]/8))
wr = pygame.image.load("z\\wr.png").convert_alpha()
wr = pygame.transform.scale(wr, (res[0]/8, res[1]/8))
wn = pygame.image.load("z\\wn.png").convert_alpha()
wn = pygame.transform.scale(wn, (res[0]/8, res[1]/8))
wb = pygame.image.load("z\\wb.png").convert_alpha()
wb = pygame.transform.scale(wb, (res[0]/8, res[1]/8))
wq = pygame.image.load("z\\wq.png").convert_alpha()
wq = pygame.transform.scale(wq, (res[0]/8, res[1]/8))
wk = pygame.image.load("z\\wk.png").convert_alpha()
wk = pygame.transform.scale(wk, (res[0]/8, res[1]/8))
pygame.display.set_caption("Szachy")
programIcon = pygame.image.load("z\\bk.png").convert_alpha()
pygame.display.set_icon(programIcon)
a, b = 0, 0
wrence = False

def xval(posval):
    x = ((posval % 10) - 1) * res[1]/8
    return x


def yval(posval):
    y = (posval // 10 - 1) * res[1]/8
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
            a, b = (a // (res[1]/8)+1), (b // (res[1]/8)+1)*10
            clickval = a+b

            if not wrence:
                if clickval in startpos:
                    screen.get_at(pos)[:3]
                    print(screen.get_at(pos)[:1])
                    fig_wrence = startpos[clickval]
                    del startpos[clickval]
                    wrence = True
            elif wrence:
                startpos[clickval] = fig_wrence
                wrence = False

    # Ticking
    dt = clock.tick()

    # render

    screen.blit(board, (0, 0))
    for i in startpos:
        screen.blit(startpos[i], (xval(i), yval(i)))

    if wrence:
        x = pygame.mouse.get_pos()[1]-res[1]/16
        y = pygame.mouse.get_pos()[0]-res[1]/16
        screen.blit(fig_wrence, (y, x))

    pygame.display.flip()
