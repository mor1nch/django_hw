from flask import Flask

app = Flask(__name__)

local_page_path = 'index.html'

with open(local_page_path, 'r', encoding='utf-8') as file:
    local_page_content = file.read()


@app.route('/')
def index():
    return local_page_content


if __name__ == '__main__':
    app.run(debug=True)