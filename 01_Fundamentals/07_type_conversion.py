"""A hands-on tour of Python type conversion.

Run this file to see numeric, text, Boolean, and collection conversions,
conversion errors, safe parsing, and a small score-report project.
"""


def section(title):
    print(f"\n{title}")
    print("-" * len(title))


print("=" * 68)
print("PYTHON TYPE CONVERSION: A HANDS-ON TOUR")
print("=" * 68)


# 1. Convert valid numeric text.
section("1. TEXT TO NUMBERS")
lesson_text = "12"
lessons = int(lesson_text)
price_text = "3.50"
price = float(price_text)
print(f"{lesson_text!r} is {type(lesson_text).__name__}; int(...) gives {lessons}")
print(f"{price_text!r} converts to float {price}")
print(f"Lessons plus one: {lessons + 1}")


# 2. int(float) truncates toward zero; round() rounds to a nearby integer.
section("2. TRUNCATION VERSUS ROUNDING")
print(f"int(3.9): {int(3.9)}")
print(f"int(-3.9): {int(-3.9)}")
print(f"round(3.9): {round(3.9)}")
print(f"-7 // 2: {-7 // 2} (floor division rounds down)")


# 3. Convert values to text for joining or display.
section("3. VALUES TO TEXT")
score = 85
score_text = str(score)
print(f"str(score): {score_text!r} ({type(score_text).__name__})")
print("Join with str(): " + "Score: " + str(score))
print(f"Usually clearer f-string: Score: {score}")


# 4. bool() uses truthiness; it does not parse text like True/False.
section("4. BOOLEAN CONVERSION")
for value in [0, 5, "", "Python", "False", None, [], [0]]:
    print(f"bool({value!r}) = {bool(value)}")

answer = " YES ".strip().lower()
wants_to_continue = answer in {"yes", "y"}
print(f"Parsed yes/no text explicitly: {wants_to_continue}")


# 5. Convert among collection types.
section("5. COLLECTION CONVERSIONS")
print(f"list('cat'): {list('cat')}")
print(f"tuple([1, 2, 3]): {tuple([1, 2, 3])}")
print(f"set([1, 1, 2, 3]): {set([1, 1, 2, 3])}")
pairs = [("name", "Ada"), ("score", 98)]
print(f"dict(pairs): {dict(pairs)}")


# 6. Invalid conversions raise errors; catch the expected ValueError.
section("6. HANDLING INVALID CONVERSION")
for text in ["42", "twelve", "3.5"]:
    try:
        number = int(text)
    except ValueError:
        print(f"Cannot convert {text!r} directly to int.")
    else:
        print(f"Converted {text!r} to {number}.")


# 7. Mini-project: parse, validate, and format a score.
section("7. MINI-PROJECT: SCORE REPORT")
for score_text in ["87", "eighty-seven", "120"]:
    try:
        score = int(score_text)
    except ValueError:
        print(f"{score_text!r}: score must be a whole number.")
    else:
        if not 0 <= score <= 100:
            print(f"{score_text!r}: score must be between 0 and 100.")
        else:
            progress = score / 100
            print(f"Score: {score}; progress: {progress:.0%}")


print("\n" + "=" * 68)
print("TOUR COMPLETE — conversion may fail or discard information; choose carefully.")
print("=" * 68)
