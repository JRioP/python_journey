class DailyTaskTwoSecond:
    def __init__(self):
        self.things = []

    def add_object(self, obj):
        self.things.append(obj)

    def check_duplicates(self):
        seen = set()
        unique_things = []

        for obj in self.things:
            if obj in seen:
                print(f"Duplicate found: {obj}")
            else:
                seen.add(obj)
                unique_things.append(obj)

        self.things = unique_things

    def sort_object_list(self):
        self.things.sort()

