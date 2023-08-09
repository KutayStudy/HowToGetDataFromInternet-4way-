import requests
import json

#POST
to_do_item = {"userId":2,"title":"my to do","completed": False}
post_url = "https://jsonplaceholder.typicode.com/todos/"
#optional header
headers = {"Content-Type": "application/json"}
#1.
#post_response = requests.post(post_url,json=to_do_item,headers=headers)
#print(post_response.json())
#2.
#post_response = requests.post(post_url,data=json.dumps(to_do_item),headers=headers)
#print(json.dumps(to_do_item))

put_url = "https://jsonplaceholder.typicode.com/todos/15"

#PUT

to_do_item_15 = {"userId" : 2, "title": "put title", "completed": False}
#put_response = requests.put(put_url, json=to_do_item_15)
#print(put_response.json())

#PATCH

to_do_item_patch_15 = {"title": "Patch Test"}
#patch_response = requests.patch(put_url,json=to_do_item_patch_15)
#print(patch_response.json())

#DELETE

#delete_response = requests.delete(put_url)
#print(delete_response.json())
#print(delete_response.status_code)