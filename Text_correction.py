import google.generativeai as genai

genai.configure(api_key="AIzaSyA-UjYFpBvXHa7EEXPgVTKB5DuQF8h9wWs")
model = genai.GenerativeModel("gemini-1.5-flash")

def correct (content):
    response = model.generate_content(f"{content}: this is the content of the story that is going to be posted on a story telling website. So correct only the grammatical errors without changing the content's meaning ")
    return response.text

def generate (comments,content):
    brancehs = model.generate_content(f"{comments}: this is the comments of the given story :{content}. Generate 3 story branches to continue the next part along with the % of interest on each of the branches based on the comments. Give output in this format : branch i : branch content,%interest of branch i :  x%")
    return brancehs.text

# br = generate("This sent chills down my spine. What’s in the engraving? Who’s outside?! I need answers!,The atmosphere is perfectly haunting, but I hope there’s a twist ahead—maybe it’s someone he knows? ,I bet the locket holds a key to Sam’s past. Or maybe I’m overthinking it. Either way, I want more!","The lantern flickered softly, casting restless shadows across the walls of the abandoned cabin. Sam tightened his grip on the rusted locket he had just found beneath the floorboards. It wasn’t his. It shouldn’t have been there. As he flipped it open, the engraving inside made his breath hitch—three words etched so faintly they almost disappeared with each blink. Footsteps echoed outside, growing louder. Sam froze. Who could possibly know he was here?")
#
# print(br)