## 2. API Authentication ##

# Create a dictionary of headers, with our Authorization header.
headers = {"Authorization": "token 1f36137fbbe1602f779300dad26e4c1b7fbab631"}

# Make a GET request to the Github API with our headers.
# This API endpoint will give us details about Vik Paruchuri.
response = requests.get("https://api.github.com/users/VikParuchuri", headers=headers)

# Print the content of the response.  As you can see, this token is associated with the account of Vik Paruchuri.
print(response.json())

response_2 = requests.get("https://api.github.com/users/VikParuchuri/orgs", headers=headers)
orgs = response_2.json()

## 3. Endpoints and objects ##

# headers is loaded in.
response = requests.get("https://api.github.com/users/torvalds", headers=headers)
torvalds = response.json()


## 4. Other objects ##

# Enter your answer here.
response = requests.get("https://api.github.com/repos/octocat/Hello-World", headers=headers)
hello_world = response.json()

## 5. Pagination ##

params = {"per_page": 50, "page": 1}
response = requests.get("https://api.github.com/users/VikParuchuri/starred", headers=headers, params=params)
page1_repos = response.json()

params2 = {"per_page":50, "page":2}
response_2 = requests.get("https://api.github.com/users/VikParuchuri/starred", headers=headers, params=params2)
page2_repos = response_2.json()

## 6. User-level endpoints ##

# Enter your code here.
response = requests.get("https://api.github.com/user", headers=headers)
user = response.json()

## 7. POST requests ##

# Create the data we'll pass into the API endpoint.  This endpoint only requires the "name" key, but others are optional.
payload = {"name": "test"}

# We need to pass in our authentication headers!
response = requests.post("https://api.github.com/user/repos", json=payload, headers=headers)
print(response.status_code)

payload_2 = {"name":"learning-about-apis"}
response_2 = requests.post("https://api.github.com/user/repos",json=payload_2,headers=headers)
status=response_2.status_code

## 8. PUT/PATCH requests ##

payload = {"description": "The best repository ever!", "name": "test"}
response = requests.patch("https://api.github.com/repos/VikParuchuri/test", json=payload, headers=headers)
print(response.status_code)

payload_2 = {"description": "Learning about requests!","name":"learning-about-apis"}
#response_2 = requests.patch("https://api.github.com/repos/VikParuchuri/learning-about-apis",json=payload_2,headers=headers)
response_2 = requests.patch("https://api.github.com/repos/VikParuchuri/learning-about-apis", json=payload_2, headers=headers)
status = response_2.status_code

## 9. DELETE requests ##

response = requests.delete("https://api.github.com/repos/VikParuchuri/test", headers=headers)
print(response.status_code)

response_2 = requests.delete("https://api.github.com/repos/VikParuchuri/learning-about-apis",headers=headers)
status = response_2.status_code