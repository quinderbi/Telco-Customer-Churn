import json
import os

config = {}

relative_path = os.path.join(os.path.dirname(__file__), 'config.json')
with open(relative_path) as f:
    config = json.load(f)