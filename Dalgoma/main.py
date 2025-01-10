from settings import *
from dalgona import *

import pygame as pg
import random
import sys


class Dalgona:
    SHAPES = {
        "Triangle": TRIANGLE,
        "Square": SQUARE,
        "Diamond": DIAMOND,
        "Circle": CIRCLE,
        "Unicorn": UNICORN,
        "Elephant": ELEPHANT,
        "CookieOfGod": COOKIEOFGOD,
        "Monalisa": MONALISA
    }

    def __init__(self, game):
        self.game = game
        self.mouse_held = False  # Track if the mouse button is held down
        self.mistakes = []  # List to store mistakes

        # Randomly select a dalgona shape
        dalgona_name = random.choice(list(self.SHAPES.keys()))
        initialise_dalgona(dalgona_name)
        self.grid = self.SHAPES[dalgona_name]

    def handle_mouse_input(self, pos):
        block_size = 5  # Size of each grid block
        x, y = pos
        col = x // block_size  # Determine which column was clicked
        row = y // block_size  # Determine which row was clicked
        if 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]):  # Ensure it's within grid
            if self.grid[row][col] == 0:  # If the cell is empty
                self.grid[row][col] = 3  # Change the cell to red
                self.mistakes.append(1)
            elif self.grid[row][col] == 1:  # If the cell is part of the dalgona
                self.grid[row][col] = 2  # Change the cell colour to cracked dalgona

    def handle_mouse_click(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            self.mouse_held = True
            self.handle_mouse_input(event.pos)
        elif event.type == pg.MOUSEBUTTONUP:
            self.mouse_held = False
        elif event.type == pg.MOUSEMOTION and self.mouse_held:
            self.handle_mouse_input(event.pos)

    def win_lose_condition(self):
        if len(self.mistakes) >= 3:
            print("You lost! Too many mistakes!")
            self.game.running = False  # Stop the game

    def draw(self):
        block_size = 5  # Set the size of each block
        for row_index, row in enumerate(self.grid):
            for col_index, cell in enumerate(row):
                x = col_index * block_size
                y = row_index * block_size
                rect = pg.Rect(x, y, block_size, block_size)
                if cell == 1:
                    pg.draw.rect(self.game.screen, DALGOMA_COLOUR, rect)
                elif cell == 2:
                    pg.draw.rect(self.game.screen, DALGOMA_CRACKED, rect)
                elif cell == 3:
                    pg.draw.rect(self.game.screen, RED, rect)

    def update(self, events):
        self.win_lose_condition()
        for event in events:
            self.handle_mouse_click(event)


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.dalgona = Dalgona(self)
        self.running = True

        self.timer_font = pg.font.Font(None, 38)
        self.timer_sec = 180  # Set the timer to 60 seconds
        self.last_timer_update = pg.time.get_ticks()  # Track the last time the timer was updated
        
        self.mistakes_font = pg.font.Font(None, 38)
        
    def display_mistakes(self):
        # Render and display the mistakes
        mistakes_text = self.mistakes_font.render(f"{3-len(self.dalgona.mistakes)}", True, (255, 255, 255))
        self.screen.blit(mistakes_text, (WIDTH-40, 20))

    def show_timer(self):
        # Render and display the timer
        minutes = self.timer_sec // 60
        
        timer_text = self.timer_font.render(f"{minutes}:{self.timer_sec-(minutes*60):02}", True, (255, 255, 255))
        self.screen.blit(timer_text, (20, 20))

    def run(self):
        while self.running:
            self.screen.fill(BLACK)
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    self.running = False

            # Timer logic
            current_time = pg.time.get_ticks()
            if current_time - self.last_timer_update >= 1000:  # 1 second has passed
                self.timer_sec -= 1
                self.last_timer_update = current_time

            # Check if the timer runs out
            if self.timer_sec <= 0:
                print("Time's up! You lost!")
                self.running = False  # Stop the game

            # Update and draw game objects
            self.dalgona.update(events)
            self.dalgona.draw()

            # Draw the timer
            self.show_timer()
            # Draw the mistakes
            self.display_mistakes()

            pg.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    game = Game()
    game.run()
    pg.quit()
    sys.exit()