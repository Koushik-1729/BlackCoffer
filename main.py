from gnews import GNews
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
gnews = GNews()
negative_words=open('MasterDictionary/negative-words.txt').readlines()
negative_words=[i.replace('\n',"") for i in negative_words]
positive_words=open('MasterDictionary/positive-words.txt').readlines()
positive_words=[i.replace('\n',"") for i in positive_words]
stop_words=open('StopWords/StopWords_Auditor.txt').readlines()
stop_words=[i.replace('\n',"") for i in stop_words]
stop_words_Currencies=open('StopWords/StopWords_Currencies.txt').readlines()
stop_words_Currencies=[i.replace('\n',"") for i in stop_words_Currencies]
stop_words_Dates=open('StopWords/StopWords_DatesandNumbers.txt').readlines()
stop_words_Dates=[i.replace('\n',"") for i in stop_words_Dates]
stop_words_Generic=open('StopWords/StopWords_Generic.txt').readlines()
stop_words_Generic=[i.replace('\n',"") for i in stop_words_Generic]
stop_words_Generic_Long=open('StopWords/StopWords_GenericLong.txt').readlines()
stop_words_Generic_Long=[i.replace('\n',"") for i in stop_words_Generic_Long]
stop_words_Geographic=open('StopWords/StopWords_Geographic.txt').readlines()
stop_words_Geographic=[i.replace('\n',"") for i in stop_words_Geographic]
stop_words_Names=open('StopWords/StopWords_Names.txt').readlines()
stop_words_Names=[i.replace('\n',"") for i in stop_words_Names]

all_stop_words = stop_words + stop_words_Currencies +stop_words_Dates +stop_words_Generic+stop_words_Generic_Long+stop_words_Geographic+stop_words_Names
column_names = [
    "POSITIVE SCORE",
    "NEGATIVE SCORE",
    "POLARITY SCORE",
    "SUBJECTIVITY SCORE",
    "AVG SENTENCE LENGTH",
    "PERCENTAGE OF COMPLEX WORDS",
    "FOG INDEX",
    "AVG NUMBER OF WORDS PER SENTENCE",
    "COMPLEX WORD COUNT",
    "WORD COUNT",
    "SYLLABLE PER WORD",
    "PERSONAL PRONOUNS",
    "AVG WORD LENGTH"
]
def get_all_scores(_url):
  try:
    gdata = gnews.get_full_article(_url)
    article_title = gdata.title
    article_text = ''.join(gdata.text.split('\n')[:-2])

    # print(article_text)

    import nltk
    from nltk.tokenize import sent_tokenize, word_tokenize
    from nltk.corpus import stopwords

    # Provided text
    text = article_text

    # Your list of stop words (replace with your actual list)
    custom_stopwords = ["the", "and", "to", "of", "in", "is", "it", "this", "that", "with"]

    # Create a set of custom and NLTK stop words
    nltk_stopwords = set(stopwords.words('english'))
    all_stopwords = set(custom_stopwords) | nltk_stopwords

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stop words
    filtered_tokens = [word for word in tokens if word.lower() not in all_stopwords]

    # Load your dictionary of positive and negative words (replace with your actual dictionary)
    # For demonstration, we'll use a sample dictionary.
    # positive_words = positive_words
    # negative_words = negative_words

    # Calculate Positive and Negative Scores
    positive_score = sum(1 for word in filtered_tokens if word.lower() in positive_words)
    negative_score = sum(1 for word in filtered_tokens if word.lower() in negative_words)

    # Calculate Polarity Score
    polarity_score = (positive_score - negative_score) / (positive_score + negative_score + 0.000001)

    # Calculate Subjectivity Score
    subjectivity_score = (positive_score + negative_score) / (len(filtered_tokens) + 0.000001)

    complex_word_count = sum(1 for word in filtered_tokens if len(word) > 6)

    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Calculate Average Sentence Length
    avg_sentence_length = len(filtered_tokens) / len(sentences)

    # Calculate Percentage of Complex Words
    complex_word_count = sum(1 for word in filtered_tokens if len(word) > 6)
    percentage_complex_words = (complex_word_count / len(filtered_tokens)) * 100

    # Calculate FOG Index
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)

    # Calculate Average Number of Words per Sentence
    avg_words_per_sentence = len(filtered_tokens) / len(sentences)

    # Calculate Word Count
    word_count = len(filtered_tokens)

    # Calculate Syllables per Word
    def count_syllables(word):
        return sum(word.lower().count(ch) for ch in "aeiou")

    syllables_per_word = sum(count_syllables(word) for word in filtered_tokens) / len(filtered_tokens)

    # Count Personal Pronouns
    personal_pronouns = ["I", "me", "my", "mine", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves"]
    personal_pronoun_count = sum(1 for word in filtered_tokens if word.lower() in personal_pronouns)

    # Calculate Average Word Length
    avg_word_length = sum(len(word) for word in filtered_tokens) / len(filtered_tokens)

    # Display results
    # print("Positive Score:", positive_score)
    # print("Negative Score:", negative_score)
    # print("Polarity Score:", polarity_score)
    # print("Subjectivity Score:", subjectivity_score)
    # print("Average Sentence Length:", avg_sentence_length)
    # print("Percentage of Complex Words:", percentage_complex_words)
    # print("FOG Index:", fog_index)
    # print("Average Number of Words per Sentence:", avg_words_per_sentence)
    # print("Word Count:", word_count)
    # print("Syllables per Word:", syllables_per_word)
    # print("Personal Pronouns Count:", personal_pronoun_count)
    # print("Average Word Length:", avg_word_length)

    return [positive_score ,negative_score,polarity_score ,subjectivity_score ,avg_sentence_length ,percentage_complex_words,fog_index,avg_words_per_sentence ,complex_word_count,word_count,syllables_per_word,personal_pronoun_count,avg_word_length]
  except:
     return [0]*len(column_names)

#print(len(column_names))


import pandas as pd


df = pd.read_excel('input.xlsx',engine='openpyxl')

# e = get_all_scores('https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-3/')
# print(e)
df[column_names] = df.apply(lambda x : get_all_scores(x.URL) ,axis=1 ,result_type='expand')

df.to_excel('out.xlsx',index=False)


