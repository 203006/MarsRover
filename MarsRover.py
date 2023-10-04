from abc import ABC, abstractmethod

# Command Pattern: Define commands as objects
class Command(ABC):
    @abstractmethod
    def execute(self, rover):
        pass

# Concrete Commands
class MoveForward(Command):
    def execute(self, rover):
        rover.move_forward()

class TurnLeft(Command):
    def execute(self, rover):
        rover.turn_left()

class TurnRight(Command):
    def execute(self, rover):
        rover.turn_right()

# Mars Rover class
class MarsRover:
    def __init__(self, x, y, direction, grid, obstacles):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid = grid
        self.obstacles = obstacles
        self.command_map = {
            'M': MoveForward(),
            'L': TurnLeft(),
            'R': TurnRight()
        }

    def execute_commands(self, commands):
        for command in commands:
            self.command_map.get(command, NullCommand()).execute(self)

    def move_forward(self):
        new_x, new_y = self.calculate_new_position()
        if self.is_valid_move(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def calculate_new_position(self):
        if self.direction == 'E':
            return self.x, self.y + 1
        elif self.direction == 'W':
            return self.x, self.y - 1
        elif self.direction == 'S':
            return self.x + 1, self.y
        elif self.direction == 'N':
            return self.x - 1, self.y

    def is_valid_move(self, new_x, new_y):
        if (new_x, new_y) in self.obstacles:
            return False
        return 0 <= new_x < self.grid[0] and 0 <= new_y < self.grid[1]

    def turn_left(self):
        direction_map = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
        self.direction = direction_map.get(self.direction, self.direction)

    def turn_right(self):
        direction_map = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        self.direction = direction_map.get(self.direction, self.direction)

    def get_position(self):
        return self.x, self.y, self.direction

# Null Object Pattern: A command object that does nothing
class NullCommand(Command):
    def execute(self, rover):
        pass

# Example usage
if __name__ == "__main__":
    grid = (10, 10)
    obstacles = [(2, 2), (3, 5)]
    rover = MarsRover(0, 0, 'E', grid, obstacles)
    commands = input("enter the commands list");
    rover.execute_commands(commands)
    final_position = rover.get_position()
    print(f"Final Position: {final_position}")










