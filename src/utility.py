from definitions import *
from configuration import *


def valid_color(color):
    return color != None and color >= 1 and color <= 6
    
    
def valid_direction(direction):
    return direction != None and direction >= 1 and direction <= 4
    
    
def in_bounds(coordinate):
    return coordinate != None and coordinate >= 1 and coordinate <= Configuration.grid_length
    

def valid_point(point):
    return point != None and in_bounds(point.x) and in_bounds(point.y)
    
    
def print_debug(message):
    if Configuration.debug:
        print "[DEBUG] %s" % (message)
        
        
def print_benchmark(message):
    if Configuration.benchmark:
        print "[TIMER] %s" % (message)


def print_calibrate(message):
    if Configuration.calibrating:
        print "[CALIBRATE] %s" % (message)


# Returns the powerset of the current list
def powerset(seq):
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item


# Given a Point and its direction, returns the other Point that it needs to be swapped with
def get_swap_point(point, direction):
    if not valid_point(point):
        return None
        
    if direction == Direction.left:     return Point(point.x - 1, point.y)
    elif direction == Direction.right:  return Point(point.x + 1, point.y)
    elif direction == Direction.up:     return Point(point.x, point.y - 1)
    elif direction == Direction.down:   return Point(point.x, point.y + 1)
    return None


# Given a Board object, returns a 2D list of the textual representations of the colors
def board_to_text(board):
    if board == None:
        return None
        
    return [[board[(x + 1, y + 1)].name if board[(x + 1, y + 1)] != None else "unknown" for x in range(board.size)] for y in range(board.size)]
    
    
# Given a Match object, returns a list of Points in that match
def get_points_from_match(match):
    result = []
    vertical_multiplier = 0
    horizontal_multiplier = 0
    
    if match.orientation == Orientation.vertical:
        vertical_multiplier = 1
    else:
        horizontal_multiplier = 1
    
    for c in range(match.length):
        result.append(Point(match.point.x + (horizontal_multiplier * c), match.point.y + (vertical_multiplier * c)))
        
    return result