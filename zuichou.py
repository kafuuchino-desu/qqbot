# -*- coding: utf-8 -*-
import random
import time
import yaml
import re
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatterbot = ChatBot(
    '嘴臭机器人',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    # input_adapter='chatterbot.input.TerminalAdapter',
    # output_adapter='chatterbot.output.TerminalAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch'
    ],
    database='C:/Users/Mashiro/.qqbot-tmp/plugins/database.sqlite3'
)
chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train("C:/Users/Mashiro/.qqbot-tmp/plugins/zuichou.yml")
lastContent = {
    'content': "你杀妈吗",
    'member': None
}


def preProcessContent(content):
    regex = r'@\S* |[\[\]]'
    return ''.join(list(filter(lambda x: x != '', re.split(regex, content))))


def onQQMessage(bot, contact, member, content):
    global lastContent
    global chatterbot
    the_content = {'content':preProcessContent(content),'member':member.nick}
    # isMe?
    if bot.isMe(contact, member) or (contact.ctype != 'buddy' and member.qq == bot.conf.qq):
        time.sleep(0.1)
        return
    if the_content['content'] == '':
        return
    try:
        with open("C:/Users/Mashiro/.qqbot-tmp/plugins/zuichou.yml", "a+", encoding="utf-8") as x:
            if lastContent['member'] != '阳炎级' or the_content['member'] != '阳炎级':
                prevContent = "- - " + lastContent['content'] + "\n"
                thisContent = "  - " + the_content['content'] + "\n"
                print(prevContent)
                print(thisContent)
                x.write(prevContent)
                x.write(thisContent)
                x.flush()
        x.close()
    except:
        pass
    # chatterbot.train([lastContent, content])

    lastContent["content"] = the_content["content"]
    lastContent["member"] = member.nick
    if content == '-hello' and member.nick == '骑着考卷兜风':
        bot.SendTo(contact, '嘴臭风bot登场')
    elif '[@ME] ' in content:
        msg = the_content["content"]
        randNum = random.randint(1, 100)
        if randNum < 34:
            if str(msg) != '':
                bot.SendTo(contact, '你@你🐎呢')
            else:
                bot.SendTo(contact, '只@不讲话，真实弱智')
        elif randNum >= 34 and randNum < 67:
            if str(msg) != '':
                bot.SendTo(contact, 'at我讲垃圾话你有病吧')
            else:
                bot.SendTo(contact, 'at我不讲话，真实杀妈怪')

        return

    elif content == '-sleep' and member.nick == '骑着考卷兜风':
        bot.SendTo(contact, '我睡觉惹，，，')
        bot.Stop()

    randNum = random.randint(1, 100)
    print(randNum)
    if randNum < 50:
        try:
            chatterbot.train("C:/Users/Mashiro/.qqbot-tmp/plugins/zuichou.yml")
            naiyou = str(chatterbot.get_response(the_content['content']))
            bot.SendTo(contact, naiyou)
        except(KeyboardInterrupt, EOFError, SystemExit):
            return
