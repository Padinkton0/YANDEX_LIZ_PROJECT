import threading
import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def start_flask():
    from main import app
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    flask_thread = threading.Thread(target=start_flask, daemon=True)
    flask_thread.start()
    import time

    time.sleep(10000000)