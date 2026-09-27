"""A hands-on tour of Python dictionaries.

Run this file with Python to see examples and results. It covers creating a
dictionary, reading and changing entries, common methods, looping, nested data,
comprehensions, and a small topic-tracker project.
"""

print("=" * 64)
print("PYTHON DICTIONARIES: A HANDS-ON TOUR")
print("=" * 64)


# 1. Creating dictionaries
# A dictionary maps each key (label) to a value (the information).
student = {"name": "Ada", "score": 98, "passed": True}
empty_dictionary = {}

print("\n1. CREATING DICTIONARIES")
print(f"Student record: {student}")
print(f"Empty dictionary: {empty_dictionary}")


# 2. Reading values
# Square brackets retrieve a value by key. get() handles a possibly missing key.
print("\n2. READING VALUES")
print(f"Student name: {student['name']}")
print(f"Score: {student['score']}")
print(f"Missing course, safely: {student.get('course', 'not set')}")

# 'in' checks keys. Use .values() when you want to search the values.
print(f"Is 'name' a key? {'name' in student}")
print(f"Is 'Ada' a key? {'Ada' in student}")
print(f"Is 'Ada' a value? {'Ada' in student.values()}")


# 3. Adding and changing entries
# Assigning a new key adds a pair; assigning an existing key replaces its value.
student["course"] = "Python"
student["score"] = 100
student.update({"level": "beginner", "passed": True})

print("\n3. ADDING AND CHANGING")
print(f"Updated student: {student}")


# 4. Removing entries
# pop() removes a key and returns its value. A default makes missing keys safe.
removed_score = student.pop("score")
student.pop("nickname", "no nickname")
del student["level"]

print("\n4. REMOVING ENTRIES")
print(f"Removed score: {removed_score}")
print(f"Student now: {student}")


# 5. Looping through keys, values, and pairs
profile = {"name": "Ada", "course": "Python", "status": "learning"}
print("\n5. LOOPING THROUGH A DICTIONARY")
print("Keys:")
for key in profile:
    print(f"- {key}")

print("Key and value pairs:")
for key, value in profile.items():
    print(f"- {key}: {value}")

print(f"Values view: {profile.values()}")


# 6. Nested dictionaries
# A value can be another dictionary. Follow each key to reach inner data.
students = {
    "Ada": {"score": 98, "course": "Python"},
    "Grace": {"score": 100, "course": "Computer Science"},
}

print("\n6. NESTED DICTIONARIES")
print(f"Ada's score: {students['Ada']['score']}")
print(f"Grace's course: {students['Grace']['course']}")
print(f"Safe lookup: {students.get('Linus', {}).get('score', 'not available')}")


# 7. Dictionary comprehension
# Build a dictionary by describing each key:value pair to create.
numbers = [1, 2, 3, 4]
squares = {number: number * number for number in numbers}
even_squares = {number: number * number for number in numbers if number % 2 == 0}

print("\n7. DICTIONARY COMPREHENSION")
print(f"Squares: {squares}")
print(f"Even-number squares: {even_squares}")


# 8. Mini-project: Python topic tracker
topics = {
    "Strings": "complete",
    "Lists": "complete",
    "Tuples": "in progress",
}

topics["Sets"] = "not started"
topics["Tuples"] = "complete"

print("\n8. MINI-PROJECT: PYTHON TOPIC TRACKER")
for topic, status in topics.items():
    print(f"- {topic}: {status}")

complete_count = list(topics.values()).count("complete")
print(f"Completed topics: {complete_count} of {len(topics)}")
print(f"Dictionaries status: {topics.get('Dictionaries', 'not started')}")


print("\n" + "=" * 64)
print("TOUR COMPLETE — try changing the examples and running the file again.")
print("=" * 64)
