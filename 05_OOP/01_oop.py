"""A hands-on tour of object-oriented programming in Python.

Run this file to see classes, objects, attributes, methods, class attributes,
encapsulation conventions, inheritance, composition, special methods, and a
small study-tracker project.
"""

from dataclasses import dataclass

print("=" * 68)
print("PYTHON OOP: A HANDS-ON TOUR")
print("=" * 68)


# 1. A minimal class and an instance.
class EmptyExample:
    pass


empty_object = EmptyExample()
print("\n1. CLASS AND OBJECT")
print(f"Created an instance of: {type(empty_object).__name__}")


# 2. __init__ sets up each new object; self is the current instance.
class StudyTopic:
    category = "Python topic"  # class attribute shared by these instances

    def __init__(self, name, status="not started"):
        self.name = name        # instance attribute
        self.status = status    # each object gets its own status

    def report(self):
        return f"{self.name}: {self.status}"

    def mark_complete(self):
        self.status = "complete"

    @classmethod
    def not_started(cls, name):
        # cls allows inherited versions to create the child class's type.
        return cls(name)

    def __str__(self):
        return self.report()


strings = StudyTopic("Strings", "complete")
loops = StudyTopic("Loops", "in progress")
print("\n2. INITIALIZATION, ATTRIBUTES, AND METHODS")
print(strings.name)
print(strings.report())
print(loops.report())
print(f"Shared category: {strings.category}")


# 3. Each instance keeps its own state.
loops.mark_complete()
print("\n3. INSTANCE STATE")
print(f"Loops after update: {loops.status}")
print(f"Strings remains: {strings.status}")
print(f"Readable object display: {loops}")


# 4. Encapsulation: validate updates through a method.
class QuizScore:
    def __init__(self, score):
        self._score = score  # leading underscore means internal by convention

    def update(self, new_score):
        if 0 <= new_score <= 100:
            self._score = new_score
            return True
        return False

    def report(self):
        return f"Score: {self._score}"


print("\n4. CONTROLLED UPDATES")
quiz = QuizScore(80)
print(quiz.update(95), quiz.report())
print(quiz.update(150), quiz.report())


# 5. Inheritance: PracticeTopic is a kind of Topic.
class Topic:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"Topic: {self.name}"


class PracticeTopic(Topic):
    def __init__(self, name, exercise_count):
        super().__init__(name)  # initialize the inherited name attribute
        self.exercise_count = exercise_count

    def describe(self):  # override the parent's method
        return f"{self.name}: {self.exercise_count} practice exercises"


print("\n5. INHERITANCE AND OVERRIDING")
practice = PracticeTopic("Loops", 8)
print(practice.describe())


# 6. Polymorphism: different classes can respond to the same method call.
class VideoLesson:
    def describe(self):
        return "Watch the lesson video"


class CodingLesson:
    def describe(self):
        return "Complete the coding exercise"


print("\n6. POLYMORPHISM")
for lesson in [VideoLesson(), CodingLesson()]:
    print(lesson.describe())


# 7. Class and static methods.
class TopicTools:
    @staticmethod
    def is_valid_status(status):
        # No instance or class is passed automatically to this helper.
        return status in {"not started", "in progress", "complete"}


print("\n7. CLASS AND STATIC METHODS")
default_topic = StudyTopic.not_started("Dictionaries")
print(default_topic.report())
print(f"Is 'complete' a valid status? {TopicTools.is_valid_status('complete')}")


# 8. Properties can validate values while keeping attribute-style access.
class ValidatedQuizScore:
    def __init__(self, score):
        self.score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not 0 <= value <= 100:
            raise ValueError("score must be between 0 and 100")
        self._score = value


print("\n8. PROPERTY VALIDATION")
validated = ValidatedQuizScore(85)
validated.score = 95
print(f"Validated score: {validated.score}")


# 9. A dataclass supplies common data-class methods automatically.
@dataclass
class TopicCard:
    name: str
    status: str = "not started"


print("\n9. DATACLASS")
print(TopicCard("OOP", "in progress"))


# 10. Composition: a Course has Lesson objects.
class Lesson:
    def __init__(self, title, complete=False):
        self.title = title
        self.complete = complete


class Course:
    def __init__(self, title, lessons):
        self.title = title
        self.lessons = lessons

    def completed_count(self):
        return sum(lesson.complete for lesson in self.lessons)


print("\n10. COMPOSITION")
lesson_list = [Lesson("Strings", True), Lesson("Lists"), Lesson("OOP", True)]
course = Course("Python Basics", lesson_list)
print(f"{course.title}: {course.completed_count()} lessons complete")


# 11. Special methods make objects work naturally with Python.
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)


playlist = Playlist(["Song A", "Song B"])
print("\n11. SPECIAL METHODS")
print(f"Playlist has {len(playlist)} songs")


# 12. Mini-project: study tracker objects.
topics = [
    StudyTopic("Strings", "complete"),
    StudyTopic("Lists", "in progress"),
    StudyTopic("OOP"),
]
topics[1].mark_complete()

print("\n12. MINI-PROJECT: STUDY TRACKER")
for topic in topics:
    print(topic.report())


print("\n" + "=" * 68)
print("TOUR COMPLETE — create a class for another concept you are learning.")
print("=" * 68)
