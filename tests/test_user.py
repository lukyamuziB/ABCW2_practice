from app.user_model import User

import pytest
@pytest.fixture
def user_agent():
	user = User("Ben","Ben12","ben0","password")
	user.create_category("Samosa","They look like triangles")
	user.create_recipe("Samosa", "sangala", "agian, like triangles")
	return user


def test_user_cant_miss_args():
	with pytest.raises(TypeError):
		user = User("a")

def test_user_args_are_strings():
	with pytest.raises(TypeError):
		user = User(1,3,"ui",[7.0,9])


def test_user_can_make_recipe(user_agent):
	a = user_agent.edit_category("Samosa", "guy")
	assert a == "guy"

def test_user_can_delete_recipe(user_agent):
	result = user_agent.delete_recipe("sangala")
	assert "sangala" not in user_agent.recipes


def test_user_can_delee_recipe(user_agent):
	with pytest.raises(KeyError):
		result = user_agent.edit_category("blahh", "laahhh")


@pytest.mark.parametrize("new, old, desc",[("blah","jah","sydgybdysg"),\
	                    ("buy","get","yugacysbdtyug"),("hdshg","dgysgyg","gdyvgv")])
def test_edit_category(new, old, desc):
	user = User("a","b","c","d")
	a = user.create_category(new,desc)
	b = user.edit_category(new, old)
	assert old in user.categories 


@pytest.mark.parametrize("category, desc, name, new_name",[("salads","kjhjh","cucumber","cabbage"),\
	                     ("soups","hhfbfs", "mash soup", "carrot_soup")])
def test_user_can_edit_recipe(category, desc, name, new_name):
	user = User("a","b","c","d")
	user.create_category(category, desc)
	user.create_recipe(category, name, desc)
	user.edit_recipe_name(name, new_name)
	assert new_name in user.recipes


def test_user_cant_delete_non_existent_recipe(user_agent):
	with pytest.raises(KeyError):
		user_agent.delete_recipe("ANDELA")


def test_for_category_datatype(user_agent):
	with pytest.raises(TypeError):
		user_agent.create_category(1,9)
		user_agent.edit_recipe_name("sangala","lorem ipsum")
		user_agent.create_recipe('Samosa','b','c')









