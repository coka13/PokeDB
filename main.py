import requests
import json
from flask import Flask, redirect, url_for, request, render_template
from pokemon import Pokemon,createPokemon






app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        if 'pokemon_name' not in request.form:
            return 'No Pokémon found'
        pokemon_name = request.form['pokemon_name']
        pokemon=createPokemon(pokemon_name)
        return render_template('index.html',pokemon=pokemon)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)