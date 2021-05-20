from telegram.ext import Updater, CommandHandler


def start(update, context):
	
	update.message.reply_text('Hola, humano')


if __name__ =='__main__':

	updater = Updater(token='1788680064:AAGLELV5ne0mk4epEFeIFtdqbC7ARxVhZM4', use_context=True

	dp = updater.dispatcher
	
	dp.add_handler(CommandHandler('Start',start))
	
	update.start_polling()
	updater.idle()

	


