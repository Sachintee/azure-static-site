from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Azure Python Web App 🚀</h1><p>Deployment Successful!</p>"

if __name__ == "__main__":
    app.run()
