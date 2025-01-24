import os
import base64
import litellm
import mimetypes
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

prompt = 'Can you tell me the name of this meme template?'

# Get absolute path and encode the image
media_path = './meme.jpg'
with open(media_path, 'rb') as media_file:
    media_data = base64.b64encode(media_file.read()).decode('utf-8')

# Create the messages payload according to the documentation
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": prompt
            },
            {
                "type": "image_url",
                "image_url": {"url": f"data:{mimetypes.guess_type(media_path)[0]};base64,{media_data}"}
            }
        ]
    }
]

# Make the API call to Gemini model
response: litellm.ModelResponse = litellm.completion(
    model="gemini/gemini-2.0-flash-exp",
    messages=messages,
    api_key=os.getenv('GEMINI_API_KEY')
)

# Extract the response content
content = response.choices[0].message.content
finish_reason = response.choices[0].finish_reason