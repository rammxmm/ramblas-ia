from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

def get_ai_response(query):
    client = Groq(api_key="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")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": query
            }
        ],
        model="llama-3.3-70b-versatile"
    )
    return chat_completion.choices[0].message.content

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.form['message']
    response = get_ai_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
