"""My first Python program.

Run this file with Python to see print(), comments, output options, and a small
greeting program. It uses sample input by default so it runs without prompting.
Set INTERACTIVE_INPUT to True if you want to type a name yourself.
"""

INTERACTIVE_INPUT = False

print("=" * 56)
print("MY FIRST PYTHON PROGRAM")
print("=" * 56)

# print() displays the text inside the quotes.
print("\n1. HELLO, WORLD!")
print("Hello, world!")

# Python runs statements in order, from top to bottom.
print("\n2. STATEMENTS RUN IN ORDER")
print("First instruction")
print("Second instruction")
print("Third instruction")

# print() can display different kinds of values.
# Text needs quotes; numbers and Boolean values do not.
print("\n3. DIFFERENT VALUES")
print("A message")
print(42)
print("42")  # this is text, unlike the number above
print(3.5)
print(True)

# A comment begins with #. Python ignores the comment itself.
print("\n4. COMMENTS")
# This comment is for the person reading the code.
print("The program runs this line, but ignores the comment.")

# sep controls what goes between multiple print() arguments.
# end controls what print() writes after its output.
print("\n5. SEPARATOR AND ENDING")
print("2026", "09", "28", sep="-")
print("Loading", end="...")
print("done")

# This small welcome uses sample data by default for unattended runs.
# Turn on interactive input to type your own name in the terminal.
print("\n6. PERSONALIZED WELCOME")
if INTERACTIVE_INPUT:
    name = input("What is your name? ")
else:
    name = "Ada"
    print("Using sample name 'Ada'; set INTERACTIVE_INPUT = True to type your own.")

print("Welcome to Python,", name)
print(f"Hello, {name}! Your programming journey starts here.")

# A tiny complete first program: display a simple welcome card.
print("\n7. WELCOME CARD MINI-PROJECT")
print("========================")
print("Welcome to Python!")
print("Your programming journey starts here.")
print("========================")

print("\n" + "=" * 56)
print("PROGRAM COMPLETE — edit a message, save, and run it again.")
print("=" * 56)
