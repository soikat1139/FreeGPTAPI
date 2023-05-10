from gpt4free import forefront
# create an account
token = forefront.Account.create(logging=False)
print(token)
#get a response
for response in forefront.StreamingCompletion.create(
	token=token,
	prompt='Who are You',
	model='gpt-4'
):
    print(response.choices[0].text )
print("")

# flush=True