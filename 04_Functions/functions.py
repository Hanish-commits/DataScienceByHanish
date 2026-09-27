"""A hands-on tour of Python functions.

Run this file with Python to see examples and results. It covers function
basics, arguments, return values, defaults, local/global scope, *args/**kwargs,
lambdas, map/filter/reduce, useful built-ins, and a study helper.
"""

from functools import reduce

print("=" * 68)
print("PYTHON FUNCTIONS: A HANDS-ON TOUR")
print("=" * 68)


# 1. Define and call a function
# def creates the function; writing its name with () calls (runs) it.
def say_hello():
    print("Hello from Python!")


print("\n1. DEFINING AND CALLING")
say_hello()
say_hello()


# 2. Parameters and arguments
# name is a parameter in the definition; "Ada" is an argument in the call.
def greet(name):
    print(f"Hello, {name}!")


def introduce(name, language):
    print(f"{name} is learning {language}.")


print("\n2. PARAMETERS AND ARGUMENTS")
greet("Ada")
greet("Grace")
introduce("Ada", "Python")


# 3. Return values
# return sends a result back to the caller; print only displays it.
def add(first, second):
    return first + second


def show_total(first, second):
    print(first + second)


def calculate_total(first, second):
    return first + second


print("\n3. RETURNING A VALUE")
total = add(4, 7)
print(f"Saved result: {total}; doubled: {total * 2}")
visible_result = show_total(2, 3)
usable_result = calculate_total(2, 3)
print(f"show_total returned: {visible_result}")  # None
print(f"calculate_total returned: {usable_result}")


# 4. Early return and multiple results
def describe_score(score):
    if score < 0:
        return "Score cannot be negative."
    return f"Score: {score}"


def min_and_max(numbers):
    return min(numbers), max(numbers)  # a tuple of two results


print("\n4. EARLY RETURN AND MULTIPLE RESULTS")
print(describe_score(95))
print(describe_score(-3))
lowest, highest = min_and_max([4, 9, 2, 7])
print(f"Lowest: {lowest}; highest: {highest}")

# A recursive function calls itself. Its base case stops the chain of calls.
def countdown(number):
    if number <= 0:
        return
    print(number)
    countdown(number - 1)


print("Countdown using recursion:")
countdown(3)


# 5. Positional arguments, keyword arguments, and defaults
def make_label(topic, level="beginner"):
    return f"{topic} ({level})"


print("\n5. POSITIONAL, KEYWORD, AND DEFAULT ARGUMENTS")
print(make_label("Lists"))
print(make_label(level="intro", topic="Functions"))


# 6. Mutable defaults: use None, then create a fresh list inside.
def add_topic(topic, topics=None):
    if topics is None:
        topics = []
    topics.append(topic)
    return topics


print("\n6. SAFE MUTABLE DEFAULT PATTERN")
print(add_topic("Strings"))
print(add_topic("Lists"))  # independent new list, not the previous result


# 7. Scope: local and global names
# A function can read a global name if it does not assign to that name locally.
course_name = "Python"


def show_course():
    print(f"Read global course_name: {course_name}")


# A local variable with the same spelling shadows the global name in the function.
status = "global: not started"


def show_local_and_global_status():
    status = "local: in progress"
    print(f"Inside function: {status}")


print("\n7. LOCAL AND GLOBAL SCOPE")
show_course()
show_local_and_global_status()
print(f"Outside function: {status}")  # still the global value

# global explicitly allows assignment to a module-level name.
completed_count = 0


def mark_complete_with_global():
    global completed_count
    completed_count += 1


mark_complete_with_global()
print(f"After global assignment: {completed_count}")

# Usually, returning a new value makes the data flow clearer than using global.
def increment(count):
    return count + 1


completed_count = increment(completed_count)
print(f"After return-based update: {completed_count}")


# 8. Enclosing scope and nonlocal
# nonlocal updates a name belonging to the enclosing function.
def make_counter():
    count = 0

    def next_count():
        nonlocal count
        count += 1
        return count

    return next_count


counter = make_counter()
print("\n8. ENCLOSING SCOPE AND NONLOCAL")
print(counter())
print(counter())


# 9. Flexible arguments: *args and **kwargs
# *args gathers extra positional arguments into a tuple.
def add_all(*numbers):
    print(f"  numbers inside function: {numbers} (type: {type(numbers).__name__})")
    return sum(numbers)


