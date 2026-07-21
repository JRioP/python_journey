class workoutTracker:
    def __init__(self, runner_name):
        self.runner_name = runner_name
        self.total_distance = 0
        self.total_calories = 0

    def add_workout(self, distance):
        self.total_distance += distance

    def add_calories(self, calories):
        self.total_calories += calories

    def show_progress(self):
        print(f"{self.runner_name} has logged a total of {self.total_distance} Km. He/she has burned a total of {self.total_calories} calories.")

new_runner = workoutTracker(str(input("Enter the runner's name: ").title()))
new_runner.add_workout(5)
new_runner.add_workout(3)
new_runner.add_calories(500)
new_runner.show_progress()