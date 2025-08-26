from flask import Flask, request, jsonify
import json
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc

port = 8000
app = Flask(__name__)

with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

with open('cookies.json', 'r', encoding='utf-8') as f:
    cookies = json.load(f)

print("Starting browser...")
driver = uc.Chrome()
driver.get("https://character.ai")
time.sleep(3)

print("Injecting cookies...")
for cookie in cookies:
    cookie.pop('sameSite', None)
    try:
        driver.add_cookie(cookie)
    except:
        pass

driver.get(config['url'])
time.sleep(5)

read_messages = []

def get_full_text(element):
    return driver.execute_script("""
        const e = arguments[0];
        return e.innerText || e.textContent || "";
    """, element).strip()

def send_message(message_text, timeout=30):
    print(f"[SENDING] {message_text}")
    textarea = driver.find_element(By.TAG_NAME, 'textarea')
    textarea.send_keys(message_text)
    textarea.send_keys(Keys.ENTER)

    start_time = time.time()
    while True:
        if time.time() - start_time > timeout:
            print("[WARNING] Timeout esperando resposta.")
            return ""

        slides = driver.find_elements(By.CSS_SELECTOR, '.swiper-slide-visible, .swiper-slide-active')
        for slide in slides[::-1]:
            try:
                message_element = slide.find_element(By.CSS_SELECTOR, '[data-testid="completed-message"]')
                previous_text = ""
                stable_counter = 0
                full_text = ""
                while True:
                    current_text = message_element.text.strip()
                    if current_text == previous_text and current_text != "":
                        stable_counter += 0.3
                        if stable_counter >= 1.0:
                            full_text = current_text
                            break
                    else:
                        stable_counter = 0
                        previous_text = current_text
                    time.sleep(0.3)

                if full_text not in read_messages:
                    read_messages.append(full_text)
                    print(f"[RECEIVED] {full_text}")
                    return full_text
            except:
                continue

        time.sleep(0.5)


@app.route("/message", methods=["POST"])
def respond():
    data = request.json
    message_text = data.get("text", "")
    reply = send_message(message_text)
    return jsonify({config['name']: reply})

if __name__ == "__main__":
    print(f"Running server on 0.0.0.0:{port}")
    app.run(host="0.0.0.0", port=port, debug=True, use_reloader=False)

