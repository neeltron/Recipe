from flask import Flask, render_template, request, make_response, redirect, url_for
import requests



app = Flask(
  __name__,
  template_folder='templates',
  static_folder='static'
)

@app.route('/', methods = ['GET', 'POST'])
def index():
  if request.method == "POST":
    title = request.form.get('title')
    a = requests.get(url='https://api.spoonacular.com/recipes/findByIngredients?apiKey=f6c43d380801460d9e95ebdaa401d319&ingredients=coffee')
    
    return a[1]["title"]
  return render_template('index.html')



if __name__ == '__main__':
  # Run the Flask app
  app.run(
	host='0.0.0.0',
	debug=True,
	port=8080
  )
