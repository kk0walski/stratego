import pygame
from GUI import GUI
from Player import Human, CompRandomDiagonals, oddPlayer, AlfaBetaOdd

class PvC(GUI):

    def __init__(self, size, window_width, window_height):
        GUI.__init__(self, size, window_width, window_height)
        self.player1 = Human(1)
        self.player2 = AlfaBetaOdd(2, size=self.size)

    def run(self):
        while not self.done:
            for event in pygame.event.get():  # User did something
                move = [0, 0]
                if self.TOURN == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        move, warunek = self.player1.run(self.map_x, self.map_y, self.board)
                        if warunek:
                            print(self.board.getState())
                            self.done = self.board.isEnd()
                            self.TOURN = 2
                else:
                    move, warunek = self.player2.run(self.board)
                    if warunek:
                        print(self.board.getState())
                        self.done = self.board.isEnd()
                        self.TOURN = 1

            key_pressed = pygame.key.get_pressed()
            if key_pressed[pygame.K_LEFT]:  # and map_x != 0:
                self.map_x -= self.map_x_c
            elif key_pressed[pygame.K_RIGHT]:
                self.map_x += self.map_x_c
            elif key_pressed[pygame.K_UP]:
                self.map_y -= self.map_x_c
            elif key_pressed[pygame.K_DOWN]:
                self.map_y += self.map_x_c
            elif key_pressed[pygame.K_ESCAPE]:
                quit()

            # Set the screen background
            self.main_map.fill(self.BLACK)

            # Draw the grid
            self.draw()
            self.screen.blit(self.main_map, (self.map_x, self.map_y, self.window_width, self.window_height))
            # Limit to 60 frames per second
            self.clock.tick(60)

            # Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # Be IDLE friendly. If you forget this line, the program will 'hang'
            # on exit.
        pygame.quit()

gra = PvC(50, 800, 800)
gra.run()