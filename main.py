import sys, pygame

print(pygame.__version__)
res = (800, 800)
pygame.init()
screen = pygame.display.set_mode(res, pygame.RESIZABLE)

clock = pygame.time.Clock()
board = pygame.image.load("z\\board.png").convert()
board = pygame.transform.scale(board, res)
bp = pygame.image.load("z\\bp.png").convert_alpha()
bp = pygame.transform.scale(bp, (res[0] / 8, res[1] / 8))
br = pygame.image.load("z\\br.png").convert_alpha()
br = pygame.transform.scale(br, (res[0] / 8, res[1] / 8))
bn = pygame.image.load("z\\bn.png").convert_alpha()
bn = pygame.transform.scale(bn, (res[0] / 8, res[1] / 8))
bb = pygame.image.load("z\\bb.png").convert_alpha()
bb = pygame.transform.scale(bb, (res[0] / 8, res[1] / 8))
bq = pygame.image.load("z\\bq.png").convert_alpha()
bq = pygame.transform.scale(bq, (res[0] / 8, res[1] / 8))
bk = pygame.image.load("z\\bk.png").convert_alpha()
bk = pygame.transform.scale(bk, (res[0] / 8, res[1] / 8))
wp = pygame.image.load("z\\wp.png").convert_alpha()
wp = pygame.transform.scale(wp, (res[0] / 8, res[1] / 8))
wr = pygame.image.load("z\\wr.png").convert_alpha()
wr = pygame.transform.scale(wr, (res[0] / 8, res[1] / 8))
wn = pygame.image.load("z\\wn.png").convert_alpha()
wn = pygame.transform.scale(wn, (res[0] / 8, res[1] / 8))
wb = pygame.image.load("z\\wb.png").convert_alpha()
wb = pygame.transform.scale(wb, (res[0] / 8, res[1] / 8))
wq = pygame.image.load("z\\wq.png").convert_alpha()
wq = pygame.transform.scale(wq, (res[0] / 8, res[1] / 8))
wk = pygame.image.load("z\\wk.png").convert_alpha()
wk = pygame.transform.scale(wk, (res[0] / 8, res[1] / 8))
pygame.display.set_caption("Szachy")
programIcon = pygame.image.load("z\\bk.png").convert_alpha()
pygame.display.set_icon(programIcon)
a, b = 0, 0
wrece = False
ruch = "w"
ruchy = []


def moz(x, p):
    def spraw(p1, m1, p2, m2):
        odleglosc = 0
        while odleglosc > -1:  # pentla w dół
            odleglosc += 1
            sprawdzane = (p1 + odleglosc * m1, p2 + odleglosc * m2)
            if odleglosc > 8:
                odleglosc = -2
            elif sprawdzane not in startpos:
                mozruchy.append(sprawdzane)
            elif startpos[sprawdzane][1] is ruch:
                odleglosc = -2
            elif startpos[sprawdzane][1] is not ruch:
                mozruchy.append(sprawdzane)
                odleglosc = -2

    mozruchy = []
    if x[2] == "p":
        if ruch == "w":
            kierunek = -1
        elif ruch == "b":
            kierunek = 1
        if (p[0] + kierunek, p[1]) not in startpos:
            mozruchy.append((p[0] + kierunek, p[1]))
            if p[0] == 4.5 - 2.5 * kierunek:
                if (p[0] + kierunek * 2, p[1]) not in startpos:
                    mozruchy.append((p[0] + kierunek * 2, p[1]))
        if (p[0] + kierunek, p[1] - 1) in startpos:
            if startpos[(p[0] + kierunek, p[1] - 1)][1] is not ruch:
                mozruchy.append((p[0] + kierunek, p[1] - 1))
        if (p[0] + kierunek, p[1] + 1) in startpos:
            if startpos[(p[0] + kierunek, p[1] + 1)][1] is not ruch:
                mozruchy.append((p[0] + kierunek, p[1] + 1))#todo bicie w przelocie
    if x[2] == "r":
        spraw(p[0], 1, p[1], 0)
        spraw(p[0], -1, p[1], 0)
        spraw(p[0], 0, p[1], 1)
        spraw(p[0], 0, p[1], -1)
    if x[2] == "n":
        night = [(p[0] - 2, p[1] + 1), (p[0] - 2, p[1] - 1), (p[0] + 2, p[1] + 1), (p[0] + 2, p[1] - 1),
                 (p[0] + 1, p[1] + 2), (p[0] + 1, p[1] - 2), (p[0] - 1, p[1] - 2), (p[0] - 1, p[1] + 2)]
        for sam in night:
            if sam in startpos:
                if ruch is not startpos[sam][1]:
                    mozruchy.append(sam)
            else:
                mozruchy.append(sam)
    if x[2] == "b":
        spraw(p[0], 1, p[1], 1)
        spraw(p[0], 1, p[1], -1)
        spraw(p[0], -1, p[1], 1)
        spraw(p[0], -1, p[1], -1)
    if x[2] == "q":
        spraw(p[0], 1, p[1], 1)
        spraw(p[0], 1, p[1], -1)
        spraw(p[0], -1, p[1], 1)
        spraw(p[0], -1, p[1], -1)
        spraw(p[0], 1, p[1], 0)
        spraw(p[0], -1, p[1], 0)
        spraw(p[0], 0, p[1], 1)
        spraw(p[0], 0, p[1], -1)
    if x[2] == "k":
        dospawk = [(p[0] + 1, p[1] + 1), (p[0] + 1, p[1]), (p[0] + 1, p[1] - 1), (p[0], p[1] + 1), (p[0], p[1] - 1),
                   (p[0] - 1, p[1] + 1), (p[0] - 1, p[1]),
                   (p[0] - 1, p[1] - 1)]
        for i in dospawk:
            if i not in startpos:
                mozruchy.append(i)
        if x[3] is True and startpos[(p[0], p[1] + 3)][3] is True and (p[0], p[1] + 2) not in startpos and (p[0], p[1] + 1) not in startpos:
            mozruchy.append((p[0], p[1] + 2))
        if x[3] is True and startpos[(p[0], p[1] - 4)][3] is True and (p[0], p[1] - 2) not in startpos and (p[0], p[1] - 1) not in startpos and (p[0], p[1] - 3) not in startpos:
            mozruchy.append((p[0], p[1] - 2))
    return mozruchy


