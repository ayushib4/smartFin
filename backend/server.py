from flask import Flask, request

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    try:
        data = request.get_json()  # Get the JSON data from the request
        # Process the data
        # Example: Assuming the JSON data has a 'name' field, return a response with a greeting
        name = data['name']
        greeting = f"Hello, {name}!"
        return {'message': greeting}
    except Exception as e:
        return {'error': str(e)}, 400

if __name__ == '__main__':
    app.run(debug=True)
