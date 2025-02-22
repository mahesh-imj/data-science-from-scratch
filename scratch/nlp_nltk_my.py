import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "Signal determines if the Lower HVAC screen is stowed or not."
words = word_tokenize(sentence)
pos_tags = pos_tag(words)

# Extracting proper nouns (NNP) and adjectives (JJ)
special_words = [word for word, pos in pos_tags if pos in ['NNP', 'JJ']]
print(special_words)  # Output: ['Lower', 'HVAC']
