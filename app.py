from flask import Flask, jsonify
from playwright.sync_api import sync_playwright

app = Flask(__name__)

@app.route('/instagram/<username>')
def fetch_instagram(username):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"https://www.instagram.com/{username}/", timeout=60000)
        page.wait_for_timeout(3000)
        html = page.content()
        browser.close()
        return jsonify({"html": html})

if __name__ == '__main__':
    app.run()
