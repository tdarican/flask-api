from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

def create_driver():
    options = Options()
    options.add_argument('--headless')  # Tarayıcıyı gizli modda çalıştır
    options.add_argument('--no-sandbox')  # Sandbox hatalarını önle
    options.add_argument('--disable-dev-shm-usage')  # Bellek hatalarını önle
    driver = webdriver.Chrome(options=options)
    return driver

@app.route('/instagram/<username>')
def get_instagram_post(username):
    driver = create_driver()
    driver.get(f'https://www.instagram.com/{username}/')
    
    # Sayfa yüklendikten sonra son gönderiyi çek
    try:
        post_link = driver.find_element(By.XPATH, '//article//a').get_attribute('href')
        driver.quit()  # İşlem bitince tarayıcıyı kapat
        return jsonify({'post_url': post_link})
    except Exception as e:
        driver.quit()  # Hata durumunda da tarayıcıyı kapat
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
