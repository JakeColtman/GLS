from Connections.Telegram import TelegramStream

stream = TelegramStream().get_messages()
print(stream)