from scraper import *

import telebot
bot = telebot.TeleBot("1419760780:AAGHrfGtzeodj_u3qV9CoIhuOy4wZ2sTi8g")

#Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
	bot.reply_to(message, "Please reply with one of these commands:\n\n/hackathons - To get a list of latest Hackathons\n\n/workshops - To get a list of latest Workshops\n\n/internships - To get a list of latest Internships\n\n/scholarships - To get a list of latest scholarships\n\n/quizzes - To get a list of latest Quizzes\n\n/competitions - To get a list of latest Competitions\n\n/cultural - To get a list of latest Cultural Events\n\n/festivals - To get a list of latest College Fests\n\n/articles - To get a list of latest Articles\n")

#This handler will handle all the event commands
@bot.message_handler(commands=['hackathons','workshops','internships','scholarships','quizzes','competitions','cultural','festivals'])
def fetch_college_events(message):
	final_msg = ""
	ctr = 1
	category = message.text[1:]
	data = scrape_website_events(category)
	for each in data:
		final_msg = final_msg + str(ctr)+". "+each['title']+"\n"+each['organisation']+"\n"+each['date']+"\n"+each['link']+"\n\n"
		ctr = ctr+1
	bot.reply_to(message, final_msg)

#This handler will handle all the article commands
@bot.message_handler(commands=['articles'])
def fetch_college_articles(message):
	final_msg = ""
	ctr = 1
	category = message.text[1:]
	data = scrape_website_articles(category)
	for each in data:
		final_msg = final_msg +str(ctr)+". "+each['title']+"\n"+each['description']+"\n"+each['link']+"\n\n"
		ctr = ctr+1
	bot.reply_to(message, final_msg)

bot.polling()