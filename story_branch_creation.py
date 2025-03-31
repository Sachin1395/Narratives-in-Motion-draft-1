from transformers import pipeline

# # Load a pre-trained story generation model
# generator = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct")
#
# def generate_story_continuations(prompt, max_length=100, num_return_sequences=3):
#     """Generate multiple branches for the next part of the story."""
#     continuations = generator(prompt, max_length=max_length, num_return_sequences=num_return_sequences)
#     return [c['generated_text'] for c in continuations]
#
# # Example story prompt
# story_prompt = "As John opened the mysterious box, he saw something unexpected inside. To be continued..."
#
# # Generate possible story branches
# story_branches = generate_story_continuations(story_prompt)
# for i, branch in enumerate(story_branches, 1):
#     print(f"Branch {i}: {branch}\n")

classifier = pipeline("sentiment-analysis")

res = classifier("I am happy")

print(res)