from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, RegexpTokenizer, TweetTokenizer 
import nltk

tokenizer = TweetTokenizer()
message = 'This is an amazing app!! I really love 🤣🥳😀 it!! would be good if it also supported      multiple line comments.'

print(tokenizer.tokenize(message))