# **kwargs gathers extra named arguments into a dictionary.
def show_profile(**details):
    for key, value in details.items():
        print(f"  {key}: {value}")


# These symbols also unpack a sequence or dictionary into a function call.
def introduce_person(name, course):
    return f"{name} is learning {course}."


print("\n9. *ARGS AND **KWARGS")
print(f"Sum of flexible inputs: {add_all(2, 3, 4, 10)}")
show_profile(name="Ada", course="Python", level="beginner")
print(introduce_person(*( "Grace", "Python")))
person_details = {"name": "Linus", "course": "Python"}
print(introduce_person(**person_details))


# 10. Lambda functions
# A lambda is a short anonymous function with one expression.
double = lambda number: number * 2

print("\n10. LAMBDA FUNCTIONS")
print(f"double(5): {double(5)}")
topics = ["Sets", "Dictionaries", "Lists"]
print(f"Sorted by name length: {sorted(topics, key=lambda topic: len(topic))}")

# For reusable or multi-step work, a regular def is clearer.
def double_clearly(number):
    return number * 2


print(f"Regular function result: {double_clearly(5)}")


# 11. map() transforms each item; list() shows all results at once.
scores = [70, 80, 90]
new_scores = list(map(lambda score: score + 5, scores))
# A list comprehension is a common, readable alternative.
new_scores_comprehension = [score + 5 for score in scores]

print("\n11. MAP: TRANSFORM ITEMS")
print(f"Original scores: {scores}")
print(f"With map(): {new_scores}")
print(f"With comprehension: {new_scores_comprehension}")


# 12. filter() keeps items whose test returns True.
all_scores = [55, 72, 90, 48, 83]
passing = list(filter(lambda score: score >= 60, all_scores))
passing_comprehension = [score for score in all_scores if score >= 60]

print("\n12. FILTER: KEEP MATCHING ITEMS")
print(f"Passing with filter(): {passing}")
print(f"Passing with comprehension: {passing_comprehension}")


# 13. reduce() repeatedly combines values into one result.
# It is imported from functools. The third argument (0) is the starting value.
numbers = [2, 3, 4]
product = reduce(lambda running_product, number: running_product * number,
                 numbers, 1)
total_with_reduce = reduce(lambda running_total, number: running_total + number,
                           numbers, 0)

print("\n13. REDUCE: COMBINE INTO ONE RESULT")
print(f"Product: {product}")
print(f"Sum via reduce: {total_with_reduce}; simpler sum(): {sum(numbers)}")


# 14. Other useful built-ins that accept or use functions.
print("\n14. USEFUL BUILT-INS")
print(f"Any score is 100? {any(score == 100 for score in all_scores)}")
print(f"All scores pass? {all(score >= 60 for score in all_scores)}")
print(f"Highest score: {max(all_scores)}")
print(f"Numbered topics: {list(enumerate(topics, start=1))}")
print(f"Paired topics and scores: {list(zip(topics, scores))}")
print(f"Is len callable? {callable(len)}")


# 15. Docstrings
# A docstring is the description immediately inside a function.
def rectangle_area(width, height):
    """Return the area of a rectangle."""
    return width * height


print("\n15. DOCSTRINGS")
print(f"Area of 4 by 6 rectangle: {rectangle_area(4, 6)}")
print(f"Description: {rectangle_area.__doc__}")


# 16. Mini-project: Python study helper
def topic_message(topic, status="not started"):
    """Return a short study-status message for one topic."""
    return f"{topic}: {status}"


def count_completed(progress):
    """Return how many topics have the status 'complete'."""
    return sum(status == "complete" for status in progress.values())


def completion_percent(progress):
    """Return completion as a percentage, or 0 for an empty tracker."""
    if not progress:
        return 0
    return count_completed(progress) / len(progress) * 100


study_progress = {
    "Strings": "complete",
    "Lists": "complete",
    "Tuples": "in progress",
    "Functions": "not started",
}

print("\n16. MINI-PROJECT: PYTHON STUDY HELPER")
print(topic_message("Functions", "in progress"))
print(f"Completed topics: {count_completed(study_progress)}")
print(f"Progress: {completion_percent(study_progress):.0f}%")


print("\n" + "=" * 68)
print("TOUR COMPLETE — try changing the examples and running the file again.")
print("=" * 68)
