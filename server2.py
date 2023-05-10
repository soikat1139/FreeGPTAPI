from flask import Flask, request
from gpt4free import theb

app = Flask(__name__)

@app.route('/question', methods=['POST'])
def answer_question():
    # Get the question from the POST request
    question = request.form['question']
    
    # Generate a response using the GPT-4 API
    response = ''
    for token in theb.Completion.create(question):
        response += token
    
    # Return the response to the client
    return response

if __name__ == '__main__':
    app.run()
