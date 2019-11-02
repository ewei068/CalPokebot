import pickle
import requests
import os
import time

for i in range(10001, 10019):
    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    move_url = 'https://pokeapi.co/api/v2/move/' + str(i)
    response = requests.get(move_url,headers = headers)
    move_data = response.json()
    move_name = move_data["name"]
    cache_path = 'move_cache'
    dbfile = open(cache_path, 'rb')
    cache = pickle.load(dbfile)
    print(cache.keys())
    dbfile.close()

    if move_name not in cache.keys():
        cache[move_name] = move_data
        os.remove(cache_path)
        dbfile = open(cache_path, 'ab')
        # source, destination
        pickle.dump(cache, dbfile)
        dbfile.close()

    time.sleep(2)