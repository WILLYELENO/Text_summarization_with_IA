# Importar módulos necesarios

import urllib.request
import re
import nltk
# import requests
# from bs4 import BeautifulSoup
from inscriptis import get_text
from googletrans import Translator

# Scrapea artículo de Wikipedia
enlace = "https://en.wikipedia.org/wiki/Python_(programming_language)"
html = urllib.request.urlopen(enlace).read().decode('utf-8')
text = get_text(html)
article_text = text
article_text = article_text.replace("[ edit ]", "")
print("###################")

# Tokenización y procesamiento del texto
# from nltk import word_tokenize, sent_tokenize

# Eliminación de corchetes y espacios extra
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)

formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text)
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

# Descargar recursos de NLTK si es necesario
# nltk.download('punkt')
# nltk.download('stopwords')

# Tokenización de oraciones
sentence_list = nltk.sent_tokenize(article_text)

# Encontrar la frecuencia de cada palabra
stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

# Normalizar las frecuencias de palabras
maximum_frequency = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word] / maximum_frequency)

# Calcular las puntuaciones de las oraciones
sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

# Crear el resumen con las mejores frases
import heapq
summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)
print(summary)

# Traducir el resumen al español
translator = Translator()
translation = translator.translate(summary, src="en", dest="es")
print(translation.text)


