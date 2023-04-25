from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

import os

# Creating a chatbot Instance
bot = ChatBot('Buddy',
            logic_adapters=['chatterbot.logic.MathematicalEvaluation','chatterbot.logic.TimeLogicAdapter',
            {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Muh dho ke aa',
            'maximum_similarity_threshold': 0.90
            }],
            read_only = True,
            preprocessors=['chatterbot.preprocessors.clean_whitespace',
                        'chatterbot.preprocessors.unescape_html',
                        'chatterbot.preprocessors.convert_to_ascii']
                        )

# locate training folder
directory = 'training_data'

for filename in os.listdir(directory):
    if filename.endswith(".txt"): # only pick txt file for training
        print('\n Chatbot training with '+os.path.join(directory, filename)+' file')
        training_data = open(os.path.join(directory, filename)).read().splitlines()
        trainer = ListTrainer(bot) # bot training
        trainer.train(training_data)
    else:
        continue

# user choose whether to train with English corpus data
decision1 = input('Train chatbot with English corpus data? (Y/N): ')

if decision1 == 'Y' or decision1 == 'y':
    print('\n Chatbot training with English corpus data')
    trainer_corpus = ChatterBotCorpusTrainer(bot)
    trainer_corpus.train('chatterbot.corpus.english')

decision2 = input("Train chatbot with the necessary corpus dataset? (Y/N):")

if decision2 == 'Y' or decision2 == 'y':
    print('\n Chatbot training on large corpus data')
