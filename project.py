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

# Hàm để làm sạch và tiền xử lý văn bản
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

# Yêu cầu người dùng nhập văn bản
# user_input = input("Please enter a text for analysis: ")
# language = detect_language(user_input)

# Áp dụng hàm tiền xử lý vào văn bản nhập vào
# cleaned_text = clean_text(user_input, language)

# # In văn bản sau khi đã được tiền xử lý
# print("\nOriginal Text: ", user_input)
# print("Cleaned Text: ", cleaned_text)
