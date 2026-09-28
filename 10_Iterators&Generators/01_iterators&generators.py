"""A hands-on tour of Python iterators and generators.

Run this file to see iterables, iter()/next(), generator functions, yield,
generator expressions, lazy execution, pipelines, and a custom iterator.
"""

print("=" * 68)
print("PYTHON ITERATORS AND GENERATORS: A HANDS-ON TOUR")
print("=" * 68)


# 1. Several built-in objects are iterable.
print("\n1. ITERABLES")
for letter in "code":
    print(letter, end=" ")
print()
for number in [10, 20, 30]:
    print(number, end=" ")
print()
for number in range(3):
    print(number, end=" ")
print()


# 2. iter() makes an iterator; next() advances that same iterator.
topics = ["Strings", "Lists", "Generators"]
iterator = iter(topics)
print("\n2. ITERATOR AND NEXT")
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(f"A default handles exhaustion: {next(iterator, 'finished')}")


# 3. An iterable can supply a new independent iterator each time.
print("\n3. TWO ITERATORS FROM ONE LIST")
first_pass = iter(["A", "B"])
second_pass = iter(["A", "B"])
print(next(first_pass))   # A
print(next(first_pass))   # B
print(next(second_pass))  # A; this iterator has its own position


# 4. A generator function yields values and pauses between them.
def count_up_to(limit):
    number = 1
    while number <= limit:
        yield number
        number += 1


print("\n4. GENERATOR FUNCTION")
counter = count_up_to(3)  # body has not started yet
print(next(counter))
print(next(counter))
print(next(counter))
print(f"After the last value: {next(counter, 'finished')}")


# 5. Show lazy execution: code runs only when the generator is advanced.
def announce_numbers(limit):
    for number in range(limit):
        print(f"Preparing {number}")
        yield number


print("\n5. LAZY EXECUTION")
announced = announce_numbers(2)
print("Generator created; its body has not run yet.")
print(f"Requested value: {next(announced)}")
print(f"Requested value: {next(announced)}")


# 6. A generator expression produces results on demand.
squares = (number * number for number in range(1, 6))
print("\n6. GENERATOR EXPRESSION")
print(next(squares))
print(next(squares))
print(f"Remaining values: {list(squares)}")

# If only consuming once, pass a generator expression directly to sum().
total = sum(number * number for number in range(1, 6))
print(f"Sum of squares: {total}")


# 7. A pipeline can filter and transform values without intermediate lists.
numbers = range(1, 11)
evens = (number for number in numbers if number % 2 == 0)
squares_of_evens = (number * number for number in evens)
print("\n7. GENERATOR PIPELINE")
print(f"Sum of squares of even numbers 1..10: {sum(squares_of_evens)}")


# 8. yield from delegates values from another iterable.
def all_topics():
    yield from ["Strings", "Lists"]
    yield from ["Tuples", "Sets"]


print("\n8. YIELD FROM")
print(list(all_topics()))


# 9. A manual iterator implements __iter__ and __next__.
class CountUpTo:
    def __init__(self, limit):
        self.current = 1
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.limit:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


print("\n9. CUSTOM ITERATOR")
print(list(CountUpTo(4)))


# 10. Mini-project: yield completed study topics one at a time.
records = [
    ("Strings", "complete"),
    ("Lists", "in progress"),
    ("Tuples", "complete"),
    ("Generators", "not started"),
]


def completed_topics(topic_records):
    for topic, status in topic_records:
        if status == "complete":
            yield topic


print("\n10. MINI-PROJECT: COMPLETED TOPICS")
completed = completed_topics(records)
print(f"First completed topic: {next(completed)}")
print(f"Remaining completed topics: {list(completed)}")


print("\n" + "=" * 68)
print("TOUR COMPLETE — generators are one-pass; make a new one to start again.")
print("=" * 68)
