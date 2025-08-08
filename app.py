from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the Flask application instance
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Create the Flask application instance
app = Flask(__name__)

# ... the rest of your app.config code ...
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the database model
class GameHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_text = db.Column(db.String(500), nullable=False)
    binary_stream = db.Column(db.String(5000), nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

# Create a simple route for the home page
@app.route('/')
def index():
    return render_template('index.html') # NEW: Render the HTML file

# Command to create the database tables
with app.app_context():
    db.create_all()

# Run the app if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)