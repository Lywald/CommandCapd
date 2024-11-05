import pyautogui
from PIL import Image
import pygetwindow as gw
import io
import base64
from openai import OpenAI



######### WRITE YOUR OWN OPENAI KEY HERE OR IT WON'T WORK
api_key = ""



## Set the API key
client = OpenAI(api_key=api_key)

# Get the active window
active_window = gw.getActiveWindow()

# Get the position and size
if active_window:
    left, top = active_window.topleft
    width, height = active_window.size
else:
    print("No active window found.")

# Take a screenshot of the entire screen
screenshot = pyautogui.screenshot()

screenshot = screenshot.crop((left, top, left+width, top+height))

# Save the screenshot to a BytesIO object
byte_io = io.BytesIO()
screenshot.save(byte_io, format='PNG')

# Convert the BytesIO data to base64
byte_io.seek(0)
base64_encoded_result = base64.b64encode(byte_io.getvalue()).decode('utf-8')

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "If there is a prompt between quotes at the right of 'capd', please answer the prompt to participate in a chat. NEVER say 'It looks like the prompt is...', just assume it is. If there is multiple 'capd', answer the latest only."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_encoded_result}",
                    }
                },
            ],
        }
    ],
    max_tokens=1024,
)

print(response.choices[0].message.content)