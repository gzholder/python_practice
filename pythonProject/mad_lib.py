def get_input(word_type: str):
    user_input: str = input(f"Enter a {word_type}:")
    return user_input

adjective = get_input("adjective")
noun1 = get_input("noun")
verb1 = get_input("verb")
noun2 = get_input("noun")
verb1 = get_input("verb")


story = f"""
Once upon a time, there was a {adjective} {noun1} who loved to {verb1} all day.
Blah blah {noun2}
and {verb1}
and {noun1} and {noun2}
"""
print(story)