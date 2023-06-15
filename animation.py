from helper import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))


def draw(update, runtime):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, AXLE_POINT)
    if update:
        update_osc_point(runtime)
    pygame.draw.rect(WIN, RED, OSC_POINT)
    pygame.draw.line(WIN, BLACK, (AXLE_POINT.x + 8, AXLE_POINT.y + 8), (OSC_POINT.x + 8, OSC_POINT.y + 8))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    clock.tick(30)

    
    start_time = time.time()
    pre_time = time.time() # previous iteration time
    dt = 0.001

    run = True
    while run:
        runtime = time.time()-start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        update = True if pre_time + dt <= time.time() else False 
        draw(update, runtime)
        if update:
            update = not update
            pre_time = time.time()


if __name__ == '__main__':
    main()