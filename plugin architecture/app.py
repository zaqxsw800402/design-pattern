import json
import factory
import importlib


def load_plugin(plugin_file: str) -> None:
    plugin = importlib.import_module(plugin_file)
    plugin.register()


factory.register('Taiwan', factory.Taiwan)
factory.register('HongKong', factory.HongKong)

with open("data.json") as file:
    data = json.load(file)
    characters = data['data']

    for plugin_file in data['plugins']:
        load_plugin(plugin_file)

    character_list = [factory.create(character) for character in characters]

    for character in character_list:
        character.say_hi()
