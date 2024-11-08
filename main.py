import telebot

import config
import extensions

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handler_start_help(message):
    if message.text == '/start':
        bot.send_message(message.chat.id,
                         f'Привет, {message.from_user.first_name}\n\nВот доступные команды:\n{config.help_list}')
    elif message.text == '/help':
        bot.send_message(message.chat.id, f'Список команд:\n{config.help_list}')


@bot.message_handler(commands=['viktorina'])
def handler_quiz(message):
    chat_id = message.chat.id

    config.user_selection[chat_id] = {}
    config.user_selection[chat_id]['викторина'] = []

    bot.send_message(chat_id, 'Начинаем викторину!')
    quiz_questions(message)


@bot.message_handler(commands=['opekun'])
def handler_guardianship_system(message):
    bot.send_message(message.chat.id, config.guardianship_system)


def quiz_questions(message):
    chat_id = message.chat.id

    if message.text != 'Отмена ❌':
        if message.text in config.quiz[list(config.quiz.keys())[len(config.user_selection[chat_id]['викторина'])]]:
            config.user_selection[chat_id]['викторина'].append(message.text)

        question_list = list(config.quiz.keys())
        current_index = len(config.user_selection[chat_id]['викторина'])

        if current_index != len(question_list):
            current_question = question_list[current_index]

            keyboard = telebot.types.InlineKeyboardMarkup()
            for i in range(0, len(config.quiz[current_question]), 2):
                if i + 1 < len(config.quiz[current_question]):
                    keyboard.add(telebot.types.KeyboardButton(config.quiz[current_question][i]),
                                 telebot.types.KeyboardButton(config.quiz[current_question][i + 1]))
                else:
                    keyboard.add(telebot.types.KeyboardButton(config.quiz[current_question][i]))
            keyboard.add('Отмена ❌')
            bot.send_message(chat_id, f'{current_question}', reply_markup=keyboard)

            bot.register_next_step_handler(message, quiz_questions)
        else:
            users_quiz_result = extensions.quiz_result(config.user_selection[chat_id]['викторина'])
            del config.user_selection[chat_id]

            bot.send_message(message.chat.id, 'Результат:', reply_markup=telebot.types.ReplyKeyboardRemove())

            keyboard = telebot.types.InlineKeyboardMarkup()
            button_1 = telebot.types.InlineKeyboardButton('Повторить', callback_data='repeat_quiz')
            button_2 = telebot.types.InlineKeyboardButton('Поделиться', callback_data='share_quiz')
            keyboard.add(button_1, button_2)
            keyboard.add(telebot.types.InlineKeyboardButton('Стать опекуном (Узнать подробнее)',
                                                            callback_data='guardianship_system'))

            with open(users_quiz_result['photo'], 'rb') as photo_file:
                bot.send_photo(chat_id, photo_file, caption=users_quiz_result['text'], reply_markup=keyboard)
    elif message.text == 'Отмена ❌':
        del config.user_selection[chat_id]
        bot.send_message(message.chat.id, 'Отмена', reply_markup=telebot.types.ReplyKeyboardRemove())


@bot.message_handler(content_types=['text'])
def handler_text(message):
    bot.send_message(message.chat.id, 'ok')


@bot.callback_query_handler(func=lambda call: True)
def repeat_quiz(call):
    if call.data == 'repeat_quiz':
        handler_quiz(call.message)
    elif call.data == 'guardianship_system':
        handler_guardianship_system(call.message)
    elif call.data == 'share_quiz':
        bot.send_message(call.message.chat.id, 'Жаль не знаю как "-_-')


bot.polling(none_stop=True)