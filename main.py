import pyautogui
import time
import pyperclip
from openai import OpenAI

def is_last_message_not_mine(chat_log, my_name):
    messages = chat_log.strip().split("/2025] ")[-1]
    if my_name in messages:
        return False 
    return True


client = OpenAI(
    api_key = "OPENAI_API_KEY"
)


# Wait for a second before starting
time.sleep(2)

# Click on the icon at (943, 1049)
pyautogui.click(1280, 1050)
time.sleep(1)  # Give some time for the application to open

while True:
    # Click and drag to select text from (711, 137) to (1098, 893)
    pyautogui.moveTo(675, 127)
    pyautogui.mouseDown()
    pyautogui.moveTo(1854, 903, duration=0.5)
    pyautogui.mouseUp()

    # Copy the selected text using Ctrl+C
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2.5)  # Give time for copying
    pyautogui.click(1030, 985)


    # Retrieve the copied text from clipboard
    copied_text = pyperclip.paste()

    if(is_last_message_not_mine(copied_text, "Rahul Shinde")):
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a person named Rahul Shinde in conversation who speaks in hindi as well as english. you are from india and you are a coder, you analyze the chat history and respond with next chat(message only not your name in chat)"},
                {
                    "role": "user",
                    "content": copied_text
                }
            ]
        )

        respose = completion.choices[0].message.content


        pyautogui.click(840, 984)
        time.sleep(0.5)

        # Paste the copied content using Ctrl+V
        pyautogui.write(respose)
        time.sleep(0.5)

        # Press Enter
        pyautogui.press('enter')

