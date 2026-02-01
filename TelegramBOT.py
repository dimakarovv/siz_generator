import telebot

TOKEN = "8588192735:AAFS1MUM5LINj6hWIpe8f6xgfKs9UyosC_c"
bot = telebot.TeleBot(TOKEN)

# Словарь для хранения выбранных условий пользователя
user_conditions = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = """Привет, я твой помощник в сфере Техносферной безопасности. Я могу:

• Рассчитать нормы выдачи СИЗ
• Помочь вспомнить терминологию
• Найти соответствующий закон

Выбери, что тебя интересует:"""

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("📋 Расчет СИЗ")
    btn2 = telebot.types.KeyboardButton("📚 Терминология")
    btn3 = telebot.types.KeyboardButton("⚖️ Законодательство")

    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)


@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """Доступные команды:
/start - Начать работу с ботом
/help - Справка

Основные функции:
📋 Расчет СИЗ - Рассчитать нормы выдачи средств индивидуальной защиты
📚 Терминология - Справочник терминов в области техносферной безопасности
⚖️ Законодательство - Информация о соответствующих законах и нормативах"""

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn_start = telebot.types.KeyboardButton("Начать")
    btn_help = telebot.types.KeyboardButton("Помощь")

    markup.add(btn_start, btn_help)
    bot.send_message(message.chat.id, help_text, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Начать")
def on_start_button(message):
    send_welcome(message)


@bot.message_handler(func=lambda message: message.text == "Помощь")
def on_help_button(message):
    send_help(message)


@bot.message_handler(func=lambda message: message.text == "📋 Расчет СИЗ")
def calculate_siz(message):
    select_text = "Выбери профессию для расчета СИЗ:"

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    professions = [
        "Сторож (4732)",
        "Водитель автомобиля (783)",
        "Дворник (997)",
        "Электромонтажник по кабельным сетям (5271)",
        "Сварщик арматурных сеток и каркасов (4438)",
        "Повар (3593)",
        "Подсобный рабочий (3640)"
    ]

    for profession in professions:
        markup.add(telebot.types.KeyboardButton(profession))

    # Добавляем кнопку "Назад"
    markup.add(telebot.types.KeyboardButton("◀️ Назад"))

    bot.send_message(message.chat.id, select_text, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "◀️ Назад")
def go_back(message):
    send_welcome(message)


@bot.message_handler(func=lambda message: message.text == "Сторож (4732)")
def select_storozh(message):
    chat_id = message.chat.id
    user_conditions[chat_id] = []

    conditions_text = """Выбери дополнительные условия работы сторожа (можно выбрать несколько):

1.1 Скользкие, обледенелые, зажиренные, мокрые поверхности
1.2 Перепад высот, отсутствие ограждения на высоте
1.3 Груз, инструмент или предмет, перемещаемый или поднимаемый, в том числе на высоту

Или выбери опцию без дополнительных условий:"""

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = telebot.types.KeyboardButton("☑️ 1.1 Скользкие поверхности")
    btn2 = telebot.types.KeyboardButton("☑️ 1.2 Перепад высот")
    btn3 = telebot.types.KeyboardButton("☑️ 1.3 Груз/инструмент")
    btn_no_conditions = telebot.types.KeyboardButton("✅ Без дополнительных условий")

    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn_no_conditions)
    markup.add(telebot.types.KeyboardButton("◀️ Назад"))

    bot.send_message(chat_id, conditions_text, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "☑️ 1.1 Скользкие поверхности")
def add_condition_1_1(message):
    chat_id = message.chat.id
    if chat_id not in user_conditions:
        user_conditions[chat_id] = []

    if "1.1" not in user_conditions[chat_id]:
        user_conditions[chat_id].append("1.1")
        bot.send_message(chat_id, "✅ Условие 1.1 добавлено")
    else:
        user_conditions[chat_id].remove("1.1")
        bot.send_message(chat_id, "❌ Условие 1.1 удалено")

    show_conditions_status(chat_id)


@bot.message_handler(func=lambda message: message.text == "☑️ 1.2 Перепад высот")
def add_condition_1_2(message):
    chat_id = message.chat.id
    if chat_id not in user_conditions:
        user_conditions[chat_id] = []

    if "1.2" not in user_conditions[chat_id]:
        user_conditions[chat_id].append("1.2")
        bot.send_message(chat_id, "✅ Условие 1.2 добавлено")
    else:
        user_conditions[chat_id].remove("1.2")
        bot.send_message(chat_id, "❌ Условие 1.2 удалено")

    show_conditions_status(chat_id)


