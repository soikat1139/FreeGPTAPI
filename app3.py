from gpt4free.quora import Poe

# available models:  ['Sage', 'GPT-4', 'Claude+', 'Claude-instant', 'ChatGPT', 'Dragonfly', 'NeevaAI']

poe = Poe(model='ChatGPT', driver='firefox', cookie_path='cookie.json', driver_path='path_of_driver')
poe.chat('who won the football world cup most?')

# new bot creation
poe.create_bot('new_bot_name', prompt='You are new test bot', base_model='gpt-3.5-turbo')

# delete account
poe.delete_account()