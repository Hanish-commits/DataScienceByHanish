"""A hands-on tour of Python operators.

Run this file to see arithmetic, assignment, comparison, logical, membership,
identity, bitwise, type-dependent, and precedence examples.
"""


def section(title):
    print(f"\n{title}")
    print("-" * len(title))


print("=" * 68)
print("PYTHON OPERATORS: A HANDS-ON TOUR")
print("=" * 68)


# 1. Arithmetic operators.
section("1. ARITHMETIC")
a = 17
b = 5
print(f"a + b  = {a + b}")
print(f"a - b  = {a - b}")
print(f"a * b  = {a * b}")
print(f"a / b  = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b  = {a % b}")
print(f"a ** 2 = {a ** 2}")
print(f"-7 // 2 = {-7 // 2} (floor goes toward negative infinity)")


# 2. Assignment and augmented assignment.
section("2. ASSIGNMENT")
score = 80
score += 5
print(f"After score += 5: {score}")
score -= 2
print(f"After score -= 2: {score}")
score *= 2
print(f"After score *= 2: {score}")
score //= 10
print(f"After score //= 10: {score}")


# 3. Comparisons produce Boolean values.
section("3. COMPARISONS")
score = 85
print(f"score == 85: {score == 85}")
print(f"score != 100: {score != 100}")
print(f"score >= 60: {score >= 60}")
print(f"0 <= score <= 100: {0 <= score <= 100}")


# 4. Logical operators combine conditions.
section("4. LOGICAL OPERATORS")
submitted = True
is_weekend = False
is_holiday = True
print(f"passing AND submitted: {score >= 60 and submitted}")
print(f"weekend OR holiday: {is_weekend or is_holiday}")
print(f"NOT submitted: {not submitted}")

# Short circuiting skips the unsafe right side when the string is empty.
name = ""
print(f"Empty name passes safe check? {name != '' and name[0].isupper()}")


# 5. Membership checks.
section("5. MEMBERSHIP")
topics = ["Strings", "Lists", "Operators"]
print(f"'Lists' in topics: {'Lists' in topics}")
print(f"'Functions' not in topics: {'Functions' not in topics}")
print(f"'Py' in 'Python': {'Py' in 'Python'}")
student = {"name": "Ada", "score": 98}
print(f"'name' in student checks keys: {'name' in student}")
print(f"'Ada' in student.values(): {'Ada' in student.values()}")


# 6. Equality versus identity.
section("6. EQUALITY AND IDENTITY")
first = [1, 2]
second = first
third = [1, 2]
print(f"first == third (same contents): {first == third}")
print(f"first is second (same object): {first is second}")
print(f"first is third (different objects): {first is third}")
result = None
print(f"result is None: {result is None}")


# 7. Bitwise operators work on the integer's binary bits.
section("7. BITWISE OPERATORS")
x = 6  # binary 0110
y = 3  # binary 0011
print(f"x & y  = {x & y}")
print(f"x | y  = {x | y}")
print(f"x ^ y  = {x ^ y}")
print(f"x << 1 = {x << 1}")
print(f"x >> 1 = {x >> 1}")
print(f"~x     = {~x}")


# 8. The same operator can behave differently for different types.
section("8. OPERATORS AND TYPES")
print(f"4 + 5: {4 + 5}")
print(f"'4' + '5': {'4' + '5'}")
print(f"'ha' * 3: {'ha' * 3}")
print(f"Score with f-string: Score: {85}")


# 9. Precedence and parentheses.
section("9. PRECEDENCE")
print(f"2 + 3 * 4 = {2 + 3 * 4}")
print(f"(2 + 3) * 4 = {(2 + 3) * 4}")


# 10. Mini-project: calculate a study result.
section("10. MINI-PROJECT: STUDY RESULT")
score = 86
submitted = True
bonus_points = 5
completed_topics = ["Variables", "Data Types"]
final_score = min(100, score + bonus_points)
passed = final_score >= 60 and submitted
studied_data_types = "Data Types" in completed_topics
print(f"Final score: {final_score}")
print(f"Passed: {passed}")
print(f"Studied data types: {studied_data_types}")


print("\n" + "=" * 68)
print("TOUR COMPLETE — predict each expression before checking its result.")
print("=" * 68)
