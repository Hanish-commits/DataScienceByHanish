"""A hands-on tour of Python's built-in data types.

Run this file to see integers, floats, strings, Booleans, None, collections,
type inspection, mutability, and a mixed learner-record example.
"""


def section(title):
    print(f"\n{title}")
    print("-" * len(title))


print("=" * 68)
print("PYTHON DATA TYPES: A HANDS-ON TOUR")
print("=" * 68)


# 1. Similar-looking values can have different types.
section("1. VALUES AND THEIR TYPES")
values = [42, "42", 3.5, True, None]
for value in values:
    print(f"{value!r:<8} -> {type(value).__name__}")
print(f"isinstance(42, int): {isinstance(42, int)}")
print(f"isinstance('42', int): {isinstance('42', int)}")
print(f"isinstance(True, int): {isinstance(True, int)} (bool is a subclass of int)")


# 2. Integers and arithmetic.
section("2. INTEGERS")
lesson_count = 12
cookies = 17
people = 5
print(f"Lessons: {lesson_count}")
print(f"Cookies per person: {cookies // people}")
print(f"Cookies left over: {cookies % people}")


# 3. Floats and precision.
section("3. FLOATS")
average_score = 87.5
print(f"Average: {average_score}")
print(f"0.1 + 0.2 = {0.1 + 0.2}")
print("Binary floating-point cannot exactly represent every decimal fraction.")


# 4. Strings are text; quoted digits are not numeric values.
section("4. STRINGS")
print(f"Text concatenation: {'4' + '5'}")
print(f"Integer addition: {4 + 5}")
word = "Python"
print(f"Original: {word}; uppercase result: {word.upper()}; original still: {word}")


# 5. Booleans are comparison results and logical values.
section("5. BOOLEANS")
score = 85
is_passing = score >= 60
print(f"is_passing: {is_passing} ({type(is_passing).__name__})")
print(f"True and False: {True and False}")
print(f"not True: {not True}")


# 6. None represents an absent value; use identity comparison.
section("6. NONE")
quiz_result = None
print(f"Value: {quiz_result}; type: {type(quiz_result).__name__}")
print(f"Has no result yet? {quiz_result is None}")


# 7. Built-in collections have different purposes.
section("7. COLLECTION TYPES")
topics_list = ["Strings", "Lists", "Strings"]
fixed_point = (4, 7)
unique_topics = {"Strings", "Lists", "Strings"}
student = {"name": "Ada", "score": 98}
print(f"list: {topics_list}")
print(f"tuple: {fixed_point}")
print(f"set (duplicates collapse): {unique_topics}")
print(f"dict (key-value pairs): {student}")
print(f"empty set: {set()}; empty dictionary: {{}}")


# 8. Mutable versus immutable behavior.
section("8. MUTABILITY")
original = ["Strings"]
alias = original
alias.append("Data Types")
print(f"Original list after alias changes it: {original}")

word = "Python"
alias_word = word
alias_word = alias_word.upper()
print(f"Original string: {word}")
print(f"New uppercase string: {alias_word}")


# 9. Converting between common types.
section("9. BASIC TYPE CONVERSION")
number = int("12")
price = float("3.5")
label = str(42)
print(f"int('12') + 1 = {number + 1}")
print(f"float('3.5') = {price}")
print(f"str(42) = {label!r}")
print(f"bool('False') = {bool('False')} because the string is non-empty")


# 10. Inspect different fields in a record.
section("10. MINI-PROJECT: LEARNER RECORD")
learner = {
    "name": "Ada",
    "lessons_completed": 4,
    "average_score": 91.5,
    "is_active": True,
    "graduation_date": None,
    "topics": ["Variables", "Data Types"],
}
for field, value in learner.items():
    print(f"{field}: {value!r} ({type(value).__name__})")


print("\n" + "=" * 68)
print("TOUR COMPLETE — inspect types when a value behaves unexpectedly.")
print("=" * 68)
