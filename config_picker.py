import importlib

confname = 'laptop_bajs'
modulename = ('player_configs.config_' + confname)
config = importlib.import_module('player_configs.config_' + confname)
