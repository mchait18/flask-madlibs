from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh so secret"

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/home-2')
def home_page_2():
    story.template = request.args['template']
    return render_template('home_2.html', story=story)

@app.route('/story')
def get_story():
    answers = {}
    for word in story.prompts:
       answers[word] = request.args[word]
    story_txt = story.generate(answers)
    return render_template('story.html', story_txt= story_txt)
