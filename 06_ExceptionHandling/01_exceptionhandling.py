"""A hands-on tour of Python exception handling.

Run this file to see try/except/else/finally, common exceptions, raising and
re-raising errors, assertions, custom exceptions, and safe input handling.
"""

print("=" * 68)
print("PYTHON EXCEPTION HANDLING: A HANDS-ON TOUR")
print("=" * 68)


# 1. Catch a specific conversion error.
print("\n1. TRY AND EXCEPT")
text = "twenty"
try:
    age = int(text)
except ValueError:
    print(f"Cannot convert {text!r} to a whole number.")


# 2. else runs only when try succeeds.
print("\n2. EXCEPT AND ELSE")
for text in ["42", "not a number"]:
    try:
        number = int(text)
    except ValueError:
        print(f"Invalid number: {text!r}")
    else:
        print(f"Converted successfully: {number}")


# 3. Different exception types can have different handlers.
print("\n3. MULTIPLE EXCEPTION TYPES")
for text in ["5", "0", "five"]:
    try:
        number = int(text)
        result = 100 / number
    except ValueError:
        print(f"{text!r}: enter a whole number")
    except ZeroDivisionError:
        print("0: the number must not be zero")
    else:
        print(f"{text!r}: result is {result}")


# 4. Capture the exception object for its detail.
print("\n4. EXCEPTION MESSAGE")
try:
    int("four")
except ValueError as error:
    print(f"Conversion detail: {error}")


# 5. finally runs whether the operation succeeds or fails.
print("\n5. FINALLY")
for should_fail in [False, True]:
    try:
        if should_fail:
            raise RuntimeError("demonstration problem")
        print("Work completed")
    except RuntimeError as error:
        print(f"Handled: {error}")
    finally:
        print("Cleanup step always runs")


# For files, a with statement is usually the clearest cleanup tool.
print("\n6. CONTEXT MANAGER")
try:
    with open("this_file_does_not_exist.txt", encoding="utf-8") as file:
        contents = file.read()
except FileNotFoundError:
    print("The example file was not found; the program continues.")


# 7. Raise a specific exception when a value violates a rule.
def percentage(part, whole):
    if whole == 0:
        raise ValueError("whole must not be zero")
    return part / whole * 100


print("\n7. RAISING AN EXCEPTION")
print(f"25 of 50 is {percentage(25, 50):.0f}%")
try:
    percentage(10, 0)
except ValueError as error:
    print(f"Cannot calculate: {error}")


# 8. Re-raise after adding context when this code cannot recover.
print("\n8. RE-RAISING")
try:
    try:
        int("invalid")
    except ValueError:
        print("This layer cannot recover, so it passes the exception upward.")
        raise
except ValueError:
    print("A higher-level handler received the ValueError.")


# 9. Assertions express internal assumptions, not user-input validation.
print("\n9. ASSERTION")
validated_score = 85
assert 0 <= validated_score <= 100, "score should already be validated"
print("Internal score assumption holds.")


# 10. Custom exceptions let callers handle a domain-specific problem.
class TopicNotFoundError(Exception):
    """Raised when a topic is absent from the study tracker."""


def get_status(progress, topic):
    if topic not in progress:
        raise TopicNotFoundError(f"No progress recorded for {topic!r}")
    return progress[topic]


print("\n10. CUSTOM EXCEPTION")
progress = {"Strings": "complete"}
try:
    print(get_status(progress, "Dictionaries"))
except TopicNotFoundError as error:
    print(error)


# 11. Safe score calculator mini-project.
def read_score(text):
    try:
        score = int(text)
    except ValueError:
        return None, "Enter a whole number, such as 85."
    else:
        if not 0 <= score <= 100:
            return None, "Score must be from 0 to 100."
        return score, f"Score accepted: {score}"


print("\n11. MINI-PROJECT: SAFE SCORE CALCULATOR")
for answer in ["85", "many", "120"]:
    score, message = read_score(answer)
    print(message)


print("\n" + "=" * 68)
print("TOUR COMPLETE — try changing inputs and observing the handler used.")
print("=" * 68)
