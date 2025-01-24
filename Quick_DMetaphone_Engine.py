import fuzzy

# Initialize the Double Metaphone encoder
dmetaphone = fuzzy.DMetaphone()

# Prompt the user for input
print("Welcome to the Interactive Double Metaphone Encoder!")
print("Type a word to generate its phonetic codes. Type 'quit()' to quit.")

while True:
    # Get user input
    word = input("Enter a word (or 'quit()' to quit): ").strip()

    # Exit the loop if the user types "exit"
    if word.lower() == "quit()":
        print("Goodbye!")
        break

    # Validate input
    if not word.isalpha():
        print("Please enter a valid word containing only alphabetic characters.")
        continue

    # Generate the Double Metaphone encodings
    primary, alternate = dmetaphone(word)

    # Display the results
    print(f"Word: {word}")
    print(f"Primary Code: {primary.decode('utf-8') if primary else None}")
    print(f"Alternate Code: {alternate.decode('utf-8') if alternate else None}")
    print()
