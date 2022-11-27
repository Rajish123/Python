import requests
import pprint
import pandas as pd

api_key = "4f975953ce8bc449a5970f7918c5583d"
api_key_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0Zjk3NTk1M2NlOGJjNDQ5YTU5NzBmNzkxOGM1NTgzZCIsInN1YiI6IjYzODM1ZjcxMmUwNjk3MDI5MmUzYjExYyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.3v_-V6FWmJ3IbMTPzMXGuIvEfOpLsAOcLV8OybajWT0"


# version 3
# movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
search_query = "The Matrix"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"
r = requests.get(endpoint)
# print(r.status_code)
# pprint.pprint(r.text)
# print(r.json())
if r.status_code in range(200,299):
    data = r.json()
    results = data["results"]
    if len(results) > 0:
        movie_ids = set()
        for result in results:
            _id = result['id']
            # print(result['title'],_id)
            movie_ids.add(_id)
        # print(list(movie_ids))
        
movie_data = []
output = "movies.csv"
for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200,299):
        data = r.json()
        movie_data.append(data)
        
df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output,index=False)

#version 4
# movie_id = 501
# api_version= 4
# api_base_url = f"https://api.themoviedb.org/{api_version}"
# endpoint_path = f"/movie/{movie_id}"
# endpoint = f"{api_base_url}{endpoint_path}"
# headers = {
#     'Authorization': f'Bearer {api_key_v4}',
#     'Content-Type': 'application/json;charset=utf-8'
# }
# r = requests.get(endpoint,headers=headers)

# print(f"status code is {r.status_code}")    
# print(r.text)

