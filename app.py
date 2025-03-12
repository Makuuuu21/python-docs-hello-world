from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask App</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
            h1 { color: #333; }
        </style>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>Welcome to my Flask web page.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
