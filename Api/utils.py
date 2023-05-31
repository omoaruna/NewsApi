import requests

home_page_endpoint = "http://127.0.0.1:8000/"

# response = requests.get(home_page_endpoint)

POST_DATA = {
    "title" : "Blog Post 3",
    "content" : "Third blog post",
    "author" : "Omo M.",
    "source" : "CNN"
}
new_post = requests.post(home_page_endpoint,data=POST_DATA)
print(new_post.json())
