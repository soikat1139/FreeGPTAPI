# import library
# from gpt4free import theb

# # simple streaming completion

# while True:
# 	x = input("You:")
# 	for token in theb.Completion.create(x):
# 		print(token, end='', )
       
	
# 	# print("Theb:",response)
# 	print(" ")


# flush=True

# from gpt4free import theb

# x = "Who are you"
# response = ''

# for token in theb.Completion.create(x):
#     response += token

# print(response)



from gpt4free import theb

def generate_response(question):
    response = ''
    for token in theb.Completion.create(question):
        response += token
    return response

# Example usage
question = "Who are you?"
response = generate_response(question)
print(response)

