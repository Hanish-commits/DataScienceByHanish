"""A hands-on tour of Python strings.

Run this file with Python to see the examples and their results. It follows the
beginner-friendly scope of the companion Markdown guide: creating strings,
reading them, slicing, immutability, combining, methods, searching, and f-string
formatting.
"""

print("=" * 64)
print("PYTHON STRINGS: A HANDS-ON TOUR")
print("=" * 64)


# 1. Creating strings
# Single and double quotes both create the same kind of Python value: str.
language = "Python"
topic = 'strings'
announcement = f"Today we are learning {language} {topic}."

print("\n1. CREATING STRINGS")
print(announcement)

# Triple quotes are useful when the value itself should contain line breaks.
short_note = """Strings can contain
more than one line."""
print(short_note)

# Escape sequences represent special characters inside an ordinary string.
# \n means “start a new line”; \t means “insert a tab”.
print("Line one\nLine two")
print("Name:\tAda")


# 2. Length, indexing, and membership
# len() counts the characters in the string. Indexes start at zero.
word = "Python"
print("\n2. READING STRINGS")
print(f"Word: {word}")
print(f"Length: {len(word)}")
print(f"First character (index 0): {word[0]}")
print(f"Last character (index -1): {word[-1]}")
print(f"Does 'yth' appear in the word? {'yth' in word}")


# 3. Slicing
# A slice has the form text[start:stop:step]. The stop position is excluded.
course = "programming"
print("\n3. SLICING")
print(f"Full text: {course}")
print(f"Characters 0 through 3: {course[0:4]}")
print(f"First three characters: {course[:3]}")
print(f"From index 3 to the end: {course[3:]}")
print(f"Every second character: {course[::2]}")
print(f"Reversed: {course[::-1]}")


# 4. Immutability
# A string cannot be edited by assigning to one of its positions.
# Instead, build a new string and assign that new value to a variable.
original = "Python"
updated = "J" + original[1:]

print("\n4. IMMUTABILITY")
print(f"Original string: {original}")
print(f"New string:      {updated}")
# original still refers to "Python"; creating updated did not change it.


# 5. Combining and repeating strings
first_part = "Python"
second_part = " strings"
combined = first_part + second_part
separator_line = "-" * 24

print("\n5. COMBINING STRINGS")
print(combined)
print(separator_line)

# join() places the chosen separator between each string in the list.
words = ["learn", "by", "building"]
joined_words = " ".join(words)
print(joined_words)


# 6. Transforming strings with methods
# String methods return a result; they do not change the original variable.
rough_topic = "   pYtHoN sTrInGs   "
clean_topic = rough_topic.strip()
readable_topic = clean_topic.title()
uppercase_topic = readable_topic.upper()

print("\n6. STRING METHODS")
print(f"Rough version:     {rough_topic!r}")
print(f"After strip():     {clean_topic!r}")
print(f"After title():     {readable_topic!r}")
print(f"After upper():     {uppercase_topic!r}")
print(f"Original unchanged: {rough_topic!r}")

# replace() also returns a new string. Save it if you want to keep the result.
sentence = "Python is tricky. Python is also fun."
friendlier_sentence = sentence.replace("tricky", "interesting", 1)
print(friendlier_sentence)


# 7. Splitting and searching
# split() without an argument groups runs of whitespace into separators.
word_list = "learn Python one step at a time".split()
comma_parts = "strings,lists,loops".split(",")

print("\n7. SPLITTING AND SEARCHING")
print(f"Words: {word_list}")
print(f"Comma-separated topics: {comma_parts}")

sentence = "Python strings are useful"
print(f"Does it contain 'strings'? {'strings' in sentence}")
print(f"Position of 'useful': {sentence.find('useful')}")
print(f"Starts with 'Python'? {sentence.startswith('Python')}")
print(f"Ends with 'useful'? {sentence.endswith('useful')}")

# find() returns -1 when the requested text is absent.
print(f"Position of 'Java': {sentence.find('Java')}")


# 8. Checking character content
print("\n8. CHECKING CHARACTER CONTENT")
print(f"'123'.isdigit(): {'123'.isdigit()}")
print(f"'Python'.isalpha(): {'Python'.isalpha()}")
print(f"'Python3'.isalnum(): {'Python3'.isalnum()}")
print(f"'   '.isspace(): {'   '.isspace()}")


# 9. Formatting output with f-strings
student = "Ada"
completed_lessons = 7
progress = 0.7

print("\n9. F-STRING FORMATTING")
print(f"{student} has completed {completed_lessons} lessons.")
print(f"Progress: {progress:.0%}")
print(f"Lessons completed: {completed_lessons:03d}")

# A format width can line up text in a simple report.
print(f"{'TOPIC':<20} {'LENGTH':>6}")
print(f"{'Python':<20} {len('Python'):>6}")
print(f"{'Strings':<20} {len('Strings'):>6}")


# 10. Mini-project: make a Python study card
# This combines concepts already shown above. Change these two values and run
# the program again to see how the card changes.
raw_topic = "  python strings  "
definition = "text stored as an ordered sequence of characters"

study_topic = raw_topic.strip().title()
heading = study_topic.upper()
study_card = (
    f"{heading}\n"
    f"{definition}\n"
    f"Topic length: {len(study_topic)} characters"
)

print("\n10. MINI-PROJECT: PYTHON STUDY CARD")
print(study_card)


print("\n" + "=" * 64)
print("TOUR COMPLETE — try changing the examples and running the file again.")
print("=" * 64)
