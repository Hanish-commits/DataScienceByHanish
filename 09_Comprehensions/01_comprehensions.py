"""A hands-on tour of Python comprehensions.

Run this file to see list, set, dictionary, nested, filtered, conditional, and
generator expressions, plus equivalent loops and a small study report.
"""

print("=" * 68)
print("PYTHON COMPREHENSIONS: A HANDS-ON TOUR")
print("=" * 68)


# 1. A basic list comprehension transforms each source item.
numbers = [1, 2, 3, 4]
squares = [number * number for number in numbers]
print("\n1. BASIC LIST COMPREHENSION")
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")


# 2. The equivalent loop makes each step explicit.
topics = ["strings", "lists", "functions"]
capitalized = []
for topic in topics:
    capitalized.append(topic.title())
print("\n2. EQUIVALENT REGULAR LOOP")
print(f"Capitalized topics: {capitalized}")


# 3. Filter with a trailing if: items failing the condition are left out.
scores = [55, 72, 91, 48, 83]
passing = [score for score in scores if score >= 60]
print("\n3. FILTERING")
print(f"Passing scores: {passing}")


# 4. Conditional expression: every source item produces one label.
labels = ["pass" if score >= 60 else "retry" for score in scores]
print("\n4. IF/ELSE OUTPUT VALUE")
print(f"Status for every score: {labels}")


# 5. Set comprehension makes unique results; order is not guaranteed.
words = ["python", "PYTHON", "loops", "loops"]
lowercase_unique = {word.lower() for word in words}
print("\n5. SET COMPREHENSION")
print(f"Unique lowercase words: {lowercase_unique}")


# 6. Dictionary comprehension creates key:value pairs.
numbers = [1, 2, 3, 4]
squares_by_number = {number: number * number for number in numbers}
print("\n6. DICTIONARY COMPREHENSION")
print(f"Number to square: {squares_by_number}")

# It can also filter key:value pairs.
student_scores = {"Ada": 98, "Grace": 100, "Linus": 55}
passing_students = {
    name: score for name, score in student_scores.items() if score >= 60
}
print(f"Passing students: {passing_students}")


# 7. Nested comprehension: later for clauses are nested inside earlier ones.
pairs = [(row, column) for row in range(2) for column in range(3)]
print("\n7. NESTED COMPREHENSION")
print(f"Grid coordinates: {pairs}")

# Flatten a list of lists.
rows = [[1, 2], [3, 4], [5, 6]]
flattened = [number for row in rows for number in row]
print(f"Flattened values: {flattened}")


# 8. Multiple filters: all trailing conditions must be true.
selected = [number for number in range(1, 21) if number % 2 == 0 if number > 10]
print("\n8. MULTIPLE FILTERS")
print(f"Even numbers greater than 10: {selected}")


# 9. Call a named function from the expression.
def word_length(word):
    return len(word)


topics = ["Strings", "Lists", "Comprehensions"]
lengths = [word_length(topic) for topic in topics]
print("\n9. FUNCTION IN A COMPREHENSION")
print(f"Topic lengths: {lengths}")


# 10. Generator expressions produce values on demand rather than a full list.
generator_total = sum(number * number for number in range(5))
print("\n10. GENERATOR EXPRESSION")
print(f"Sum of squares from 0 through 4: {generator_total}")


# 11. Mini-project: build a small study report.
scores = {"Ada": 98, "Grace": 100, "Linus": 55, "Guido": 82}
passing_names = [name for name, score in scores.items() if score >= 60]
score_labels = {
    name: "pass" if score >= 60 else "retry"
    for name, score in scores.items()
}
unique_statuses = {status for status in score_labels.values()}

print("\n11. MINI-PROJECT: STUDY REPORT")
print(f"Passing names: {passing_names}")
print(f"Score labels: {score_labels}")
print(f"Unique labels: {unique_statuses}")


print("\n" + "=" * 68)
print("TOUR COMPLETE — try changing the source collections and conditions.")
print("=" * 68)
