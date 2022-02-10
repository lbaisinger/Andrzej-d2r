import importlib

confname = 'bajsi_laptop'
modulename = ('player_configs.config_' + confname)
config = importlib.import_module('player_configs.config_' + confname)
