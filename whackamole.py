import pygame
import random

# a comment
# another comment
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_location_x = random.randrange(0,640,32)
        mole_location_y = random.randrange(0,512,32)
        print(mole_location_x, mole_location_y)
        mole_rectangle = pygame.Rect(mole_location_x, mole_location_y, 32, 32)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mole_rectangle.collidepoint(event.pos):
                        print("You Hit Me!")
                        mole_location_x = random.randrange(0, 640, 32)
                        mole_location_y = random.randrange(0, 512, 32)
                        mole_rectangle.topleft = (mole_location_x, mole_location_y)
            screen.fill("light green")
            for x in range(0, 640, 32):
                pygame.draw.line(screen, "dark blue", (x, 0), (x, 512))
            for y in range(0, 512, 32):
                pygame.draw.line(screen, "dark blue", (0, y), (640, y))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_location_x, mole_location_y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
