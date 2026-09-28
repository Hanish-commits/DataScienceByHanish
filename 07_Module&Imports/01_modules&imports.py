"""A hands-on tour of Python modules and imports.

This single-file tour demonstrates standard-library imports, aliases, the main
guard, module search paths, and import-related best practices. The Markdown
guide includes a multi-file package layout you can build as a next exercise.
"""

import math
import statistics as stats
import sys
from pathlib import Path
from math import sqrt


def main():
    print("=" * 68)
    print("PYTHON MODULES AND IMPORTS: A HANDS-ON TOUR")
    print("=" * 68)

    # 1. Import a module and use names through its module prefix.
    print("\n1. IMPORT A MODULE")
    print(f"math.sqrt(81): {math.sqrt(81)}")

    # 2. Import one name directly when that keeps the code clear.
    print("\n2. IMPORT A SELECTED NAME")
    print(f"sqrt(49): {sqrt(49)}")

    # 3. Aliases can shorten long module names; stats is a common-style alias.
    print("\n3. IMPORT WITH AN ALIAS")
    print(f"Mean score: {stats.mean([70, 80, 90])}")

    # 4. pathlib is part of Python's standard library.
    print("\n4. STANDARD LIBRARY MODULE")
    path = Path("notes.txt")
    print(f"File suffix: {path.suffix}")

    # 5. A module has a special name depending on how it is run.
    print("\n5. MODULE NAME AND MAIN GUARD")
    print(f"This file's __name__ is: {__name__}")
    print("Because main() is called below only under the main guard, importing")
    print("this file from another module will not automatically run this tour.")

    # 6. sys.path lists locations Python checks when looking for modules.
    print("\n6. IMPORT SEARCH PATH")
    print(f"Python checks {len(sys.path)} import locations in this environment.")
    print(f"One path entry: {sys.path[0] if sys.path else '(none)'}")

    # 7. A module can expose reusable functions without running them at import.
    print("\n7. REUSABLE FUNCTION DEFINITION")
    print("This tour's main() contains the demonstration; importing the file")
    print("defines main() but does not call it automatically.")

    print("\n" + "=" * 68)
    print("TOUR COMPLETE — see the Markdown guide for multi-file package examples.")
    print("=" * 68)


if __name__ == "__main__":
    main()
