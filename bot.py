#!/usr/bin/env python

# -*- coding: utf-8 -*-
import telebot
import subprocess

#users = [1234556]
token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def stats(message):
    answer = "Just input any email or username! (messages are limited to 10 lines, csv file is limited to 100 lines) Good luck! ;)"
    bot.send_message(message.chat.id,  answer)

#@bot.message_handler(func=lambda message: message.chat.id not in users)
#def some(message):
#    bot.send_message(message.chat.id, "s0rry ur not acc3pt3d!")

@bot.message_handler(regexp=r'''^[@*"'.,:;|/\\]{1,50}$''')
def stats(message):
    answer = "r u sure, man?"
    bot.send_message(message.chat.id, answer)

@bot.message_handler(regexp=r'''[\t\s]{1,50}''')                                                                                            
def stats(message):                                                                                                                                   
    answer = "bad request, man"                                                                                                                         
    bot.send_message(message.chat.id, answer)   
    

@bot.message_handler(regexp="^[\w][\w@.]{1,50}$")
def command_default(message):
    splunksdk = subprocess.Popen('python search.py --timeout=10 "search index="bazas" %s | table username email password hint sourcetype | rename sourcetype AS database | head 100 " --output_mode=csv > result.csv && cat result.csv | head -n 10' % message.text, shell=True, stdout=subprocess.PIPE).stdout.read().decode("utf-8")
    if len(splunksdk) > 1:
      answer = 'What splunk found: ' +splunksdk
      bot.send_message(message.chat.id,  answer)
      doc = open('result.csv', 'rb')
      bot.send_document(message.chat.id, doc)
    else:
  bot.send_message(message.chat.id, "n0thing f0und :c") 
  
if __name__ == '__main__':
     bot.polling(none_stop=True)
