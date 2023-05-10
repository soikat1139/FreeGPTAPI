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
#     return jsonify(response)


# if __name__ == '__main__':
#     app.run(debug=True, port=5000)




import subprocess
from flask import Flask, request, jsonify
import phind

phind.cf_clearance = 'udysC4S.hzkwj2B_C9iH_yyabFZx84CztXnzCbf64yI-1682568621-0-160'
phind.user_agent   = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0'

def phind_get_answer(question:str)->str:
    # set cf_clearance cookie
    try:
    
        result = phind.Completion.create(
        model  = 'gpt-4',
        prompt = question,
        results     = phind.Search.create(question, actualSearch = True),
        creative    = False,
        detailed    = False,
        codeContext = '') 
        return result.completion.choices[0].text

    except Exception as e:
        return 'An error occured, please make sure you are using a cf_clearance token and correct useragent | %s' % e


app = Flask(__name__)

@app.route('/api/get_answer', methods=['POST'])
def handle_request():
    question = request.json.get('question')
    if question:
        answer = phind_get_answer(question)
        response = {'answer': answer}
    else:
        response = {'error': 'Question parameter is missing'}
    
    # restart the server process
    subprocess.Popen(['python', 'app.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
