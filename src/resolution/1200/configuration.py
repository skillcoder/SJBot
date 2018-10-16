from definitions import *

"""
Grid positions for 1440p:
    (1740, 134) to (2508, 902)
"""

class Configuration:
    screen_width = 1920         # Width of computer screen
    screen_height = 1200        # Height of computer screen

    offset_x = 1237             # X offset of grid
    offset_y = 112              # Y offset of grid
    grid_size = 640             # Size of grid (square)
    gem_size = 80               # Size of gem (square)
    grid_length = 8             # Number of gems from top-bottom or left-right

    idle_x = 20                # X offset for idle position
    idle_y = 20                 # Y offset for idle position

    tolerance = 4               # RGB tolerance range for gem color detection
    skip = 5                    # Percentage (100 / skip %) of pixels averaged to determine gem color (higher = slower, but more accurate)
    unknown_threshold = 2      # Max number of unknown gems allowed before converting board

    chain_delay = 0.25         # Number of seconds to delay for each chain level above one (1.36 for update one chain)
    one_by_one = False          # Make one turn before update board (1.36 and true for FOR THE SWARM)

    # Not implemented
    look_ahead_count = 20       # Look ahead X number of moves to find the best move
    powerset_limit = 20         # Maximum number of moves we can calculate powerset for without hindering performance

    enabled = False             # Runtime flag -- run the bot algorithm?
    debug = False               # Runtime flag -- show debug output
    benchmark = False           # Runtime flag -- show performance data
    calibrating = False         # Runtime flag -- show average RGB values when converting image to map
    show_turns = True           # Show moves in log


    # Color mapping table -- maps skip -> ([color -> average rgb value])
    color_table = {
        5 : {
            Color.white  : (15, 15, 14),
            Color.red    : (24, 10, 6),
            Color.blue   : (13, 28, 34),
            Color.purple : (15, 8, 15),
            Color.green  : (15, 26, 8),
            Color.yellow : (23, 22, 10)
        }
    }
    
    
    # Points mapping table -- maps match_length -> points
    points_table = {
        3 : 30,
        4 : 60,
        5 : 120,
        6 : 240,
        7: 480,
        8: 960
    }