startpos = {
    (1, 1): (br, "b", "r", True), (1, 2): (bn, "b", "n"), (1, 3): (bb, "b", "b"), (1, 4): (bq, "b", "q"),
    (1, 5): (bk, "b", "k", True), (1, 6): (bb, "b", "b"), (1, 7): (bn, "b", "n"), (1, 8): (br, "b", "r", True),
    (2, 1): (bp, "b", "p"), (2, 2): (bp, "b", "p"), (2, 3): (bp, "b", "p"), (2, 4): (bp, "b", "p"),
    (2, 5): (bp, "b", "p"), (2, 6): (bp, "b", "p"), (2, 7): (bp, "b", "p"), (2, 8): (bp, "b", "p"),
    (8, 1): (wr, "w", "r", True), (8, 2): (wn, "w", "n"), (8, 3): (wb, "w", "b"), (8, 4): (wq, "w", "q"),
    (8, 6): (wb, "w", "b"), (8, 5): (wk, "w", "k", True), (8, 7): (wn, "w", "n"), (8, 8): (wr, "w", "r", True),
    (7, 1): (wp, "w", "p"), (7, 2): (wp, "w", "p"), (7, 3): (wp, "w", "p"), (7, 4): (wp, "w", "p"),
    (7, 6): (wp, "w", "p"), (7, 5): (wp, "w", "p"), (7, 7): (wp, "w", "p"), (7, 8): (wp, "w", "p"),
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
            clickval = ((pos[1] // (res[1] / 8) + 1), pos[0] // (res[1] / 8) + 1)

            if not wrece:
                if clickval in startpos:
                    if startpos[clickval][1] == ruch:
                        fig_wrence = startpos[clickval]
                        del startpos[clickval]
                        ruchy = moz(fig_wrence, clickval)
                        poczontek = clickval
                        wrece = True
            elif wrece:
                if clickval == poczontek:
                    startpos[clickval] = fig_wrence
                    wrece = False
                elif clickval in ruchy:
                    fig_wrence = (fig_wrence[0], fig_wrence[1], fig_wrence[2], False)
                    startpos[clickval] = fig_wrence
                    wrece = False
                    if poczontek[1]-clickval[1] == -2 and fig_wrence[2] == "k":
                        startpos[(clickval[0],clickval[1]-1)] = startpos[(clickval[0], clickval[1]+1)]
                        del startpos[clickval[0], clickval[1] + 1]
                    elif poczontek[1]-clickval[1] == 2 and fig_wrence[2] == "k":
                        startpos[(clickval[0],clickval[1]+1)] = startpos[(clickval[0], clickval[1]-2)]
                        del startpos[clickval[0], clickval[1] - 2]
                    if ruch == "w":
                        ruch = "b"
                    else:
                        ruch = "w"

    # Ticking
    dt = clock.tick()

    # render
    # screen.fill((0,0,0))
    screen.blit(board, (0, 0))
    for i in startpos:
        screen.blit(startpos[i][0], ((i[1] - 1) * res[1] / 8, (i[0] - 1) * res[1] / 8,))
    if wrece:
        for i in ruchy:
            pygame.draw.circle(screen, radius=res[1] / 16, center=(
                ((i[1] - 1) * res[1] / 8) + res[1] / 16, ((i[0] - 1) * res[1] / 8) + res[1] / 16), color=(0, 0, 0),
                               width=2)
    if wrece:
        x = pygame.mouse.get_pos()[1] - res[1] / 16
        y = pygame.mouse.get_pos()[0] - res[1] / 16
        screen.blit(fig_wrence[0], (y, x))

    pygame.display.flip()
