class DailyTaskTwo:
    def __init__(self):
        self.people = []  # Pluralized for clarity

    def add_person(self, person):
        self.people.append(person)

    def check_duplicates(self):
        seen = set()
        unique_people = []
        
        for person in self.people:
            if person in seen:
                print(f"Duplicate found: {person}")
            else:
                seen.add(person)
                unique_people.append(person)
                
        self.people = unique_people

    def sort_person_list(self):
        self.people.sort()

# This will now correctly strip ANY number of duplicates!
person = DailyTaskTwo()
person.add_person("Alice")
person.add_person("Alice")
person.add_person("Alice")
person.add_person("Alice")
person.add_person("Alice")
person.add_person("Bob")
person.add_person("Bob")
person.add_person("Bob")
person.check_duplicates()
print(f"Final list: {person.people}")