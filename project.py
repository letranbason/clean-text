import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from underthesea import word_tokenize as vi_tokenize

# create list stopwords for vn
vi_stopwords = set(["và", "là", "của", "các", "đã", "những", "với", "có"])  #add if have more

# func to check language
def detect_language(text):
    if any(char in set('ạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịĩọỏốồổỗộớờởỡợụủứừửữựỳỷỹỵ') for char in text):
        return 'vietnamese'
    else:
        return 'english'


def clean_text(text, language):
    text = text.lower()
    if language == 'english':
        words = word_tokenize(text)
        stop_words = set(stopwords.words('english'))
    else:
        words = vi_tokenize(text)
        stop_words = vi_stopwords
    
    words = [word for word in words if word not in stop_words]
    return " ".join(words)
