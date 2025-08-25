# Character AI Chat API with Selenium

A simple API that lets you send messages to [Character AI](https://character.ai/) and receive responses automatically.
Built using `Flask` and `undetected-chromedriver` with Chrome.

---

## Features

* Automatically opens Character AI, injects your login cookies.
* Sends any message and waits for the full response.
* Works in **headless** or **non-headless** Chrome mode.
* Simple HTTP POST endpoint to interact programmatically.
* Returns the character's answer as JSON.

---

## Requirements

* **Python 3.10+** installed.
* **Google Chrome** or **Chromium** installed.
* **undetected-chromedriver** installed (`pip install undetected-chromedriver`).
* Internet connection.

---

## Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/Dansvn/characterai-api
cd characterai-api
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your config and cookies

* `config.json` with your character name and chat URL. Example:

```json
{
    "name": "Nishimiya",
    "url": "https://character.ai/chat/qu1XGo1xY-BUsbAovcZhV6Alw_Ln9Y-gBK_5K2GvLQo"
}
```

* `cookies.json` from your logged-in Character AI session.

---

## Running the API

```bash
python main.py
```

If successful, you'll see:

```
Starting browser...
Injecting cookies...
Running server on 0.0.0.0:8000
```

---

## API Usage

### Endpoint: `POST /message`

**Request:**

```bash
curl -X POST http://<your-ip>:8000/message -H "Content-Type: application/json" -d "{\"text\":\"Hello Nishimiya!\"}"
```

**Expected response:**

```json
{
  "Nishimiya": "Hi! Nice to see you again!"
}
```

---

## How It Works

1. Opens Character AI in a Selenium-controlled Chrome browser.
2. Injects cookies to skip login.
3. Waits until the chat page is ready.
4. On each POST request:

   * Sends your message to the character.
   * Waits until the character finishes typing.
   * Returns the full response in JSON.

---

## Notes

I made this really quickly just to have fun chatting with Nishimiya.  
Nothing fancy, just a simple API.  
I don’t plan to continue it seriously, just wanted a quick way to chat through code lol.

---

## Disclaimer

This project is for **educational purposes** only.  
Meta AI's interface may change at any time, breaking the script.

---

## Contact

If you have any questions or need support, feel free to reach out!  
**My social links:** [ayo.so/dansvn](https://ayo.so/dansvn)
