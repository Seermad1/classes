def change_name(name):
    print(name)


class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.track = tracks
        self.score = score
        pass

    def change_age(self, age):
        print(int(age))
    def add_track(self, track):
        self.track.append(track)
        print(self.track)
    def get_score(self):
        print(float(self.score))



Bob = Student("Bob", 26, ["FE", "BE"], 20.90)

# Expected methods
change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()