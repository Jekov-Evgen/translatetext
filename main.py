from flask import Flask
import urls

app = Flask(__name__)
urls.init_routes(app)

if __name__ == "__main__":
    app.run(debug=True)

