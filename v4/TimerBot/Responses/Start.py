
class Start():
	def __init__(self, Bot, bot, update):
		self.Bot = Bot
		self.bot = bot
		self.update = update
	
	def run(self):
		self.update.reply_text();