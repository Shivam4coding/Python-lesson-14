# SMART NOTES ORGANISER

print("===================================")
print("       SMART NOTES ORGANISER")
print("===================================\n")

# Step 1: Preview notes
n = int(input("How many characters would you like to preview? "))

with open("class-notes.txt", "r") as notes:
    preview = notes.read(n)

print("\n--- Notes Preview ---")
print(preview)

# Step 2: Read all lines
with open("class-notes.txt", "r") as notes:
    lines = notes.readlines()

print(f"\nTotal number of lines: {len(lines)}")

# Step 3: Display notes with line numbers
print("\n--- All Notes ---")

for i, line in enumerate(lines, start=1):
    print(f"{i} -> {line.strip()}")

# Step 4: Search for a word
search_word = input("\nEnter a word to find in your notes: ")

found_lines = []

for i, line in enumerate(lines, start=1):
    if search_word.lower() in line.lower():
        found_lines.append((i, line))

print(f"\nFound {len(found_lines)} matching note(s).")

if found_lines:
    print("\n--- Matching Notes ---")
    for number, line in found_lines:
        print(f"{number} -> {line.strip()}")
else:
    print("No matching notes found.")

# Step 5: Remove notes starting with a specific word
skip_word = input("\nWhich starting word should be skipped? ")

organised_lines = []

for line in lines:
    if line.strip().lower().startswith(skip_word.lower()):
        continue
    organised_lines.append(line)

skipped = len(lines) - len(organised_lines)

print(f"\nNumber of notes skipped: {skipped}")

# Step 6: Save organised notes
with open("organised-notes.txt", "w") as file:
    for line in organised_lines:
        file.write(line)

# Step 7: Display final file
print("\n===================================")
print("      ORGANISATION COMPLETE")
print("===================================")

print("\nOrganised notes saved to 'organised-notes.txt'.")

print("\n--- Organised Notes ---")

with open("organised-notes.txt", "r") as file:
    print(file.read())

print("\nSmart Notes Organiser completed successfully.")