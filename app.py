from flask import Flask, render_template, request
from project import clean_text, detect_language  # Assuming your script is named 'your_script.py'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    cleaned_text = ""
    if request.method == 'POST':
        user_input = request.form['text']
        language = detect_language(user_input)
        cleaned_text = clean_text(user_input, language)
    return render_template('index.html', cleaned_text=cleaned_text)

if __name__ == '__main__':
    app.run(debug=True)
