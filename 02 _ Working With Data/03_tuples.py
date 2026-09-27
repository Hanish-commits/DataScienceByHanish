"""A hands-on tour of Python tuples.

Run this file with Python to see examples and results. It covers creating
 tuples, reading and slicing, immutability, packing and unpacking, common
operations, and a small Python-topic-card project.
"""

print("=" * 64)
print("PYTHON TUPLES: A HANDS-ON TOUR")
print("=" * 64)


# 1. Creating tuples
# Commas create tuples. Parentheses make the grouping easy to see.
language_info = ("Python", 3, "beginner")
point = (4, 7)
empty = ()
one_item = ("Python",)  # the comma is essential for a one-item tuple
not_a_tuple = ("Python")

print("\n1. CREATING TUPLES")
print(f"Language info: {language_info}")
print(f"Point: {point}")
print(f"Empty tuple: {empty}")
print(f"One-item tuple: {one_item} (type: {type(one_item).__name__})")
print(f"Parenthesized string: {not_a_tuple} (type: {type(not_a_tuple).__name__})")


# 2. Length, indexing, and membership
# Positive indexes count from the front starting at zero.
# Negative indexes count from the end: -1 is last, -2 is second-to-last.
languages = ("Python", "Java", "Ruby", "Go")
print("\n2. READING TUPLES")
print(f"Length: {len(languages)}")
print(f"First item [0]: {languages[0]}")
print(f"Second item [1]: {languages[1]}")
print(f"Last item [-1]: {languages[-1]}")
print(f"Second-to-last [-2]: {languages[-2]}")
print("Position map:")
print(f"  items:    {languages}")
print("  indexes:  0      1      2      3")
print("  negative: -4     -3     -2     -1")
print(f"Is Java in the tuple? {'Java' in languages}")


# 3. Slicing
# A slice includes its start and stops before its stop position.
# Negative indexes work in slices too. Slicing creates a new tuple.
lessons = ("Strings", "Lists", "Tuples", "Loops", "Functions")
print("\n3. SLICING")
print(f"All lessons: {lessons}")
print(f"Lessons [1:4]: {lessons[1:4]}")
print("  starts at index 1; stops before index 4")
print(f"Last two [-2:]: {lessons[-2:]}")
print(f"Everything except last [:-1]: {lessons[:-1]}")
print(f"Every second [::2]: {lessons[::2]}")
print(f"Reversed [::-1]: {lessons[::-1]}")


# 4. Immutability
# Tuple item positions cannot be reassigned. Build another tuple instead.
course = ("Python", "Lists", "Tuples")
new_course = course[:2] + ("Dictionaries",)
print("\n4. IMMUTABILITY")
print(f"Original tuple: {course}")
print(f"New tuple:      {new_course}")
# course[1] = "Loops"  # Uncommenting this raises TypeError.

# A tuple may contain a mutable object. The tuple slot is fixed, but the
# inner list can still be changed.
record = ("Study plan", ["Strings", "Lists"])
record[1].append("Tuples")
print(f"Tuple containing a changed inner list: {record}")


# 5. Packing and unpacking
# Packing puts comma-separated values into a tuple.
student = "Ada", 36, "Python learner"

# Unpacking assigns each tuple item to a corresponding name.
name, age, description = student
print("\n5. PACKING AND UNPACKING")
print(f"Packed tuple: {student}")
print(f"Unpacked values: name={name}, age={age}, description={description}")

# Starred unpacking gathers the remaining values into a list.
first, *middle, last = ("Strings", "Lists", "Tuples", "Loops")
print(f"First: {first}; middle: {middle}; last: {last}")

# Python can swap names using unpacking.
first_topic = "Strings"
second_topic = "Lists"
first_topic, second_topic = second_topic, first_topic
print(f"After swapping: first={first_topic}, second={second_topic}")


# 6. Tuple methods and operations
scores = (88, 92, 88, 75)
print("\n6. METHODS AND OPERATIONS")
print(f"Scores: {scores}")
print(f"Number of 88s: {scores.count(88)}")
print(f"Position of 92: {scores.index(92)}")
print(f"Does 75 appear? {75 in scores}")
print(f"Add one item by combining tuples: {scores + (100,)}")
print(f"Repeat tuple: {('Review', 'Practice') * 2}")


# 7. Looping through tuples
print("\n7. LOOPING")
for language in ("Python", "Java", "Ruby"):
    print(f"Learning: {language}")

# A tuple of pairs can be unpacked right in the loop.
student_scores = (("Ada", 98), ("Grace", 100))
for student_name, score in student_scores:
    print(f"{student_name}: {score}")


# 8. Mini-project: Python topic cards
# Each pair stores a topic and its description. The outer tuple keeps this
# prepared set of cards together as one fixed collection.
topic_cards = (
    ("Strings", "Work with text"),
    ("Lists", "Store an ordered group that can change"),
    ("Tuples", "Group ordered values that stay fixed"),
)

print("\n8. MINI-PROJECT: PYTHON TOPIC CARDS")
for number, (topic, definition) in enumerate(topic_cards, start=1):
    print(f"{number}. {topic}: {definition}")

first_topic, first_definition = topic_cards[0]
print(f"First card is about {first_topic}: {first_definition}")


print("\n" + "=" * 64)
print("TOUR COMPLETE — try changing the examples and running the file again.")
print("=" * 64)
