from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Catnip'}
	posts = [
		{
			'author': {'nickname': 'Zoxtree'},
			'body': 'Beautiful day in Vienna!'
		},
		{
			'author': {'nickname': 'Wiz'},
			'body': 'The Descent movie was so cool!'
		},
		{
			'author': {'nickname': 'Bee'},
			'body': 'Please don\'t leave me!'
		},
		{
			'author': {'nickname': 'Peatra'},
			'body': 'Sushi in the Bronx!'
		}
	]
	return render_template('index.html', 
							  title = 'Home', 
							  user = user,
							  posts = posts)
