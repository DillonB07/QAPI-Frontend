from flask import Flask, render_template
from requests import get

app = Flask(__name__)
url = 'https://qapi-api.ml/statistics/'

@app.route('/')
def index():
    total_questions = get(f'{url}/total').text
    return render_template('home.html', questions=total_questions)

@app.route('/statistics')
def statistics():
    memory = get(f'{url}type/memory').text
    multi = get(f'{url}type/multi').text
    true = get(f'{url}type/true').text
    number = get(f'{url}type/number').text

    total_questions = get(f'{url}/total').text

    literature = get(f'{url}topic/literature').text
    geography = get(f'{url}topic/geography').text
    history = get(f'{url}topic/history').text
    entertainment = get(f'{url}topic/entertainment').text
    science = get(f'{url}topic/science').text
    leisure = get(f'{url}topic/leisure').text
    technology = get(f'{url}topic/technology').text
    return render_template('statistics.html', memory=memory, multi=multi, true_or_false=true, number=number, total=total_questions, literature=literature, geography=geography, history=history, entertainment=entertainment, science=science, leisure=leisure, technology=technology)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)