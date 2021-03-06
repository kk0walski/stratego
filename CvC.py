import pygame
from GUI import GUI
from Player import CompRandom, CompRandomDiagonals, oddPlayer, AlfaBeta, MinMax, AlfaBetaOdd
import time


class CvC(GUI):

    def __init__(self, size, window_width, window_height, player1, player2):
        GUI.__init__(self, size, window_width, window_height)
        self.player1 = player1
        self.player2 = player2
        self.data = {'Nazwa': [], 'Wynik': [], 'Czas': [], 'Ruch': []}

    def run(self):
        while not self.done:
            move = [0, 0]
            if self.TOURN == 1:
                begin = time.time()
                move, warunek, punkty = self.player1.run(self.board)
                end = time.time()
                czas = end - begin
                if warunek:
                    print(self.board.getState())
                    print("Player", 1, "Czas: ", czas)
                    print(punkty)
                    self.data['Nazwa'].append('Player1')
                    self.data['Wynik'].append(self.board.player1)
                    self.data['Czas'].append(czas)
                    self.data['Ruch'].append(punkty)
                    self.done = self.board.isEnd()
                    self.TOURN = 2
            else:
                begin = time.time()
                move, warunek, punkty = self.player2.run(self.board)
                end = time.time()
                czas = end - begin
                if warunek:
                    print(self.board.getState())
                    print("Player", 2, "Czas: ", czas)
                    print(punkty)
                    self.data['Nazwa'].append('Player2')
                    self.data['Wynik'].append(self.board.player2)
                    self.data['Czas'].append(czas)
                    self.data['Ruch'].append(punkty)
                    self.done = self.board.isEnd()
                    self.TOURN = 1

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

gra = CvC(10, 800, 800, player1=oddPlayer(1), player2=AlfaBetaOdd(2, 10, depth=3))
gra.run()