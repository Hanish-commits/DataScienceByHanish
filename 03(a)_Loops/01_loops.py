"""A hands-on tour of Python loops.

Run this file with Python to see examples of for and while loops, range,
enumerate, break, continue, loop else, nested loops, and common loop patterns.
"""

print("=" * 68)
print("PYTHON LOOPS: A HANDS-ON TOUR")
print("=" * 68)


# 1. for loop: visit each item once, in order.
languages = ["Python", "Java", "Ruby"]
print("\n1. FOR LOOP OVER A LIST")
for language in languages:
    print(f"I am learning {language}.")


# A string is also a sequence, so the loop visits one character at a time.
print("\n2. FOR LOOP OVER A STRING")
for letter in "code":
    print(letter)


# 3. range(): the stop number is excluded.
print("\n3. RANGE")
print(f"range(4): {list(range(4))}")
print(f"range(1, 5): {list(range(1, 5))}")
print(f"range(0, 10, 2): {list(range(0, 10, 2))}")
print(f"Countdown range: {list(range(5, 0, -1))}")


# 4. enumerate() gives both an index and the item.
topics = ["Strings", "Lists", "Loops"]
print("\n4. ENUMERATE")
for number, topic in enumerate(topics, start=1):
    print(f"{number}. {topic}")


# 5. while loop: keep going while its condition stays true.
count = 1
print("\n5. WHILE LOOP")
while count <= 3:
    print(f"count is {count}")
    count += 1  # this update makes the condition eventually become false


# 6. break: leave the loop early when a match is found.
print("\n6. BREAK")
for topic in ["Strings", "Lists", "Loops", "Functions"]:
    if topic == "Loops":
        print("Found Loops; stop searching.")
        break
    print(f"Checking {topic}")


# 7. continue: skip the rest of the current pass.
print("\n7. CONTINUE")
for number in range(1, 6):
    if number == 3:
        continue
    print(number)


# 8. Loop else runs only if the loop did not exit with break.
print("\n8. LOOP ELSE")
for number in [2, 4, 6, 8]:
    if number % 2 != 0:
        print("Found an odd number.")
        break
else:
    print("No odd numbers found.")


# 9. Nested loops: inner loop completes for each outer-loop item.
print("\n9. NESTED LOOPS")
for language in ["Python", "Java"]:
    for level in ["beginner", "advanced"]:
        print(f"{language}: {level}")


# 10. Loop through dictionaries and sets.
progress = {"Strings": "complete", "Lists": "in progress"}
print("\n10. DICTIONARIES AND SETS")
for topic, status in progress.items():
    print(f"{topic}: {status}")

for language in sorted({"Python", "Java", "Ruby"}):
    print(f"Set item in predictable order: {language}")


# 11. Accumulate a total and build a filtered list.
scores = [72, 85, 91]
total = 0
for score in scores:
    total += score

passing = []
for score in scores:
    if score >= 80:
        passing.append(score)

print("\n11. ACCUMULATING AND BUILDING A LIST")
print(f"Total score: {total}")
print(f"Passing scores: {passing}")
print(f"Same filtering with comprehension: {[score for score in scores if score >= 80]}")


# 12. Update items by index using enumerate().
topics = ["strings", "lists", "loops"]
for index, topic in enumerate(topics):
    topics[index] = topic.title()
print("\n12. UPDATING BY INDEX")
print(topics)


# 13. Mini-project: quiz attempts
# A list stands in for answers entered across attempts. tries always increases,
# so the loop has a clear stopping point even if no answer matches.
correct_answer = "for"
attempts = ["if", "while", "for"]
tries = 0
print("\n13. MINI-PROJECT: QUIZ ATTEMPTS")
while tries < len(attempts):
    answer = attempts[tries]
    tries += 1

    if answer == correct_answer:
        print(f"Correct! You got it in {tries} tries.")
        break
    else:
        print(f"{answer!r} is not the answer. Try again.")
else:
    print("No attempts left.")


print("\n" + "=" * 68)
print("TOUR COMPLETE — change the values and predict the loop before running.")
print("=" * 68)
