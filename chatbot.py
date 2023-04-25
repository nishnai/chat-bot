from chatterbot import ChatBot

bot = ChatBot(name='Buddy',
            logic_adapters=['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.TimeLogicAdapter',
            {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
            }],
            read_only = True,
            preprocessors=['chatterbot.preprocessors.clean_whitespace',
                        'chatterbot.preprocessors.unescape_html',
                        'chatterbot.preprocessors.convert_to_ascii']
                        )


# run and get response from user.
name = input('Enter Your Name: ')

print ('Welcome to ChatBotv2.0! Let me know how can I help you.')

while True:

    request = input(name+': ')

    if request == "Bye" or request == 'bye' or request == 'BYE':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot: ', response)