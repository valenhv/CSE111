# Student: Valentine Hernandez Vera
# EXCEEDING REQUIREMENTS: Connected the sentences to make them look like a story. For this, I added three more user-defined functions called "get_introduction", "get_buildup" and "get_resolution", and then reflected those additions in the main function.
import random

# Gets the determiners or articles that will be used.
def get_determiner(quantity):
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

# Gets the nouns that will be used.
def get_noun(quantity):
    if quantity == 1:
        words = ["bird", "cat", "boy", "girl", "child", "car", "dog", "man", "rabbit", "woman"]
    else:
        words = ["birds", "cats", "boys", "girls", "children", "men", "women", "dogs", "cars", "rabbits"]
    word = random.choice(words)
    return word

# Gets the verbs that will be used.
# Used "future" as a default parameter for Tense because it felt redundant to write "elif tense == 'future'".
# Used the number 2 to indicate plurals. This is to make sure that the statement about plurals work properly.
def get_verb(quantity, tense="future"):
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and quantity == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and quantity == 2:
        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    else:
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    word = random.choice(words)
    return word

# Gets the prepositions that will be used.
def get_preposition():
    words = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    word = random.choice(words)
    return word

# Makes the prepositional phrase.
def get_prepositional_phrase(quantity):
    if quantity == 1:
        prepositional_phrase = f"{get_preposition()} {get_determiner(1)} {get_noun(1)}"
    else:
        prepositional_phrase = f"{get_preposition()} {get_determiner(2)} {get_noun(2)}"
    return prepositional_phrase

# Makes the sentence.
def make_sentence(quantity, tense="future"):
    if quantity == 1:
        determiner_chosen = get_determiner(1)
        noun_chosen = get_noun(1)
    elif quantity == 2:
        determiner_chosen = get_determiner(2)
        noun_chosen = get_noun(2)
    
    if tense == "past":
        verb_chosen = get_verb("past")
    elif quantity == 1 and tense == "present":
        verb_chosen = get_verb(1, "present")
    elif quantity == 2 and tense == "present":
        verb_chosen = get_verb(2, "present")
    else:
        verb_chosen = get_verb(quantity, "future")
    return determiner_chosen and noun_chosen and verb_chosen

# Creativity: Gets an introduction that will be used.
def get_introduction():
    words = ["once upon a time", "one day", "today", "back in the day", "one morning", "a long time ago", "once"]
    word = random.choice(words)
    return word

# Creativity: Gets the build-up words that will be used.
def get_buildup():
    words = ["suddenly", "next", "all of a sudden", "before long", "soon", "at that moment", "unfortunately"]
    word = random.choice(words)
    return word

# Creativity: Gets the resolution words that will be used.
def get_resolution():
    words = ["finally", "luckily", "at last", "not a moment too soon"]
    word = random.choice(words)
    return word

# Collects all the randomly chosen words and puts them together to make sentences.
def main ():
    introduction = get_introduction()

    buildup1 = get_buildup()
    buildup2 = get_buildup()
    buildup3 = get_buildup()
    buildup4 = get_buildup()
    resolution = get_resolution()

    single_past = f"{get_determiner(1)} {get_noun(1)} {get_verb(1, 'past')} {get_prepositional_phrase(1)}"

    single_present = f"{get_determiner(1)} {get_noun(1)} {get_verb(1, 'present')} {get_prepositional_phrase(1)}"

    single_future = f"{get_determiner(1)} {get_noun(1)} {get_verb(1, 'future')} {get_prepositional_phrase(1)}"

    plural_past = f"{get_determiner(2)} {get_noun(2)} {get_verb(2, 'past')} {get_prepositional_phrase(2)}"

    plural_present = f"{get_determiner(2)} {get_noun(2)} {get_verb(2, 'present')} {get_prepositional_phrase(2)}"

    plural_future = f"{get_determiner(2)} {get_noun(2)} {get_verb(2, 'future')} {get_prepositional_phrase(2)}"
    
    # The result is shown in these print functions.
    print(f"{introduction.capitalize()}, {single_past}.")
    print(f"{buildup1.capitalize()}, {single_present}.")
    print(f"{buildup2.capitalize()}, {single_future}.")
    print(f"{buildup3.capitalize()}, {plural_past}.")
    print(f"{buildup4.capitalize()}, {plural_present}.")
    print(f"{resolution.capitalize()}, {plural_future}. The end.")
    return

print("Welcome! This program will show you six sentences in the form of a story. The words are chosen at random:")
print()
main()
