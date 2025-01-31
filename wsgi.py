from app import app  # app.py'deki Flask uygulamasını içe aktar
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render.com'un beklediği port
    app.run(host='0.0.0.0', port=port)