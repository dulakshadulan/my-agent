from google import genai
from dotenv import load_dotenv
from fastapi import FastAPI
import os

load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key = API_KEY)

app = FastAPI()

# stateless non stream

# response = client.interactions.create(
#     model = "gemini-flash-latest",
#     input = "Hello, how are you?"
# )
# print(response.output_text)

# stateless stream

# stream  = client.interactions.create(
#     model = "gemini-flash-latest",
#     input = "Hello, how are you? give 200 word essay",
#     stream = True
# )

# for event in stream:
#     if getattr(event, "event_type", None) == "step.delta":
#         delta = getattr(event, "delta" , None)
#         if delta and getattr(delta , "type", None) == "text":
#             print(delta.text, end="" ,flush=True)

# stateful

interaction1 = client.interactions.create(
    model="gemini-flash-latest",
    input="Hello, i have 3 pens, 3 books "
)

print(interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-flash-latest", 
    input="i gave away 2 pens , how many i have now ?",
    previous_interaction_id=interaction1.id

)
print(interaction2.output_text)

interaction3 = client.interactions.create(
    model="gemini-flash-latest",
    input="i didn't gave but bought more 3  books , now how much all. also what was my first message ?",
    previous_interaction_id=interaction2.id
)

print(interaction3.output_text)