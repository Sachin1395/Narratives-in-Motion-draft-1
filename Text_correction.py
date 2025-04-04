import google.generativeai as genai

genai.configure(api_key="AIzaSyA-UjYFpBvXHa7EEXPgVTKB5DuQF8h9wWs")
model = genai.GenerativeModel("gemini-1.5-flash")

def correct (content):
    response = model.generate_content(f"{content}: this is the content of the story that is going to be posted on a story telling website. So correct only the grammatical errors without changing the content's meaning ")
    return response.text

def generate (comments,content):
    branches = model.generate_content(f"{comments}: this is the comments of the given story :{content}. Generate 3 story branches to continue the next part along with the % of interest on each of the branches based on the comments.Remove any unicode characters in the output and use only  ascii that are in range 128 ")
    return branches.text

