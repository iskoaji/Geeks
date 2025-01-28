from django.core.management.base import BaseCommand
from apps.main.service import bot


class Command(BaseCommand):
    help = 'bot'
    
    def handle(self, *args, **options):
        print("START TELEGRAM BOT")
        bot.polling(none_stop=True, interval=0)

    def __str__(self):
        return self.title





# from django.core.management.base import BaseCommand
# from apps.main.service import bot
# from dotenv import load_dotenv
# import logging
# import time

# load_dotenv()

# # Настройка логирования
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# class Command(BaseCommand):
#     help = 'Запуск Telegram-бота'

#     def handle(self, *args, **options):
#         logger.info("Запуск Telegram-бота...")
#         while True:
#             try:
#                 bot.polling(none_stop=True, interval=1)
#             except Exception as e:
#                 logger.error(f"Ошибка в работе бота: {e}")
#                 time.sleep(3)  # Ожидание перед повторной попыткой