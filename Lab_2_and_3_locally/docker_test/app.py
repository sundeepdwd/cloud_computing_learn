# app.py
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def hello_docker():
    return "<h1>Hello, Docker World!</h1><p>This is running inside a container.</p>"

# Run the app
if __name__ == '__main__':
    # The 'host="0.0.0.0"' part is crucial for Docker.
    # It tells the app to listen on all available network interfaces,
    # not just localhost.
    app.run(debug=True, host='0.0.0.0', port=5000)