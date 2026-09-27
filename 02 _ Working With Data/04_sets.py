"""A hands-on tour of Python sets.

Run this file with Python to see examples and results. It covers creating sets,
uniqueness, adding and removing values, membership, set operations, and a
small study-progress comparison project.
"""

print("=" * 64)
print("PYTHON SETS: A HANDS-ON TOUR")
print("=" * 64)


# 1. Creating sets
# Curly braces make a non-empty set. Repeated values are stored once.
topics = {"Strings", "Lists", "Strings", "Loops"}
empty_set = set()  # {} would create an empty dictionary instead

print("\n1. CREATING SETS")
print(f"Topics (duplicates collapse): {topics}")
print(f"Empty set: {empty_set}")
print("Set print order may vary; sets do not promise a display order.")

# A set can be made from a list to remove duplicate values.
raw_names = ["Ada", "Grace", "Ada", "Linus"]
unique_names = set(raw_names)
print(f"Unique names: {unique_names}")


# 2. Adding and removing values
topics = {"Strings", "Lists"}
topics.add("Sets")
topics.update(["Loops", "Tuples"])
print("\n2. ADDING AND REMOVING")
print(f"After add() and update(): {topics}")

topics.discard("Functions")  # missing value: no error
topics.remove("Loops")
print(f"After discard() and remove(): {topics}")

# pop() removes an arbitrary item because sets have no first/last position.
removed_item = topics.pop()
print(f"An arbitrary popped item: {removed_item}")
print(f"Set after pop(): {topics}")


# 3. Membership and length
completed = {"Strings", "Lists", "Loops"}
print("\n3. MEMBERSHIP AND LENGTH")
print(f"Number of completed topics: {len(completed)}")
print(f"Have we completed Lists? {'Lists' in completed}")
print(f"Have we completed Tuples? {'Tuples' in completed}")


# 4. Set operations
# These operators compare groups and produce new sets.
alex = {"Strings", "Lists", "Loops"}
sam = {"Lists", "Sets", "Functions"}

print("\n4. SET OPERATIONS")
print(f"Alex: {alex}")
print(f"Sam:  {sam}")
print(f"Union (all topics): {alex | sam}")
print(f"Intersection (shared): {alex & sam}")
print(f"Alex only (difference): {alex - sam}")
print(f"In one set only (symmetric difference): {alex ^ sam}")


# 5. Comparing sets
required = {"Strings", "Lists"}
finished = {"Strings", "Lists", "Sets"}
print("\n5. SET COMPARISONS")
print(f"Required topics are a subset of finished? {required.issubset(finished)}")
print(f"Finished topics contain all required? {finished.issuperset(required)}")


# 6. Sorting for predictable display
# A set has no positional order; sorted() creates an ordered list for display.
print("\n6. SORTING FOR DISPLAY")
print(f"The set: {sam}")
print(f"Sorted list: {sorted(sam)}")


# 7. Removing duplicates while keeping first-seen order
# dict.fromkeys remembers insertion order and keeps each key once.
raw_topics = ["Lists", "Strings", "Lists", "Tuples", "Strings"]
unique_in_order = list(dict.fromkeys(raw_topics))
print("\n7. UNIQUE VALUES, ORIGINAL ORDER")
print(f"Original list: {raw_topics}")
print(f"Unique in first-seen order: {unique_in_order}")


# 8. Mini-project: compare Python study progress
alex_completed = {"Strings", "Lists", "Loops"}
sam_completed = {"Lists", "Sets", "Functions"}
all_completed = alex_completed | sam_completed
shared = alex_completed & sam_completed
alex_only = alex_completed - sam_completed

print("\n8. MINI-PROJECT: COMPARE STUDY PROGRESS")
print(f"Topics completed by either learner: {sorted(all_completed)}")
print(f"Topics both learners completed: {sorted(shared)}")
print(f"Topics only Alex completed: {sorted(alex_only)}")


print("\n" + "=" * 64)
print("TOUR COMPLETE — try changing the examples and running the file again.")
print("=" * 64)
