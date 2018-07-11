# -*- coding: utf-8 -*-

def onQQMessage(bot, contact, member, content):
    if content == '-hello':
        bot.SendTo(contact, '嘴臭风bot登场')
    elif content == '-stop':
        bot.SendTo(contact, '我睡觉惹，，，')
        bot.Stop()