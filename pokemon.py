import requests


type_mappings = {
    'normal': 'Normal type.ico',
    'fire': 'Fire type.ico',
    'water': 'Water type.ico',
    'electric': 'Electric type.ico',
    'grass': 'Grass type.ico',
    'ice': 'Ice type.ico',
    'fighting': 'Fighting type.ico',
    'poison': 'Poison type.ico',
    'ground': 'Ground type.ico',
    'flying': 'Flying type.ico',
    'psychic': 'Psychic type.ico',
    'bug': 'Bug type.ico',
    'rock': 'Rock type.ico',
    'ghost': 'Ghost type.ico',
    'dragon': 'Dragon type.ico',
    'dark': 'Dark type.ico',
    'steel': 'Steel type.ico',
    'fairy': 'Fairy type.ico'
}




def createPokemon(pokemon_name):
    # The API request is case sensitive  
    pokemon_name = pokemon_name.lower()

    # Make the API request
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        pokemon_data = response.json()

        # Extract the name
        name = pokemon_data['name'].capitalize()
        print("Name:", name)

        # Extract the types
        types = [type['type']['name'] for type in pokemon_data['types']]
        type_images = [type_mappings.get(t, '') for t in types]
        print("Type(s):", types)
        print("Type Images:", type_images)

        # Extract the index
        index = pokemon_data['id']
        print("Index:", index)

        # Extract the image URL
        image_url = pokemon_data['sprites']['front_default']
        print("Image URL:", image_url)
        
       # Extract the moves
        moves = []
        for move in pokemon_data['moves']:
            move_name = move['move']['name']
            
    
             # Add the move attributes as a dictionary to the moves list
            moves.append({
                'name': move_name,
            })
        
        pokemon = Pokemon(index, name, types, type_images, image_url, moves)
        return pokemon


class Pokemon:
    def __init__(self, index, name, types, type_images, image, moves):
        self.index = index
        self.name = name
        self.types = types
        self.type_images = type_images
        self.image = image
        self.moves = moves
