"""Practice loop-and-conditional patterns in Python.

Run this file to see rectangles, triangles, pyramids, diamonds, hollow shapes,
and number patterns. Each example uses row/column logic that you can change.
"""

print("=" * 68)
print("PYTHON LOOP AND CONDITIONAL PATTERNS")
print("=" * 68)


# 1. Solid rectangle: same number of symbols on every row.
print("\n1. SOLID RECTANGLE")
rows = 3
columns = 5
for row in range(rows):
    for column in range(columns):
        print("*", end=" ")
    print()  # finish this row


# 2. Growing left triangle: row number equals number of stars.
print("\n2. GROWING TRIANGLE")
height = 5
for row in range(1, height + 1):
    print("* " * row)


# 3. Inverted triangle: star count decreases each row.
print("\n3. INVERTED TRIANGLE")
for row in range(height, 0, -1):
    print("* " * row)


# 4. Right-aligned triangle: spaces shrink while stars grow.
print("\n4. RIGHT-ALIGNED TRIANGLE")
for row in range(1, height + 1):
    spaces = height - row
    stars = row
    print(" " * spaces + "* " * stars)


# 5. Centered pyramid.
# Row r has (height - r) spaces and (2*r - 1) stars.
print("\n5. PYRAMID")
for row in range(1, height + 1):
    spaces = height - row
    stars = 2 * row - 1
    print(" " * spaces + "*" * stars)


# 6. Inverted pyramid: grow spaces and reduce stars by two each row.
print("\n6. INVERTED PYRAMID")
for row in range(height, 0, -1):
    spaces = height - row
    stars = 2 * row - 1
    print(" " * spaces + "*" * stars)


# 7. Diamond: combine a pyramid and its lower half.
# Start the lower half at height - 1 to avoid repeating the widest row.
print("\n7. DIAMOND")
diamond_height = 4
for row in range(1, diamond_height + 1):
    spaces = diamond_height - row
    stars = 2 * row - 1
    print(" " * spaces + "*" * stars)
for row in range(diamond_height - 1, 0, -1):
    spaces = diamond_height - row
    stars = 2 * row - 1
    print(" " * spaces + "*" * stars)


# 8. Hollow rectangle: print a star on any border position.
print("\n8. HOLLOW RECTANGLE")
rectangle_rows = 4
rectangle_columns = 7
for row in range(rectangle_rows):
    for column in range(rectangle_columns):
        on_border = (
            row == 0
            or row == rectangle_rows - 1
            or column == 0
            or column == rectangle_columns - 1
        )
        if on_border:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# 9. Number triangle: each row prints 1 through the row number.
print("\n9. NUMBER TRIANGLE")
for row in range(1, 6):
    for number in range(1, row + 1):
        print(number, end=" ")
    print()


# 10. Repeated-number triangle: row number is repeated across that row.
print("\n10. REPEATED-NUMBER TRIANGLE")
for row in range(1, 6):
    for column in range(row):
        print(row, end=" ")
    print()


# 11. Checkerboard: if row + column is even, print a star; otherwise a dot.
print("\n11. CHECKERBOARD")
size = 5
for row in range(size):
    for column in range(size):
        if (row + column) % 2 == 0:
            print("*", end=" ")
        else:
            print(".", end=" ")
    print()


# 12. Mini-project: choose a pattern with if/elif/else.
print("\n12. CHOOSE A PATTERN")
pattern = "pyramid"  # try "triangle" or another value
choice_height = 4

if pattern == "triangle":
    for row in range(1, choice_height + 1):
        print("* " * row)
elif pattern == "pyramid":
    for row in range(1, choice_height + 1):
        spaces = choice_height - row
        stars = 2 * row - 1
        print(" " * spaces + "*" * stars)
else:
    print("Choose 'triangle' or 'pyramid'.")


print("\n" + "=" * 68)
print("PATTERN TOUR COMPLETE — change the heights and predict the output.")
print("=" * 68)
