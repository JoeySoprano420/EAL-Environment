from flask import Flask, render_template, request, jsonify
import subprocess
import logging
from logging.handlers import RotatingFileHandler
from werkzeug.middleware.proxy_fix import ProxyFix
from code_executor import CodeExecutor

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)  # Fix for handling proxy headers

# Configure logging
handler = RotatingFileHandler('app.log', maxBytes=1000000, backupCount=5)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)

executor = CodeExecutor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    data = request.json
    code = data.get('code', '')
    try:
        result = executor.execute_code(code)
        return jsonify(result)
    except Exception as e:
        app.logger.error(f"Execution failed: {str(e)}")
        return jsonify({"status": "error", "output": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
