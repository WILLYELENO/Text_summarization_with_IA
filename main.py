# Importar módulos necesarios

from fuctions import fetch_article, preprocess_text, compute_word_frequencies, score_sentences, summarize_text, translate_text

if __name__ == "__main__":
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    
    url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    article_text = fetch_article(url)
    
    if article_text:
        print("Original Article Text:\n", article_text[:2000])  # Mostrar los primeros 2000 caracteres para verificar el contenido
        article_text, formatted_article_text = preprocess_text(article_text)
        
        sentences = nltk.sent_tokenize(article_text)
        stopwords = nltk.corpus.stopwords.words('english')
        word_frequencies = compute_word_frequencies(formatted_article_text, stopwords)
        
        maximum_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = (word_frequencies[word] / maximum_frequency)
        
        sentence_scores = score_sentences(sentences, word_frequencies)
        
        summary = summarize_text(sentence_scores, sentences, 7)
        print("Summary:")
        print(summary)
        
        translated_summary = translate_text(summary, "en", "es")
        print("Translated Summary:")
        print(translated_summary)
