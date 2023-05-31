from flask import Flask, render_template

app = Flask(__name__)
visitors = 0

# Flask routes
@app.route('/')
def index():
    global visitors
    visitors += 1
    return render_template('index.html', visitor_count=visitors)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Add code to retrieve data from the backend
    data = {"example": "data"}
    return data

if __name__ == '__main__':
    app.run()
