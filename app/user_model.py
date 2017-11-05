from . Category import Category
from . Recipes import Recipes


class User():
    """User model class"""
    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.categories = {}
        self.recipes = {}

    def create_category(self, category_name, category_desc):
        category = Category(category_name, category_desc)
        self.categories[category_name] = []
        return category


    def edit_category(self, old_name, new_name):
        if old_name not in self.categories:
            raise KeyError ("You are trying to edit a none existent category")
        self.categories[new_name] = self.categories.pop(old_name)


    def create_recipe(self, category_name, recipe_name, recipe_steps):
        if category_name not in self.categories:
            raise KeyError("category does not exist")
        recipes = Recipes(recipe_name, recipe_steps)
        result = recipe_steps.split(",")
        self.categories[category_name].append(recipe_name)
        self.recipes[recipe_name] = result
        return recipes  

    
    def edit_recipe_name(self, category, old_recipe_name, new_recipe_name):
        if old_recipe_name not in self.recipes:
            raise KeyError("Recipe does not exist")
        self.recipes[new_recipe_name] = self.recipes.pop(old_recipe_name)
        recipes_list = self.categories[category]
        updated_list = [w.replace(old_recipe_name, new_recipe_name) for w in recipes_list]
        self.categories[category] = updated_list


    def edit_recipe_steps(self, recipe_name, new_steps):
        if recipe_name not in self.recipes:
            raise KeyError("Can't edit steps of non existent recipe")
        resultant_recipe = new_steps.split(",")
        self.recipes[recipe_name] = resultant_recipe
 

    def delete_recipe(self, recipe_name):
        if recipe_name not in self.recipes:
            raise KeyError("Can't delete non existent recipe")
        del self.recipes[recipe_name]




    


