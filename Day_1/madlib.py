from __future__ import print_function

"""
String Substitution for a Mad Lib
Adapted from code by Kirby Urner
"""

story = """
Once upon a time, deep in an ancient jungle,
there lived a %(animal)s.  This %(animal)s
liked to eat %(food)s, but the jungle had
very little %(food)s to offer.  One day, an
explorer found the %(animal)s and discovered
it liked %(food)s.  The explorer took the
%(animal)s back to %(city)s, where it could
eat as much %(food)s as it wanted.  However,
the %(animal)s became homesick, so the
explorer brought it back to the jungle,
leaving a large supply of %(food)s.

The End
"""


def tellStory():
    userPicks = dict()

    print()

    addPick('animal', userPicks)
    addPick('food', userPicks)
    addPick('city', userPicks)
    print(story % userPicks)


def addPick(cue, dictionary):
    prompt = "Enter a specific example for %s: " % cue
    try:
        dictionary[cue] = str(raw_input(prompt))
    except:
        dictionary[cue] = str(input(prompt))

tellStory()

print()
