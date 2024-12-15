from flask import Flask, render_template, request
from gost import cipher, decipher

app = Flask(__name__)

# Предполагается, что keyForCipherDecipher определен в gost.py
keyForCipherDecipher = b'1234567890abcdef1234567890abcdef'  # Замените на ваш ключ

@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted_message = ""
    decrypted_message = ""
    
    if request.method == 'POST':
        if 'encrypt' in request.form:
            message = request.form['message_to_encrypt']
            # Преобразуем строку в байты
            encrypted_message = cipher(bytes(message, 'utf-8')).hex()  # Шифруем и кодируем в hex
        elif 'decrypt' in request.form:
            message = request.form['message_to_decrypt']
            # Преобразуем строку в байты
            decrypted_message = decipher(bytes.fromhex(message))  # Дешифруем из hex

    return render_template('index.html', 
                           encrypted_message=encrypted_message, 
                           decrypted_message=decrypted_message)

if __name__ == '__main__':
    app.run(debug=True)
