# The code adds 'random' module and displays a random joke from the jokes list thanks to 'random.choice' module each time the code runs.

import random

jokes = ["Hear about the new restaurant called Karma?\nThere’s no menu: You get what you deserve.",
         "Did you hear about the actor who fell through the floorboards?\nHe was just going through a stage.",
         "Did you hear about the claustrophobic astronaut?\nHe just needed a little space.",
         "Why don’t scientists trust atoms?\nBecause they make up everything.",
         "Where are average things manufactured?\nThe satisfactory.",
         "How do you drown a hipster?\nThrow him in the mainstream.",
         "What sits at the bottom of the sea and twitches?\nA nervous wreck."]

random_joke = random.choice(jokes)

print(random_joke)
