"""
Ask the user to supply the words to the story in {}'s.
Tell them the story with the words they gave inserted in.
"""

# Write a story with some words missing
colour1 = input("Input colour 1: ")
colour2 = input("Input colour 2: ")
adj = input("Input adjective :")

# missing words are got from users inputs
story = """
Roses are {colour}
Violets are {colour2}
Sugar is {adjective}
And so are you
"""

# Ask the user to provide the missing words

# Display the final story
print(story.format(colour=colour1,colour2=colour2,adjective=adj))