@bot.message_handler(func=lambda message: message.text == "☑️ 1.3 Груз/инструмент")
def add_condition_1_3(message):
    chat_id = message.chat.id
    if chat_id not in user_conditions:
        user_conditions[chat_id] = []

    if "1.3" not in user_conditions[chat_id]:
        user_conditions[chat_id].append("1.3")
        bot.send_message(chat_id, "✅ Условие 1.3 добавлено")
    else:
        user_conditions[chat_id].remove("1.3")
        bot.send_message(chat_id, "❌ Условие 1.3 удалено")

    show_conditions_status(chat_id)


def show_conditions_status(chat_id):
    conditions = user_conditions.get(chat_id, [])
    status_text = "Выбранные условия:\n"

    if not conditions:
        status_text += "Условия не выбраны\n"
    else:
        for cond in conditions:
            if cond == "1.1":
                status_text += "✅ 1.1 Скользкие, обледенелые, зажиренные, мокрые поверхности\n"
            elif cond == "1.2":
                status_text += "✅ 1.2 Перепад высот, отсутствие ограждения на высоте\n"
            elif cond == "1.3":
                status_text += "✅ 1.3 Груз, инструмент или предмет, перемещаемый или поднимаемый\n"

    status_text += "\nДобавь еще условия или выбери опцию ниже:"

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = telebot.types.KeyboardButton("☑️ 1.1 Скользкие поверхности")
    btn2 = telebot.types.KeyboardButton("☑️ 1.2 Перепад высот")
    btn3 = telebot.types.KeyboardButton("☑️ 1.3 Груз/инструмент")
    btn_finish = telebot.types.KeyboardButton("✅ Готово")

    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    markup.add(btn_finish)
    markup.add(telebot.types.KeyboardButton("◀️ Назад"))

    bot.send_message(chat_id, status_text, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "✅ Без дополнительных условий")
def no_conditions(message):
    chat_id = message.chat.id
    user_conditions[chat_id] = []

    response_text = "Вы выбрали профессию: Сторож (4732)\nБез дополнительных условий\n\nОтправляю личную карточку учета выдачи СИЗ..."

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton("◀️ Назад"))

    bot.send_message(chat_id, response_text, reply_markup=markup)

    # Отправляем обычную PDF файл
    try:
        pdf_file = open("Личная карточка учета выдачи СИЗ профессия сторож (4732).pdf", "rb")
        bot.send_document(chat_id, pdf_file)
        pdf_file.close()
    except Exception as e:
        bot.send_message(chat_id, f"Ошибка при отправке файла: {str(e)}")


@bot.message_handler(func=lambda message: message.text == "✅ Готово")
def finish_selection(message):
    chat_id = message.chat.id
    conditions = user_conditions.get(chat_id, [])

    conditions_text = ", ".join(conditions) if conditions else "без дополнительных условий"
    response_text = f"Вы выбрали профессию: Сторож (4732)\nДополнительные условия: {conditions_text}\n\nОтправляю карточку учета выдачи СИЗ..."

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton("◀️ Назад"))

    bot.send_message(chat_id, response_text, reply_markup=markup)

    # Отправляем PDF файл (обычный или измененный в зависимости от условий)
    try:
        if conditions:
            # Здесь должна быть логика для отправки измененной карточки
            pdf_filename = "Личная карточка учета выдачи СИЗ профессия сторож (4732) - измененная.pdf"
            # На данный момент отправляем обычную карточку, в будущем можно создать измененные версии
            pdf_filename = "Личная карточка учета выдачи СИЗ профессия сторож (4732).pdf"
        else:
            pdf_filename = "Личная карточка учета выдачи СИЗ профессия сторож (4732).pdf"

        pdf_file = open(pdf_filename, "rb")
        bot.send_document(chat_id, pdf_file)
        pdf_file.close()
    except Exception as e:
        bot.send_message(chat_id, f"Ошибка при отправке файла: {str(e)}")


@bot.message_handler(func=lambda message: message.text in [
    "Водитель автомобиля (783)",
    "Дворник (997)",
    "Электромонтажник по кабельным сетям (5271)",
    "Сварщик арматурных сеток и каркасов (4438)",
    "Повар (3593)",
    "Подсобный рабочий (3640)"
])
def select_profession(message):
    profession = message.text
    response_text = f"Вы выбрали профессию: {profession}\n\nФункция расчета СИЗ для этой профессии в разработке..."

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton("◀️ Назад"))

    bot.send_message(message.chat.id, response_text, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "📚 Терминология")
def terminology(message):
    bot.reply_to(message, "Функция терминологии в разработке...")


@bot.message_handler(func=lambda message: message.text == "⚖️ Законодательство")
def legislation(message):
    bot.reply_to(message, "Функция законодательства в разработке...")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Пожалуйста, используй кнопки меню для навигации или команду /start")


bot.infinity_polling()