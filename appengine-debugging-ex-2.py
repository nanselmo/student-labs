# Debugging - Partner Exercise 2:
# Now that you are warmed up let's tackle another one.
# Ugh, it's riddled with bugs!
# This longer program contains more than one error.
# Copy and paste it
# Use the console to help you track them down, and fix them all.

def TalkLikeAPirate(sentence):
  """Converts a sentence to pirate-speak.

  Adapted from Python 3 for Absolute Beginners:
    http://www.google.com/books?id=sQGFIX_0xCUC&pg=PA242
  """
  # Strip whitespace and punctuation
  sentence = sentence.strip().rstrip('.!')

  # Lowercase the first letter of the sentence
  sentence = sentence[0].lower() + sentence[1:]

  # Piratify the text
  sentence = 'Yarr, ' + sentance + ', me hearties!'

  retunn sentence


print 'Content-Type: text/plain'
print ''

sentence = 'Hello, world!'
print TalkLikeAPIrate(sentence)
