import config
import telebot
import pymongo
from telebot import types

bot = telebot.TeleBot(config.token)

client = pymongo.MongoClient("mongodb+srv://user:user@cluster0.cgvx87r.mongodb.net/test")



# Database Name
db = client["mongotest"]
# Collection Name
col = db["questions"]

qest = []

x = col.find({},{'_id':0})

for data in range(6):
    obj = x.next()
    result = (obj["question"])
    qest.append(result) 
#-----------------------------------------------------
get_data = []

def global_dictionary(data):
    get_data.append(data)
    return get_data
def global_clear():
    get_data.clear()
#-----------------------------------------------------

@bot.message_handler(commands= ['start', 'restart'])
def category(message):
    keyboard_kategory = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_butt = types.KeyboardButton('Почати тестування')
    keyboard_kategory.add(start_butt)

    bot.send_message(message.chat.id, "Доброго дня, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот створений для тестування якості послуг навчального процесу.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=keyboard_kategory)

@bot.message_handler(content_types= ['text'])
def subcategory(message):
    if message.text in ['Почати тестування', 'Назад']:
        keyboard_subcategory = types.ReplyKeyboardMarkup(resize_keyboard=True)
        year_1 = types.KeyboardButton('1 курс')
        year_2 = types.KeyboardButton('2 курс')
        year_3 = types.KeyboardButton('3 курс')
        year_4 = types.KeyboardButton('4 курс')
        year_5 = types.KeyboardButton('5 курс')
        keyboard_subcategory.add(year_1, year_2, year_3, year_4, year_5)

        bot.send_message(message.chat.id, 'Оберіть курс на якому ви навчались.', reply_markup = keyboard_subcategory)

    elif message.text == "1 курс":
            keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
            key_3_1 = types.KeyboardButton('КН-11')
            key_3_2 = types.KeyboardButton('ПМ-11')
            key_3_3 = types.KeyboardButton('ІПЗ-11')
            keyboard_tovar.add(key_3_1, key_3_2, key_3_3)
                        
            msg = bot.send_message(message.chat.id, 'Виберыть групу в якій ви навчаєтесь.',
                reply_markup=keyboard_tovar)
            bot.register_next_step_handler(msg, kyrs)
    
    elif message.text == "2 курс":
            keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
            key_3_1 = types.KeyboardButton('КН-21')
            key_3_2 = types.KeyboardButton('ПМ-21')
            key_3_3 = types.KeyboardButton('ІПЗ-21')
            keyboard_tovar.add(key_3_1, key_3_2, key_3_3)
                        
            msg = bot.send_message(message.chat.id, 'Виберыть групу в якій ви навчаєтесь.',
                reply_markup=keyboard_tovar)
            bot.register_next_step_handler(msg, kyrs)
    
    elif message.text == "3 курс":
            keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
            key_3_1 = types.KeyboardButton('КН-31')
            key_3_2 = types.KeyboardButton('ПМ-31')
            key_3_3 = types.KeyboardButton('ІПЗ-31')
            keyboard_tovar.add(key_3_1, key_3_2, key_3_3)
                        
            msg = bot.send_message(message.chat.id, 'Виберыть групу в якій ви навчаєтесь.',
                reply_markup=keyboard_tovar)
            bot.register_next_step_handler(msg, kyrs)
    
    elif message.text == "4 курс":
            keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
            key_3_1 = types.KeyboardButton('КН-41')
            key_3_2 = types.KeyboardButton('ПМ-41')
            key_3_3 = types.KeyboardButton('ІПЗ-41')
            keyboard_tovar.add(key_3_1, key_3_2, key_3_3)
                        
            msg = bot.send_message(message.chat.id, 'Виберыть групу в якій ви навчаєтесь.',
                reply_markup=keyboard_tovar)
            bot.register_next_step_handler(msg, kyrs)
    
    elif message.text == "5 курс":
            keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
            key_3_1 = types.KeyboardButton('КН-51')
            key_3_2 = types.KeyboardButton('ПМ-51')
            keyboard_tovar.add(key_3_1, key_3_2)
                        
            msg = bot.send_message(message.chat.id, 'Виберыть групу в якій ви навчаєтесь.',
                reply_markup=keyboard_tovar)
            bot.register_next_step_handler(msg, kyrs)

@bot.message_handler(content_types=['text'])
def kyrs(message):    
    if message.text == "КН-11":
        keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Кушнір В.П')
        key_3_2 = types.KeyboardButton('Жуковська Н.А')
        key_3_3 = types.KeyboardButton('Ліхо О.А')
        key_3_4 = types.KeyboardButton('Тадеєв П.О')
        key_3_5 = types.KeyboardButton('Остапчук О.П')
        key_3_6 = types.KeyboardButton('Харів Н.О')
        keyboard_tovar.add(key_3_1, key_3_2, key_3_3, key_3_4, key_3_5, key_3_6)
                    
        msg = bot.send_message(message.chat.id, 'Виберіть викладача',
            reply_markup=keyboard_tovar)
        bot.register_next_step_handler(msg, teacher)

    elif message.text == "КН-21":
        keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Шпак С.Г')
        key_3_2 = types.KeyboardButton('Жуковський В.В')
        key_3_3 = types.KeyboardButton('Прищепа О.В')
        key_3_4 = types.KeyboardButton('Бачишина Л.Д')
        key_3_5 = types.KeyboardButton('Ярощак С.В')
        key_3_6 = types.KeyboardButton('Гаврилюк В.І')
        keyboard_tovar.add(key_3_1, key_3_2, key_3_3, key_3_4, key_3_5, key_3_6)
                    
        msg = bot.send_message(message.chat.id, 'Виберіть викладача',
            reply_markup=keyboard_tovar)
        bot.register_next_step_handler(msg, teacher)
    
    elif message.text == "КН-31":
        keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Бачишина Л.Д')
        key_3_2 = types.KeyboardButton('Герус В.А')
        key_3_3 = types.KeyboardButton('Бялик І.М')
        key_3_4 = types.KeyboardButton('Демчук О.С')
        key_3_5 = types.KeyboardButton('Жуковська Н.А')
        key_3_6 = types.KeyboardButton('Міщук Г.Ю')
        keyboard_tovar.add(key_3_1, key_3_2, key_3_3, key_3_4, key_3_5, key_3_6)
                    
        msg = bot.send_message(message.chat.id, 'Виберіть викладача',
            reply_markup=keyboard_tovar)
        bot.register_next_step_handler(msg, teacher)

    elif message.text == "КН-41":
        keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Турбал Ю.В')
        key_3_2 = types.KeyboardButton('Жуковський В.В')
        key_3_3 = types.KeyboardButton('Мічута О.Р')
        key_3_4 = types.KeyboardButton('Харів Н.О')
        keyboard_tovar.add(key_3_1, key_3_2, key_3_3, key_3_4)
                    
        msg = bot.send_message(message.chat.id, 'Виберіть викладача',
            reply_markup=keyboard_tovar)
        bot.register_next_step_handler(msg, teacher)
    
    # change !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    elif message.text == "КН-51":
        keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Турбал Ю.В')
        key_3_2 = types.KeyboardButton('Жуковський В.В')
        key_3_3 = types.KeyboardButton('Мічута О.Р')
        key_3_4 = types.KeyboardButton('Харів Н.О')
        keyboard_tovar.add(key_3_1, key_3_2, key_3_3, key_3_4)
                    
        msg = bot.send_message(message.chat.id, 'Виберіть викладача',
            reply_markup=keyboard_tovar)
        bot.register_next_step_handler(msg, teacher)

    elif message.text == "ПМ-11":
        keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Мічута О.Р')
        key_3_2 = types.KeyboardButton('Тадеєв П.О')
        key_3_3 = types.KeyboardButton('Кушнір О.П')
        key_3_4 = types.KeyboardButton('Остапчук О.П')
        key_3_5 = types.KeyboardButton('Ліхо О.А')
        keyboard_tovar.add(key_3_1, key_3_2, key_3_3, key_3_4, key_3_5)
                    
        msg = bot.send_message(message.chat.id, 'Виберіть викладача',
            reply_markup=keyboard_tovar)
        bot.register_next_step_handler(msg, teacher)

    elif message.text == "ПМ-21":
        keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Грицюк І.М')
        key_3_2 = types.KeyboardButton('Жуковська Н.А')
        key_3_3 = types.KeyboardButton('Гладун Л.В')
        key_3_4 = types.KeyboardButton('Ярощак С.В')
        key_3_5 = types.KeyboardButton('Гаврилюк В.І')
        keyboard_tovar.add(key_3_1, key_3_2, key_3_3, key_3_4, key_3_5)
                    
        msg = bot.send_message(message.chat.id, 'Виберіть викладача',
            reply_markup=keyboard_tovar)
        bot.register_next_step_handler(msg, teacher)
    
    elif message.text == "ПМ-31":
        keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Бачишина Л.Д')
        key_3_2 = types.KeyboardButton('Остапчук О.П')
        key_3_3 = types.KeyboardButton('Прищепа О.В')
        key_3_4 = types.KeyboardButton('Мічута О.Р')
        key_3_5 = types.KeyboardButton('Жуковська Н.А')
        keyboard_tovar.add(key_3_1, key_3_2, key_3_3, key_3_4, key_3_5)
                    
        msg = bot.send_message(message.chat.id, 'Виберіть викладача',
            reply_markup=keyboard_tovar)
        bot.register_next_step_handler(msg, teacher)

    elif message.text == "ПМ-41":
        keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Мічута О.Р')
        key_3_2 = types.KeyboardButton('Гладун Л.В')
        key_3_3 = types.KeyboardButton('Харів Н.О')
        key_3_4 = types.KeyboardButton('Гаврилюк В.І')
        keyboard_tovar.add(key_3_1, key_3_2, key_3_3, key_3_4)
                    
        msg = bot.send_message(message.chat.id, 'Виберіть викладача',
            reply_markup=keyboard_tovar)
        bot.register_next_step_handler(msg, teacher)
    
    # Change !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    elif message.text == "ПМ-51":
        keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Мічута О.Р')
        key_3_2 = types.KeyboardButton('Гладун Л.В')
        key_3_3 = types.KeyboardButton('Харів Н.О')
        key_3_4 = types.KeyboardButton('Гаврилюк В.І')
        keyboard_tovar.add(key_3_1, key_3_2, key_3_3, key_3_4)
                    
        msg = bot.send_message(message.chat.id, 'Виберіть викладача',
            reply_markup=keyboard_tovar)
        bot.register_next_step_handler(msg, teacher)

    elif message.text == "ІПЗ-11":
        keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Кушнір В.П')
        key_3_2 = types.KeyboardButton('Жуковська Н.А')
        key_3_3 = types.KeyboardButton('Тадеєв П.О')
        key_3_4 = types.KeyboardButton('Остапчук О.П')
        key_3_5 = types.KeyboardButton('Ліхо О.А')
        keyboard_tovar.add(key_3_1, key_3_2, key_3_3, key_3_4, key_3_5)
                    
        msg = bot.send_message(message.chat.id, 'Виберіть викладача',
            reply_markup=keyboard_tovar)
        bot.register_next_step_handler(msg, teacher)

    elif message.text == "ІПЗ-21":
        keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Жуковський В.В')
        key_3_2 = types.KeyboardButton('Прищепа О.В')
        key_3_3 = types.KeyboardButton('Шпак С.Г')
        key_3_4 = types.KeyboardButton('Гаврилюк В.І')
        key_3_5 = types.KeyboardButton('Ярощак С.В')
        keyboard_tovar.add(key_3_1, key_3_2, key_3_3, key_3_4, key_3_5)
                    
        msg = bot.send_message(message.chat.id, 'Виберіть викладача',
            reply_markup=keyboard_tovar)
        bot.register_next_step_handler(msg, teacher)

    elif message.text == "ІПЗ-31":
        keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Бялик І.М')
        key_3_2 = types.KeyboardButton('Демчук О.С')
        key_3_3 = types.KeyboardButton('Зубик Я.Я')
        key_3_4 = types.KeyboardButton('Міщук Г.Ю')
        key_3_5 = types.KeyboardButton('Ярощак С.В')
        keyboard_tovar.add(key_3_1, key_3_2, key_3_3, key_3_4, key_3_5)
                    
        msg = bot.send_message(message.chat.id, 'Виберіть викладача',
            reply_markup=keyboard_tovar)
        bot.register_next_step_handler(msg, teacher)

    elif message.text == "ІПЗ-41":
        keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_3_1 = types.KeyboardButton('Мічута О.Р')
        key_3_2 = types.KeyboardButton('Реут Д.Т')
        key_3_3 = types.KeyboardButton('Міщук Г.Ю')
        key_3_4 = types.KeyboardButton('Рощенюк А.М')
        keyboard_tovar.add(key_3_1, key_3_2, key_3_3, key_3_4)
                    
        msg = bot.send_message(message.chat.id, 'Виберіть викладача',
            reply_markup=keyboard_tovar)
        bot.register_next_step_handler(msg, teacher)
#------------------------------------------------------------------------------------------
    # client = pymongo.MongoClient("mongodb://localhost:27017/")

    # # Database Name
    # db = client["mongotest"]

    # # Collection Name
    # col = db["questions"]

    # qest = []

    # x = col.find({},{'_id':0})

    # for data in range(6):
    #     obj = x.next()
    #     result = (obj["question"])
    #     qest.append(result) 

    # print(qest[0])
    # print(qest[1])
    # print(qest[2])
    # print(qest[3])
    # print(qest[4])
    # print(qest[5])

#------------------------------------------------------------------------------------------
@bot.message_handler(content_types=['text'])
def teacher(message):
    if message.text in ['Кушнір В.П', 'Жуковська Н.А', 'Ліхо О.А', 'Тадеєв П.О','Остапчук О.П','Харів Н.О','Шпак С.Г', 'Жуковський В.В'
    ,'Прищепа О.В','Бачишина Л.Д','Ярощак С.В', 'Гаврилюк В.І','Герус В.А','Бялик І.М','Демчук О.С','Міщук Г.Ю', 'Турбал Ю.В','Мічута О.Р'
    ,'Харів Н.О','Кушнір О.П','Остапчук О.П', 'Грицюк І.М','Гладун Л.В','Тадеєв П.О','Зубик Я.Я','Реут Д.Т','Рощенюк А.М']:
        keyboard_tovar = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_4_1 = types.KeyboardButton('Запитання 1')
        key_4_2 = types.KeyboardButton('Запитання 2')
        key_4_3 = types.KeyboardButton('Запитання 3')
        key_4_4 = types.KeyboardButton('Запитання 4')
        key_4_5 = types.KeyboardButton('Запитання 5')
        key_4_6 = types.KeyboardButton('Запитання 6')
        key_4_7 = types.KeyboardButton('Назад')
        keyboard_tovar.add(key_4_1, key_4_2, key_4_3, key_4_4, key_4_5, key_4_6, key_4_7)
        # bot.send_photo(message.chat.id, 'https://telegra.ph/file/9bc0b953212b85c8819be.jpg')
        msg = bot.send_message(message.chat.id, 'Оберіть запитання ',
            reply_markup=keyboard_tovar)
        bot.register_next_step_handler(msg, quee)      
        
        global_dictionary(message.text)
    
@bot.message_handler(content_types=['text'])
def quee(message):
    if message.text == "Запитання 1":
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("1", callback_data='1')
        item2 = types.InlineKeyboardButton("2", callback_data='2')
        item3 = types.InlineKeyboardButton("3", callback_data='3')
        item4 = types.InlineKeyboardButton("4", callback_data='4')
        item5 = types.InlineKeyboardButton("5", callback_data='5')

        keyboard_tovar.add(item1, item2, item3, item4, item5)            
        msg = bot.send_message(message.chat.id, qest[0],
            reply_markup=keyboard_tovar)

    bot.register_next_step_handler(msg, quee2)

def quee2(message):    
    if message.text == "Запитання 2":
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("1", callback_data='1')
        item2 = types.InlineKeyboardButton("2", callback_data='2')
        item3 = types.InlineKeyboardButton("3", callback_data='3')
        item4 = types.InlineKeyboardButton("4", callback_data='4')
        item5 = types.InlineKeyboardButton("5", callback_data='5')
        keyboard_tovar.add(item1, item2, item3, item4, item5)            
        msg = bot.send_message(message.chat.id, qest[1],
            reply_markup=keyboard_tovar)
        
    bot.register_next_step_handler(msg, quee3)

def quee3(message):    
    if message.text == "Запитання 3":
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("1", callback_data='1')
        item2 = types.InlineKeyboardButton("2", callback_data='2')
        item3 = types.InlineKeyboardButton("3", callback_data='3')
        item4 = types.InlineKeyboardButton("4", callback_data='4')
        item5 = types.InlineKeyboardButton("5", callback_data='5')

        keyboard_tovar.add(item1, item2, item3, item4, item5)            
        msg = bot.send_message(message.chat.id, qest[2],
            reply_markup=keyboard_tovar)

    bot.register_next_step_handler(msg, quee4)        

def quee4(message): 
    if message.text == "Запитання 4":
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("1", callback_data='1')
        item2 = types.InlineKeyboardButton("2", callback_data='2')
        item3 = types.InlineKeyboardButton("3", callback_data='3')
        item4 = types.InlineKeyboardButton("4", callback_data='4')
        item5 = types.InlineKeyboardButton("5", callback_data='5')
        keyboard_tovar.add(item1, item2, item3, item4, item5)            
        msg = bot.send_message(message.chat.id, qest[3],
            reply_markup=keyboard_tovar)

    bot.register_next_step_handler(msg, quee5)

def quee5(message): 
    if message.text == "Запитання 5":
        keyboard_tovar = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("1", callback_data='1')
        item2 = types.InlineKeyboardButton("2", callback_data='2')
        item3 = types.InlineKeyboardButton("3", callback_data='3')
        item4 = types.InlineKeyboardButton("4", callback_data='4')
        item5 = types.InlineKeyboardButton("5", callback_data='5')

        keyboard_tovar.add(item1, item2, item3, item4, item5)            
        msg = bot.send_message(message.chat.id, qest[4],
            reply_markup=keyboard_tovar)
    
    bot.register_next_step_handler(msg, quee6)    
    
def quee6(message):  
    if message.text == "Запитання 6":           
        bot.send_message(message.chat.id, qest[5])
        print(get_data)

        # Database Name
        db = client["mongotest"]

        # Collection Name
        col = db["answers"]

        result ={ 
        'teacher_name': get_data[0],
        'question1': int(get_data[1]),
        'question2': int(get_data[2]),
        'question3': int(get_data[3]),
        'question4': int(get_data[4]),
        'question5': int(get_data[5])
    }

        x = col.insert_one(result)

        global_clear()

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == '1':
                bot.send_message(call.message.chat.id, 'Ви вибрали оцінку 1')
            elif call.data == '2':
                bot.send_message(call.message.chat.id, 'Ви вибрали оцінку 2')
            if call.data == '3':
                bot.send_message(call.message.chat.id, 'Ви вибрали оцінку 3')
            elif call.data == '4':
                bot.send_message(call.message.chat.id, 'Ви вибрали оцінку 4')
            if call.data == '5':
                bot.send_message(call.message.chat.id, 'Ви вибрали оцінку 5')
                
            #remove inline buttons  
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Запитання",
                reply_markup=None)
            global_dictionary(call.data)
            # global_dictionary(call.data)
            
    except Exception as e:
        print(repr(e))

bot.polling()
    
