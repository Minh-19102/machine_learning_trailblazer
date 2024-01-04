import json
import os

data = {
  "remove_list": [],
  "change_list": {}
}

current_dir = os.path.dirname(os.path.abspath(__file__)) 
json_file = os.path.join(current_dir, 'artist_filter2.json')

with open(json_file) as f:
  artists_data = json.load(f)

for key, values in artists_data.items():
  for artist in values:
    
    name = artist.get('name')
    spotify_id = artist.get('spotify_id')
    
    if not spotify_id:
      data['remove_list'].append(name)
  
    elif name and spotify_id:
      data['change_list'][name] = spotify_id

with open('HMN1.json', 'w') as f:
  json.dump(data, f, indent=2)