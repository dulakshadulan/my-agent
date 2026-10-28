import os 
from dotenv import load_dotenv
from google import genai
from .Provider import ProviderClass

load_dotenv()

class GeminiProvider(ProviderClass):
    def __init__(self  ):
        self.GEMINI_API = os.getenv("GEMINI_API_KEY")
        self.model = "gemini-flash-latest"
        self.client = genai.Client(api_key=self.GEMINI_API)

    async def model_call(
            self,
            message : dict ):

        interaction  = self.client.interactions.create(
                model=self.model,
                input=message
            )
        return interaction.output_text
        
