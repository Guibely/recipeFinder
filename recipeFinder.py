import requests


def recipe_search(recipe_title):
    id = '3359ddd1'
    key = 'c14afc936b3b59c63f35fc940670a386	'
    url = f'https://api.edamam.com/search?q={recipe_title}&app_id={id}&app_key={key}'

    response = requests.get(url)
    data = response.json()

    if 'hits' in data:
        recipes = data['hits']
        for recipe in recipes:
            recipe_name = recipe['recipe']['label']
            recipe_url = recipe['recipe']['url']
            name = f"Recipe: {recipe_name}"
            link = f"URL: {recipe_url}"
            with open("recipes.txt", "a") as recipe_file:
                recipe_file.write(name + link+"\n")
    else:
        print("No recipes found.")


title = open("recipes.txt", "r")
recipe = title.read()
recipe_search(recipe)
