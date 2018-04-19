import pygame
from GUI import GUI
from Player import CompRandom, CompRandomDiagonals
import time

class CvC(GUI):

    def __init__(self, size, window_width, window_height):
        GUI.__init__(self, size, window_width, window_height)
        self.player1 = CompRandomDiagonals(1)
        self.player2 = CompRandomDiagonals(2)

    def run(self):
        while not self.done:
            if self.TOURN == 1:
                if self.player1.run(self.board):
                    print(self.board.getState())
                    self.done = self.board.isEnd()
                    self.TOURN = 2
            else:
                if self.player2.run(self.board):
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

gra = CvC(30, 300, 300)
gra.run()