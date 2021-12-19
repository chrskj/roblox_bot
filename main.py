# Modules
import pygame
from time import sleep

from os import system, name
from api.keybinds import Chat, Hotkey

from screen.colors import Colors
from screen.metrics import Metrics

from api.windows import WindowManager
from screen.functions import clear, getInfo

from api.user import equipItem, leaveGame, resetChar
from api.movement import Move, RandomMove, MoveToPos, resetPosition

# Template functions
def _clear():

    """Cross-platform method of clearing the terminal"""

    if name == "nt":

        system("cls")

    elif name == "posix":

        system("clear")

    else:

        raise SystemError("Unsupported operating system %" % name)

# Initialization
HANDLER = WindowManager()

pygame.init()

# Create window
SCREEN = pygame.display.set_mode((640, 480))

METRICS = Metrics(SCREEN, Colors.BLACK)

# Focus on ROBLOX only
HANDLER.focusROBLOX()

resetChar()

# Proceed once reset is done
TILE_TIME = 0.175
DES_POSX = 0
DES_POSY = 0
sleep(7)

# Begin master loop
while True:

    # Fetch screen size and mouse positions
    X, Y, W, H = getInfo()
    _X, _Y, _W, _H = getInfo()

    # Update every frame
    clear(SCREEN, Colors.WHITE)

    # Invert coordinates for use in different grid
    Y = H - Y

    # Display our X and Y
    METRICS.setPos((X, Y))

    METRICS.show()

    # Set the line points
    points = [
        [(0, _Y), (W, _Y), Colors.GREEN],
        [(X, 0), (X, H), Colors.RED]
    ]

    # Show the lines
    for point_pair in points:

        pygame.draw.lines(SCREEN, point_pair[2], True, (point_pair[0], point_pair[1]), 1)

    # Handle events
    for event in pygame.event.get():

        # Exit script
        if event.type == pygame.QUIT:

            Chat("Script closed; stopping..")

            resetChar()

            _clear()

            pygame.quit()

            exit()

        # Move to position
        if event.type == pygame.MOUSEBUTTONUP:

            MoveToPos((X, Y))

            Chat("Moved to designated position.")

        # Keystrokes
        if event.type == pygame.KEYDOWN:

            # Reset character
            if event.unicode.upper() == "R":

                resetPosition()

                resetChar()

                sleep(4.5)

                Chat("Reset request complete.")

            # Leave game
            if event.unicode.upper() == "L":

                resetPosition()

                leaveGame()

            # Leave game
            if event.unicode.upper() == "I":
                while True:
                    DES_POSX = 8
                    DES_POSY = -19.5
                    MoveToPos((DES_POSX, DES_POSY))
                    DES_POSX += 11.5
                    MoveToPos((DES_POSX, DES_POSY))

                    for i in range(4):
                        for i in range(4):
                            DES_POSY -= 15
                            MoveToPos((DES_POSX, DES_POSY))
                            DES_POSX -= 3
                            MoveToPos((DES_POSX, DES_POSY))
                            DES_POSY += 15
                            MoveToPos((DES_POSX, DES_POSY))
                            DES_POSX -= 3
                            MoveToPos((DES_POSX, DES_POSY))

                        for i in range(4):
                            DES_POSY -= 15
                            MoveToPos((DES_POSX, DES_POSY))
                            DES_POSX += 3
                            MoveToPos((DES_POSX, DES_POSY))
                            DES_POSY += 15
                            MoveToPos((DES_POSX, DES_POSY))
                            DES_POSX += 3
                            MoveToPos((DES_POSX, DES_POSY))
                    DES_POSX = 8
                    DES_POSY = -19.5
                    MoveToPos((DES_POSX, DES_POSY))
                    DES_POSY = 0
                    MoveToPos((DES_POSX, DES_POSY))
                    DES_POSX = 0
                    MoveToPos((DES_POSX, DES_POSY))
                    Hotkey("E", 1)
                    sleep(60)

            # Leave game
            if event.unicode.upper() == "K":
                Hotkey("W", 5*.18)

            # Leave game
            if event.unicode.upper() == "J":
                Hotkey("W", 5*.20)

            # Leave game
            if event.unicode.upper() == "L":
                Hotkey("W", 5*1)

    pygame.display.update()
