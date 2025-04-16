names = ["Alice", "Bob", "Charlie", "Anna", "David", "Diana", "Brian"]
grouped_names = {}

for name in names:
    first_letter = name[0].upper()
    grouped_names.setdefault(first_letter, []).append(name)

print("Grouped names:", grouped_names)
