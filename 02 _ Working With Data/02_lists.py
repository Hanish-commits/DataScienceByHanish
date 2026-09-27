"""A hands-on tour of Python lists.

Run this file with Python to see examples and results. It covers creating lists,
reading and slicing them, changing contents, copying, looping, searching,
sorting, and a small study-tracker project.
"""

print("=" * 64)
print("PYTHON LISTS: A HANDS-ON TOUR")
print("=" * 64)


# 1. Creating lists
# A list stores several ordered items between square brackets.
languages = ["Python", "Java", "Ruby"]
scores = [92, 85, 98]
empty_topics = []

print("\n1. CREATING LISTS")
print(f"Languages: {languages}")
print(f"Scores: {scores}")
print(f"An empty list: {empty_topics}")


# 2. Length, indexing, and membership
# Indexes start at 0. Negative indexes count backward from the end:
# -1 is last, -2 is second-to-last. Both are useful when list length varies.
print("\n2. READING LISTS")
print(f"Number of languages: {len(languages)}")
print(f"First language (index 0): {languages[0]}")
print(f"Second language (index 1): {languages[1]}")
print(f"Last language (index -1): {languages[-1]}")
print(f"Second-to-last (index -2): {languages[-2]}")
print("Position map:")
print(f"  items:    {languages}")
print("  indexes:  0      1      2")
print("  negative: -3     -2     -1")
print(f"Is Java in the list? {'Java' in languages}")
print(f"Is Go in the list? {'Go' in languages}")


# 3. Slicing
# Slicing selects a range: start is included, stop is excluded.
# Negative slice indexes count from the end too. Slices make a new list.
programming_topics = ["Strings", "Lists", "Loops", "Functions", "Files"]
print("\n3. SLICING")
print(f"All topics: {programming_topics}")
print(f"Indexes 1 through 3: {programming_topics[1:4]}")
print("  starts at index 1; stops before index 4")
print(f"Last two using negative indexes: {programming_topics[-2:]}")
print(f"Everything except the last: {programming_topics[:-1]}")
print(f"First two (start omitted): {programming_topics[:2]}")
print(f"Every second topic: {programming_topics[::2]}")
print(f"Reversed copy: {programming_topics[::-1]}")


# 4. Updating and adding items
# Lists are mutable: you can replace an item and add more items.
learning_plan = ["Strings", "Loops", "Functions"]
learning_plan[1] = "Lists"
learning_plan.append("Dictionaries")
learning_plan.insert(0, "Variables")

print("\n4. UPDATING AND ADDING")
print(f"Updated plan: {learning_plan}")

# append adds its argument as one item. extend adds each item from an iterable.
append_example = ["Strings", "Lists"]
append_example.append(["Loops", "Functions"])
extend_example = ["Strings", "Lists"]
extend_example.extend(["Loops", "Functions"])
print(f"After append(list): {append_example}")
print(f"After extend(list): {extend_example}")


# 5. Removing items
# remove() uses a value; pop() removes and returns an item.
tasks = ["Read", "Practice", "Review"]
tasks.remove("Practice")
finished_task = tasks.pop()

print("\n5. REMOVING ITEMS")
print(f"Remaining tasks: {tasks}")
print(f"Task returned by pop(): {finished_task}")


# 6. Combining and copying
morning = ["Read", "Plan"]
afternoon = ["Code", "Test"]
full_day = morning + afternoon
repeated = ["Review"] * 3

print("\n6. COMBINING AND COPYING")
print(f"Combined lists: {full_day}")
print(f"Repeated list: {repeated}")

# Assignment makes an alias: both names refer to one list.
original = ["Python", "Java"]
alias = original
alias.append("Ruby")
print(f"After changing alias, original is: {original}")

# copy() creates a separate outer list.
original = ["Python", "Java"]
separate_copy = original.copy()
separate_copy.append("Ruby")
print(f"Original after copy is changed: {original}")
print(f"Separate copy: {separate_copy}")


# 7. Looping and enumerate
languages = ["Python", "Java", "Ruby"]
print("\n7. LOOPING")
for language in languages:
    print(f"I am learning {language}.")

print("\nNumbered list:")
for number, language in enumerate(languages, start=1):
    print(f"{number}. {language}")


# 8. List comprehensions
# A comprehension builds a new list from each item in an existing list.
scores = [72, 85, 91, 64, 98]
curved_scores = [score + 5 for score in scores]
passing_scores = [score for score in scores if score >= 70]

print("\n8. LIST COMPREHENSIONS")
print(f"Original scores: {scores}")
print(f"Scores plus five: {curved_scores}")
print(f"Passing scores: {passing_scores}")


# 9. Searching and sorting
# index() finds the first matching position; count() counts matching items.
languages = ["Python", "Java", "Python", "Ruby"]
print("\n9. SEARCHING AND SORTING")
print(f"First Python position: {languages.index('Python')}")
print(f"Number of Python entries: {languages.count('Python')}")
print(f"Is Ruby present? {'Ruby' in languages}")

# sort() changes a list and returns None. sorted() gives you a new list.
unsorted_scores = [88, 72, 96, 85]
new_sorted_scores = sorted(unsorted_scores)
print(f"Original after sorted(): {unsorted_scores}")
print(f"New sorted list: {new_sorted_scores}")

unsorted_scores.sort()
print(f"Original after .sort(): {unsorted_scores}")
print(f"Descending order: {sorted(unsorted_scores, reverse=True)}")


# 10. Mini-project: Python study tracker
# Try changing the topics or completed_topic and run the program again.
topics = ["Strings", "Lists", "Loops"]
topics.append("Dictionaries")

completed_topic = "Strings"
if completed_topic in topics:
    topics.remove(completed_topic)

print("\n10. MINI-PROJECT: PYTHON STUDY TRACKER")
print("Topics still to study:")
for number, topic in enumerate(topics, start=1):
    print(f"{number}. {topic}")
print(f"Topics remaining: {len(topics)}")

if "Functions" in topics:
    topics.remove("Functions")
else:
    print("Functions is not on the list yet.")


print("\n" + "=" * 64)
print("TOUR COMPLETE — try changing the examples and running the file again.")
print("=" * 64)
