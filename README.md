# recipeFinder

Communication contract microservice A

Instructions for how to REQUEST data from the recipe finder microservice :
  You must open recipes.txt file and write down the title for the recipe you want to get. Then add a sleep time for 5 seconds.
  Example:
  with open ("recipes.txt", "w") as recipes:
  recipes.write("lasagne")
  time.sleep(5)


Instructions for how to  RECEIVE data from the recipe finder microservice :
  After waiting 5 seconds, then read the recipes.txt file and you will get 1+ recipes to choose from for your program.
  Example:
  with open ("recipes.txt", "r") as recipe_file:
  recipes = recipe_file.read()


UMI:
![UMI](https://github.com/Guibely/recipeFinder/assets/107956206/713e46a2-e316-4bed-8179-35e24dbe6cea)

