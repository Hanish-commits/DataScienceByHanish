"""A hands-on tour of Python variables and assignment.

Run this file to see variable names, assignment, reassignment, augmented
assignment, naming conventions, references, mutability, unpacking, and a small
study-progress summary.
"""


def section(title):
    print(f"\n{title}")
    print("-" * len(title))


print("=" * 68)
print("PYTHON VARIABLES: A HANDS-ON TOUR")
print("=" * 68)


# 1. A variable name refers to a value.
section("1. NAMES AND VALUES")
learner = "Ada"
score = 98
print(f"learner refers to {learner!r}")
print(f"score refers to {score}")


# 2. Assignment evaluates the right side before binding the result to the name.
section("2. ASSIGNMENT AND EXPRESSIONS")
lesson_count = 4
remaining = 10 - lesson_count
print(f"Completed: {lesson_count}")
print(f"Remaining: 10 - {lesson_count} = {remaining}")


# 3. Reassignment makes the name refer to a new value.
section("3. REASSIGNMENT")
status = "not started"
print(status)
status = "in progress"
print(status)
status = "complete"
print(status)

# A name can refer to different types, though consistent meaning is clearer.
result = 42
print(f"result is {result!r}, type {type(result).__name__}")
result = "forty-two"
print(f"result is now {result!r}, type {type(result).__name__}")


# 4. Augmented assignment updates a value using its current value.
section("4. UPDATING VALUES")
points = 10
points += 5
print(f"After points += 5: {points}")
points -= 2
print(f"After points -= 2: {points}")
points *= 3
print(f"After points *= 3: {points}")


# 5. Clear variable names use snake_case and describe the information.
section("5. NAMING VARIABLES")
student_name = "Grace"
quiz_score = 100
number_of_lessons = 12
print(student_name, quiz_score, number_of_lessons)
print("Names are case-sensitive: score and Score are different names.")


# 6. Assignment creates another reference; it does not copy a mutable list.
section("6. SHARED REFERENCES")
first_list = ["Strings", "Lists"]
second_list = first_list
second_list.append("Variables")
print(f"first_list:  {first_list}")
print(f"second_list: {second_list}")
print("Both names refer to the same list object.")

# .copy() creates a separate shallow copy for a flat list.
original_topics = ["Strings", "Lists"]
separate_topics = original_topics.copy()
separate_topics.append("Variables")
print(f"Original: {original_topics}")
print(f"Copy:     {separate_topics}")


# 7. Multiple assignment unpacks values into matching names.
section("7. MULTIPLE ASSIGNMENT AND UNPACKING")
name, score = "Ada", 98
print(f"name={name}; score={score}")

first_topic = "Strings"
second_topic = "Lists"
first_topic, second_topic = second_topic, first_topic
print(f"After swapping: first={first_topic}; second={second_topic}")


# 8. Uppercase names signal constants by convention, not enforcement.
section("8. CONSTANT-STYLE NAMES")
MAX_SCORE = 100
print(f"Maximum score by convention: {MAX_SCORE}")


# 9. Mini-project: update a study progress summary.
section("9. MINI-PROJECT: STUDY PROGRESS")
learner_name = "Ada"
total_lessons = 10
completed_lessons = 4
remaining_lessons = total_lessons - completed_lessons
print(f"Learner: {learner_name}")
print(f"Completed: {completed_lessons} of {total_lessons}")
print(f"Remaining: {remaining_lessons}")

completed_lessons += 1
remaining_lessons = total_lessons - completed_lessons
print(f"After one more lesson: {completed_lessons} complete, {remaining_lessons} remaining")


print("\n" + "=" * 68)
print("TOUR COMPLETE — change values and follow how each name is updated.")
print("=" * 68)
