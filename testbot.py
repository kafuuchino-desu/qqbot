# chatterbotfrom chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
#
# bot = ChatBot(
#     "嘴臭机器人",
#     storage_adapter='chatterbot.storage.SQLStorageAdapter',
#     # input_adapter='chatterbot.input.TerminalAdapter',
#     # output_adapter='chatterbot.output.TerminalAdapter',
#     logic_adapters=[
#         'chatterbot.logic.MathematicalEvaluation',
#         'chatterbot.logic.BestMatch'
#     ],
#     database='./test.sqlite3'
# )
# bot.set_trainer(ListTrainer)
# # bot.train([
# #     'How are you?',
# #     'I am good.',
# #     'That is good to hear.',
# #     'Thank you',
# #     'You are welcome.',
# # ])
# while True:
#     try:
#         a = input()
#         bot_output = bot.get_response(a)
#         print(type(bot_output))
#         print(str(bot_output))
#     except(KeyboardInterrupt, EOFError, SystemExit):
#         break

print(a)