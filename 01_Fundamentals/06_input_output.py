"""A hands-on tour of Python input and output.

Run this script to see print(), f-strings, sep/end, escape sequences, cleaned
input, and an interactive study summary. Sample answers are used by default;
set INTERACTIVE_INPUT = True to type your own responses.
"""

INTERACTIVE_INPUT = False


def section(title):
    print(f"\n{title}")
    print("-" * len(title))


print("=" * 68)
print("PYTHON INPUT AND OUTPUT: A HANDS-ON TOUR")
print("=" * 68)


# 1. print() displays strings and other values.
section("1. BASIC OUTPUT")
print("Hello, Python!")
print(42)
score = 98
print(score)
print(score + 2)


# 2. Multiple arguments are separated by a space by default.
section("2. MULTIPLE VALUES")
name = "Ada"
print("Learner:", name, "Score:", score)


# 3. F-strings place values and expressions into readable text.
section("3. F-STRINGS")
completed = 4
total = 10
print(f"{name} scored {score} points.")
print(f"Lessons remaining: {total - completed}")
price = 3.5
progress = 0.735
print(f"Price: ${price:.2f}")
print(f"Progress: {progress:.1%}")
print(f"Score with three-character width: {score:03d}")


# 4. sep goes between print arguments; end goes after this call's output.
section("4. SEP AND END")
print("2026", "09", "28", sep="-")
print("Loading", end="...")
print("done")


# 5. Escape sequences add line breaks and tabs.
section("5. NEWLINES AND TABS")
print("First line\nSecond line")
print("Name:\tAda")


# 6. input() returns text. Use sample answers by default for unattended runs.
section("6. INPUT")
if INTERACTIVE_INPUT:
    input_name = input("Your name: ")
    input_topic = input("Topic you are studying: ")
else:
    input_name = "  Ada  "
    input_topic = "  Input and Output  "
    print("Using sample answers; set INTERACTIVE_INPUT = True to type your own.")

print(f"Raw name response: {input_name!r}")
print(f"Input type: {type(input_name).__name__}")


# 7. Clean responses before displaying or comparing them.
section("7. CLEANING INPUT")
clean_name = input_name.strip()
clean_topic = input_topic.strip()
print(f"Clean name: {clean_name!r}")
print(f"Clean topic: {clean_topic!r}")

answer = " YES "
normalized_answer = answer.strip().lower()
print(f"Normalized yes/no answer: {normalized_answer!r}")
print(f"Is it an accepted yes answer? {normalized_answer in {'yes', 'y'} }")


# 8. Mini-project: personalized study summary.
section("8. MINI-PROJECT: STUDY SUMMARY")
print("=" * 32)
print(f"Learner: {clean_name}")
print(f"Current topic: {clean_topic}")
print("Keep making progress!")
print("=" * 32)


print("\n" + "=" * 68)
print("TOUR COMPLETE — turn on interactive input to personalize the report.")
print("=" * 68)
