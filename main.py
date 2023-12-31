
from flask import Flask, redirect, url_for, request, render_template
from pokemon import Pokemon,createPokemon
from waitress import serve






app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        if 'pokemon_name' not in request.form:
            return 'No Pokemon found'
        pokemon_name = request.form['pokemon_name']
            
        pokemon=createPokemon(pokemon_name)
        return render_template('index.html',pokemon=pokemon)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
   # app.run(debug=True)
