from flask import Flask, request
from gpt4free import forefront

app = Flask(__name__)

# Create a Forefront account and get the access token
token = forefront.Account.create(logging=False)

@app.route('/question', methods=['POST'])
def answer_question():
    question = request.json.get('question')
    # Use GPT-4 to generate an answer based on the question
    response = forefront.Completion.create(
        token=token,
        prompt=question,
        model='gpt-4'
    )
    answer = response.choices[0].text.strip()
    return {"answer": answer}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
