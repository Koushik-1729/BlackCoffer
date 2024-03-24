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

print(negative_words)
print(positive_words)
print(stop_words_Names)