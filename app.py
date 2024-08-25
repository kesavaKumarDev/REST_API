from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def post_endpoint():
    try:
        data = request.get_json()
        user_id = "john_doe_17091999"  # Replace with your actual user ID logic
        
        numbers = data.get('numbers', [])
        alphabets = data.get('alphabets', [])
        
        if not isinstance(numbers, list) or not isinstance(alphabets, list):
            return jsonify({"is_success": False, "error": "Invalid input format"}), 400
        
        # Find highest lowercase alphabet
        highest_lowercase = [ch for ch in alphabets if ch.islower()]
        highest_lowercase.sort(reverse=True)
        
        response = {
            "is_success": True,
            "user_id": user_id,
            "college_email_id": data.get("college_email_id", ""),
            "college_roll_number": data.get("college_roll_number", ""),
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

@app.route('/bfhl', methods=['GET'])
def get_endpoint():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
