class MonkeyBananaProblem:
    def __init__(self):
        self.monkey = "door"
        self.box = "window"
        self.banana = "ceiling"
        self.has_banana = False

    def display_state(self):
        print(f"Monkey: {self.monkey}, Box: {self.box}, Has Banana: {self.has_banana}")

    def move_to_box(self):
        print("Monkey moves to the box.")
        self.monkey = self.box
        self.display_state()

    def push_box(self):
        print("Monkey pushes the box under the bananas.")
        self.box = "under the bananas"
        self.monkey = self.box
        self.display_state()

    def climb_box(self):
        print("Monkey climbs on the box.")
        self.display_state()

    def grab_banana(self):
        print("Monkey grabs the bananas!")
        self.has_banana = True
        self.display_state()

    def solve(self):
        print("\n--- Solving Monkey and Banana Problem ---\n")
        self.display_state()
        self.move_to_box()
        self.push_box()
        self.climb_box()
        self.grab_banana()
        print("\n✅ Goal Achieved: Monkey has the bananas!\n")


# Run the program
problem = MonkeyBananaProblem()
problem.solve()
