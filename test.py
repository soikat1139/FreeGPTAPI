
#Test 1 has been successful. The server is running and the API is working.:


from flask import Flask, request, jsonify
from gpt4free import theb



def generate_response(question):
    response = ''
    for token in theb.Completion.create(question):
        response += token
    return response


app = Flask(__name__)

@app.route('/api/get_answer', methods=['POST'])
def handle_request():
    question = request.json.get('question')
    if question:
        answer = generate_response(question)
        response = {'answer': answer}
    else:
        response = {'error': 'Question parameter is missing'}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
















#Test 2 running the server on the cloud: Running but needs some improvement model :GPT 4

# from flask import Flask, request, jsonify
# from gpt4free import forefront
# import subprocess

# token = forefront.Account.create(logging=False)


# def generate_response(question):
#     responsed = ''
#     for response in forefront.StreamingCompletion.create(
# 	token=token,
# 	prompt=question,
# 	model='gpt-4'
# ):


#         responsed += response.choices[0].text


#     return responsed

# app = Flask(__name__)

# @app.route('/api/get_answer', methods=['POST'])
# def handle_request():


#     question = request.json.get('question')


#     if question:


#         answer = generate_response(question)


#         response = {'answer': answer}
#     else:
#         response = {'error': 'Question parameter is missing'}

#         subprocess.Popen(['python', 'test.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     return jsonify(response)


# if __name__ == '__main__':
#     app.run(debug=True, port=5000)



















    #TEST -3 iMPROVSED VERSRIOM


# from flask import Flask, request, jsonify
# from gpt4free import forefront
# import os
# import signal
# token = forefront.Account.create(logging=False)

# def generate_response(question, token):
#     responsed = ''
#     for response in forefront.StreamingCompletion.create(
#         token=token,
#         prompt=question,
#         model='gpt-4'
#     ):
#         responsed += response.choices[0].text
#     return responsed


# app = Flask(__name__)



# @app.route('/api/get_answer', methods=['POST'])
# def handle_request():
#     question = request.json.get('question')
#     if question:
#         answer = generate_response(question, token)
#         response = {'answer': answer}
#     else:
#         response = {'error': 'Question parameter is missing'}
#     os.kill(os.getpid(), signal.SIGTERM) # restart the server
#     return jsonify(response)

# if __name__ == '__main__':
    
#     app.run(debug=True, port=5000)




#Test 4 successful model :GPT 4



# import subprocess
# from flask import Flask, request, jsonify
# import phind

# phind.cf_clearance = 'udysC4S.hzkwj2B_C9iH_yyabFZx84CztXnzCbf64yI-1682568621-0-160'
# phind.user_agent   = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0'

# def phind_get_answer(question:str)->str:
#     # set cf_clearance cookie
#     try:
    
#         result = phind.Completion.create(
#         model  = 'gpt-4',
#         prompt = question,
#         results     = phind.Search.create(question, actualSearch = True),
#         creative    = False,
#         detailed    = False,
#         codeContext = '') 
#         return result.completion.choices[0].text

#     except Exception as e:
#         return 'An error occured, please make sure you are using a cf_clearance token and correct useragent | %s' % e


# app = Flask(__name__)

# @app.route('/api/get_answer', methods=['POST'])
# def handle_request():
#     question = request.json.get('question')
#     if question:
#         answer = phind_get_answer(question)
#         response = {'answer': answer}
#     else:
#         response = {'error': 'Question parameter is missing'}
    
#     # restart the server process
#     subprocess.Popen(['python', 'app.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

#     return jsonify(response)

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)





#Test 4 start from here










# print(response.dict())

# {
#     "response": "...",
#     "links": [...],
#     "extra": {...},
#         "slots": {...}
#     }
# }

# chatbot



# from flask import Flask, request, jsonify


# from gpt4free import you

# # simple request with links and details
# response = you.Completion.create(
#     prompt="hello world",
#     detailed=True,
#     include_links=False, )



# chat = []

# def generate_response(prompt):
#     response = you.Completion.create(
#         prompt=prompt,
#         chat=chat
#         )

#     # print(response.text)


#     chat.append({"question": prompt, "answer": response.text})
#     return response.text

# app = Flask(__name__)

# @app.route('/api/get_answer', methods=['POST'])
# def handle_request():
#     question = request.json.get('question')
#     if question:
#         answer = generate_response(question)
#         response = {'answer': answer}
#     else:
#         response = {'error': 'Question parameter is missing'}
#     return jsonify(response)


# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
 