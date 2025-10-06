import os
from google import genai
# Note: You do NOT need the `openai` library or an `openai.api_key` line anymore.

# The client automatically reads the key from the GEMINI_API_KEY
# environment variable.
client = genai.Client()

def chat_with_gemini(prompt):
    # Use the client to call the generate_content method
    response = client.models.generate_content(
        model="gemini-2.5-flash", # A fast, modern, and cheap model
        contents=[{"role": "user", "parts": [{"text": prompt}]}]
    )
    # The response object structure is simpler than OpenAI's
    return response.text

if __name__ == "__main__":
    try:
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit", "bye"]:
                break
            response = chat_with_gemini(user_input) # Assuming you are now using Gemini
            print("Chatbot: ", response)
    except KeyboardInterrupt:
        # This message will be displayed instead of the traceback
        print("\nChatbot: Goodbye!")