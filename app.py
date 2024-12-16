from flask import Flask, render_template, request
from gost import cipher, decipher, hash

app = Flask(__name__)

# Предполагается, что keyForCipherDecipher определен в gost.py
keyForCipherDecipher = b'1234567890abcdef1234567890abcdef'  # Замените на ваш ключ

@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted_message = ""
    decrypted_message = ""
    hashed_message = ""
    hashed_message_d = ""
    
    if request.method == 'POST':
        if 'encrypt' in request.form:
            message = request.form['message_to_encrypt']
            
            # Преобразуем строку в байты
            encrypted_message = cipher(bytes(message, 'utf-8')).hex()  # Шифруем и кодируем в hex
            hashed_message = hash(bytes(message, 'utf-8')).hex()
        elif 'decrypt' in request.form:
            message = request.form['message_to_decrypt']
            # Преобразуем строку в байты
            decrypted_message = decipher(bytes.fromhex(message))  # Дешифруем из hex
            hashed_message_d = hash(decrypted_message.encode('utf-8')).hex()

    return render_template('index.html', 
                           encrypted_message=encrypted_message, 
                           decrypted_message=decrypted_message, 
                           hashed_message = hashed_message,
                           hashed_message_d = hashed_message_d)

if __name__ == '__main__':
    app.run(debug=True)
