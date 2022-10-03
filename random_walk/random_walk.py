import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from random import choice

class RandomWalk():
    """Class for generation random walk."""

    def __init__(self, num_points=5000):
        """Initialize walks atributes."""
        self.num_point = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Determine the direction and distance for a step."""
        # Определяем направление и шаг.

        num_direction = choice([1, -1])
        num_distance = choice(list(range(1, 11)))
        num_step = num_direction * num_distance

        return num_step

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_point:

            # Decide which direction to go and how far to go in that direction.

            x_step = self.get_step()
            y_step = self.get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)