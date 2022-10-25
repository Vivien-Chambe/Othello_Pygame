import pygame

class Board:
    def __init__(self):
        self.board = [[0 for x in range(8)] for y in range(8)]
        self.board[3][3] = 1
        self.board[4][4] = 1
        self.board[3][4] = 2
        self.board[4][3] = 2
        self.player = 1

    def draw(self, screen):
        screen.fill("Dark Green")
        for x in range(8):
            for y in range(8):
                if self.board[x][y] == 0:
                    pygame.draw.rect(screen, ("White"), [x * 50, y * 50, 50, 50], 1)
                elif self.board[x][y] == 1:
                    pygame.draw.rect(screen, ("White"), [x * 50, y * 50, 50, 50], 1)
                    pygame.draw.circle(screen, ("Black"), [x * 50 + 25, y * 50 + 25], 20)
                elif self.board[x][y] == 2:
                    pygame.draw.rect(screen, ("White"), [x * 50, y * 50, 50, 50], 1)
                    pygame.draw.circle(screen, ("White"), [x * 50 + 25, y * 50 + 25], 20)

    def reset(self):
        self.board = [[0 for x in range(8)] for y in range(8)]
        self.board[3][3] = 1
        self.board[4][4] = 1
        self.board[3][4] = 2
        self.board[4][3] = 2
        self.player = 1


    def add(self, x, y):
        if self.board[x][y] == 0:
            self.board[x][y] = self.player
            if self.player == 1:
                self.player = 2 
            else: 
                self.player = 1
            return True
        else:
            return False

    # Change color of pieces between two pieces of the same color
    def outflank(self, x, y):
        # Check if the piece is outflanked by a piece of the same color
        # If it is, change the color of the pieces between the two pieces of the same color
        # If it is not, do nothing
        
        # Check if the piece is outflanked by a piece of the same color to the right
        # If it is, change the color of the pieces between the two pieces of the same color
        # If it is not, do nothing
        for i in range(x + 1, 8):
            if self.board[i][y] == 0:
                break
            elif self.board[i][y] == self.board[x][y]:
                for j in range(x + 1, i):
                    self.board[j][y] = self.board[x][y]
                break

        # Check if the piece is outflanked by a piece of the same color to the left
        # If it is, change the color of the pieces between the two pieces of the same color
        # If it is not, do nothing
        for i in range(x - 1, -1, -1):
            if self.board[i][y] == 0:
                break
            elif self.board[i][y] == self.board[x][y]:
                for j in range(x - 1, i, -1):
                    self.board[j][y] = self.board[x][y]
                break

        # Check if the piece is outflanked by a piece of the same color to the bottom
        # If it is, change the color of the pieces between the two pieces of the same color
        # If it is not, do nothing
        for i in range(y + 1, 8):
            if self.board[x][i] == 0:
                break
            elif self.board[x][i] == self.board[x][y]:
                for j in range(y + 1, i):
                    self.board[x][j] = self.board[x][y]
                break

        # Check if the piece is outflanked by a piece of the same color to the top
        # If it is, change the color of the pieces between the two pieces of the same color
        # If it is not, do nothing
        for i in range(y - 1, -1, -1):
            if self.board[x][i] == 0:
                break
            elif self.board[x][i] == self.board[x][y]:
                for j in range(y - 1, i, -1):
                    self.board[x][j] = self.board[x][y]
                break

        # Check if the piece is outflanked by a piece of the same color to the bottom right
        # If it is, change the color of the pieces between the two pieces of the same color
        # If it is not, do nothing
        for i in range(1, 8):
            if x + i > 7 or y + i > 7:
                break
            elif self.board[x + i][y + i] == 0:
                break
            elif self.board[x + i][y + i] == self.board[x][y]:
                for j in range(1, i):
                    self.board[x + j][y + j] = self.board[x][y]
                break
        
        # Check if the piece is outflanked by a piece of the same color to the top left
        # If it is, change the color of the pieces between the two pieces of the same color
        # If it is not, do nothing
        for i in range(1, 8):
            if x - i < 0 or y - i < 0:
                break
            elif self.board[x - i][y - i] == 0:
                break
            elif self.board[x - i][y - i] == self.board[x][y]:
                for j in range(1, i):
                    self.board[x - j][y - j] = self.board[x][y]
                break

        # Check if the piece is outflanked by a piece of the same color to the bottom left
        # If it is, change the color of the pieces between the two pieces of the same color
        # If it is not, do nothing
        for i in range(1, 8):
            if x - i < 0 or y + i > 7:
                break
            elif self.board[x - i][y + i] == 0:
                break
            elif self.board[x - i][y + i] == self.board[x][y]:
                for j in range(1, i):
                    self.board[x - j][y + j] = self.board[x][y]
                break
        
        # Check if the piece is outflanked by a piece of the same color to the top right
        # If it is, change the color of the pieces between the two pieces of the same color
        # If it is not, do nothing
        for i in range(1, 8):
            if x + i > 7 or y - i < 0:
                break
            elif self.board[x + i][y - i] == 0:
                break
            elif self.board[x + i][y - i] == self.board[x][y]:
                for j in range(1, i):
                    self.board[x + j][y - j] = self.board[x][y]
                break