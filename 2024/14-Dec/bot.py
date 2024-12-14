class Bot:
    def __init__(self, pos_x, pos_y, vel_x, vel_y, grid_size):
        self.pos = {"x": pos_x, "y": pos_y}
        self.vel = {"x": vel_x, "y": vel_y}
        self.grid_size = {"width": grid_size[0], "height": grid_size[1]}
        self.grid = [['O' for _ in range(self.grid_size["width"])] for _ in range(self.grid_size["height"])]

    def __repr__(self):
        return f"Bot({self.pos["x"]}, {self.pos["y"]}, {self.vel["x"]}, {self.vel["y"]}, ({self.grid_size["width"]},{self.grid_size["height"]}))"
    
    def print_grid(self):
        for row in self.grid:
            print("".join(row))
        print()