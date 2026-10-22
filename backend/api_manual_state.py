from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ.get("GEMINI_API_KEY")

client = genai.Client()
MODEL = "gemini-flash-latest"

history = [
    {
        "type" : "user_input",
        "content": [{"type" : "text" , "text":"I have 2 dogs"}]
    }
]

interaction1 = client.interactions.create(
    model=MODEL ,
    input=history,
    store=False    
)

response = interaction1.output_text
print("Response : ",interaction1.output_text)

for step in interaction1.steps:
    history.append(step.model_dump())

history.append({

        "type" : "user_input",
        "content": [{"type" : "text" , "text":"you name them"}]
    
})

interaction2 = client.interactions.create(
    model="gemini-flash-latest",
    store=False,
    input = history
)
print(interaction2.output_text)