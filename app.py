from flask import Flask, render_template, request
from project import clean_text, detect_language 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
app = Flask(__name__)
app.config['DEBUG'] = True
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
