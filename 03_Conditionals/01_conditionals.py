"""A hands-on tour of Python conditionals: if, elif, and else.

Run this file with Python to see examples of comparisons, Boolean logic,
truthiness, membership, nesting, independent checks, and a study-progress
mini-project.
"""

print("=" * 68)
print("PYTHON CONDITIONALS: A HANDS-ON TOUR")
print("=" * 68)


# 1. A basic if
# The indented body runs only when its condition is True.
has_homework = True
print("\n1. IF")
if has_homework:
    print("Set aside time to study.")


# 2. if and else choose one of two paths.
score = 54
print("\n2. IF AND ELSE")
if score >= 60:
    print("Passed")
else:
    print("Not passed yet")


# 3. An elif chain checks from top to bottom and runs the first match.
score = 84
print("\n3. IF, ELIF, ELSE")
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "Keep practicing"
print(f"Score {score} earns: {grade}")


# 4. Comparison operators produce True or False.
print("\n4. COMPARISONS")
score = 80
print(f"score == 80: {score == 80}")
print(f"score != 100: {score != 100}")
print(f"score >= 80: {score >= 80}")
print(f"0 <= score <= 100: {0 <= score <= 100}")


# 5. Boolean operators combine or reverse conditions.
submitted = True
is_weekend = False
is_holiday = True
is_complete = False
print("\n5. AND, OR, NOT")
print(f"Passing and submitted: {score >= 60 and submitted}")
print(f"Weekend or holiday: {is_weekend or is_holiday}")
print(f"Not complete: {not is_complete}")


# 6. Truthiness: empty collections and empty text are falsey.
name = "Ada"
names = []
print("\n6. TRUTHINESS")
if name:
    print(f"Hello, {name}!")
if not names:
    print("No names have been added yet.")

# Use an identity check to tell None apart from a valid value like zero.
score = 0
if score is not None:
    print("A score was provided, even though it is zero.")


# 7. Membership and identity checks.
completed = ["Strings", "Tuples"]
result = None
print("\n7. MEMBERSHIP AND IDENTITY")
if "Lists" in completed:
    print("Lists are complete.")
else:
    print("Lists are still on the plan.")
if result is None:
    print("There is no result yet.")


# 8. Nested conditionals: the inner decision happens only after sign-in.
logged_in = True
is_admin = False
print("\n8. NESTED CONDITIONALS")
if logged_in:
    if is_admin:
        print("Open the admin dashboard.")
    else:
        print("Open the standard dashboard.")
else:
    print("Please sign in.")


# 9. Independent if statements can both run; elif selects only one branch.
score = 95
print("\n9. INDEPENDENT IF STATEMENTS")
if score >= 60:
    print("Passed")
if score >= 90:
    print("Excellent")


# 10. A conditional expression chooses one value.
score = 72
result = "pass" if score >= 60 else "try again"
print("\n10. CONDITIONAL EXPRESSION")
print(f"Result: {result}")


# 11. Mini-project: choose a helpful study message.
topic = "Lists"
score = 78
completed = ["Strings", "Tuples"]

print("\n11. MINI-PROJECT: STUDY PROGRESS MESSAGE")
if topic in completed:
    message = f"You have already completed {topic}."
elif score >= 80:
    message = f"Great work on {topic}! You are ready to move on."
elif score >= 60 and topic:
    message = f"You passed {topic}. A little more practice will help."
else:
    message = f"Keep practicing {topic} before moving on."
print(message)


print("\n" + "=" * 68)
print("TOUR COMPLETE — change the values and predict the branch before running.")
print("=" * 68)
