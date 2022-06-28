#!/home/toshiba/fopi/bin/ python

# from locale import currency
import datetime
import sqlite3, pytz
from locale import currency
# from datetime
import telebot
from telebot import types #Подключили дополнения
from telegram_bot_pagination import InlineKeyboardPaginator
from telbot.apple import second_level_iphone, second_level_apple, second_level_uzhivani_iphone
from django.core.exceptions import ObjectDoesNotExist
import telbot.constant

import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fopi.settings')
django.setup()


from telbot.models import (
    Client, ClientReward, Order, 
    OrderProduct, CategoryDescription, 
    ProductToCategory, CategoryPath,
    Category, UrlAlias
)


# объявление переменных
btn1 = u"🤑 Мої бонуси"
btn2 = u"🗒 Історія замовлень"
btn3 = u"📱iPhone"
btn4 = u"💻 Apple"
btn5 = u"📱🤝Уживані iPhone"
btn6 = u"🛒 Каталог товарiв"
btn7 = u"👈 назад"



base_url = "https://fopi.ua/"
phone = ''
c = None

API = telbot.constant._token

bot = telebot.TeleBot(API)

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(message, res=False):
    mes = 'Вітаю 👋! Я розповім тобі, що вміє Fopi Bot. \n \nДля початку давай авторизуємось. Скоріше тицяй на кнопку 👇'
    
    global conn
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    
    #connect to Data Base SQLite
    conn = sqlite3.connect('db.sqlite3')
    bd = conn.cursor()
    #write var's in BD(table users)
    
    bd.execute('SELECT * FROM users WHERE chat_id={};'.format(message.chat.id))
    t = bd.fetchall()
    if len(t) == 1:
        user_markup.row(btn1,btn2)
        user_markup.row(btn6)
        # user_markup.row(btn3,btn4)
        # user_markup.row(btn5)
        bot.send_message(message.from_user.id, 'Круто😎 Ти авторизований Fopi френд. Обирай в меню, що тебе цікавить 👇', reply_markup=user_markup)
        bd.execute('SELECT * FROM users WHERE chat_id={};'.format(message.chat.id))
        for b in bd:
            if b[-1] == 0:
                bd.execute('UPDATE users SET status={} WHERE chat_id={}'.format(1, b[3]))
        bd.close()
        conn.commit()
        conn.close()
    else:
        # bot.send_message(message.chat.id, mes)
        phone_1(message, mes)

    


@bot.message_handler(commands=['number']) #Объявили ветку для работы по команде <strong>number</strong>
def phone_1(message, mes):
    keyboard = telebot.types.ReplyKeyboardMarkup(True, False)
    # keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) #Подключаем клавиатуру
    button_phone = types.KeyboardButton(text="👆Авторизація", request_contact=True) #Указываем название кнопки, которая появится у пользователя
    keyboard.row(button_phone) #Добавляем эту кнопку 
    keyboard.row(btn6) #Добавляем эту кнопку 
    bot.send_message(message.chat.id, mes, reply_markup=keyboard) #Дублируем сообщением о том, что пользователь сейчас отправит боту свой номер телефона (на всякий случай, но это не обязательно)

 

@bot.message_handler(content_types=['contact']) #Объявили ветку, в которой прописываем логику на тот случай, если пользователь решит прислать номер телефона :) 
def contact(message):
    if message.contact is not None: #Если присланный объект <strong>contact</strong> не равен нулю
        # print(message.contact) #Выводим у себя в панели контактные данные. А вообщем можно их, например, сохранить или сделать что-то еще.     
        # print(message.chat.id)
        date_now = datetime.datetime.strftime(datetime.datetime.now(tz=pytz.timezone('Europe/Kiev')), "%Y.%m.%d %H:%M:%S")
        global phone
        phone = str(message.contact.phone_number)[-10:]
        # print(message.contact.first_name, message.contact.last_name)

        #connect to Data Base SQLite
        conn = sqlite3.connect('db.sqlite3')
        bd = conn.cursor()
        #write var's in BD(table users)

        bd.execute('SELECT * FROM users WHERE chat_id={};'.format(message.chat.id))
        t = bd.fetchall()
        if len(t) == 0:
            bd.execute('INSERT INTO users (id, firstName, secondName, chat_id, date_added, phone, status) VALUES(NULL, "{}", "{}", {}, "{}", "{}", 1)'.format(message.contact.first_name, message.contact.last_name, message.chat.id, date_now, phone))
            conn.commit()
            print("Contact saved!")
        else:
            print("Conntact exist")
        print(phone)
        start(message)



def sec_level_apple_1(message):
    # user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup = telebot.types.InlineKeyboardMarkup()
    sc = second_level_apple()
    list_l = []
    for s in sc:
        # print(s.category_id, s.categor.first().name)
        list_l.append(s)
    
    for i in range(0, len(list_l), 2):
        # user_markup.row(list_l[i].description, list_l[i+1].description)
        b1 = types.InlineKeyboardButton(text=list_l[i].categor.first().name, callback_data=list_l[i].category_id) #, callback_data=list_uzh[i].category_id)
        b2 = types.InlineKeyboardButton(text=list_l[i+1].categor.first().name, callback_data=list_l[i+1].category_id) #, callback_data=list_uzh[i+1].category_id)
        user_markup.row(b1, b2)
    bot.send_message(message.from_user.id, message.text, reply_markup=user_markup)


def sec_level_iphone_1(message):
    user_markup = telebot.types.InlineKeyboardMarkup()
    sc = second_level_iphone()
    list_l = []
    for s in sc:
        list_l.append(s)
    for i in range(0, len(list_l), 2):
        b1 = types.InlineKeyboardButton(text=list_l[i].category.categor.first().name, callback_data=list_l[i].category_id) #, callback_data=list_uzh[i].category_id)
        b2 = types.InlineKeyboardButton(text=list_l[i+1].category.categor.first().name, callback_data=list_l[i+1].category_id) #, callback_data=list_uzh[i+1].category_id)
        user_markup.row(b1, b2)
    bot.send_message(message.from_user.id, 'Обери модель', reply_markup=user_markup)



def sec_level_uzhivani_1(message):
    user_markup = telebot.types.InlineKeyboardMarkup()
    list_uzh = second_level_uzhivani_iphone()
        
    for i in range(0, len(list_uzh), 2):
        try:
            cd = CategoryDescription.objects.get(category_id=list_uzh[i].category_id)
            cd_plus_1 = CategoryDescription.objects.get(category_id=list_uzh[i+1].category_id)
            b1 = types.InlineKeyboardButton(text=cd.name[8:], callback_data=list_uzh[i].category_id)
            b2 = types.InlineKeyboardButton(text=cd_plus_1.name[8:], callback_data=list_uzh[i+1].category_id)
            user_markup.row(b1, b2)
            # user_markup.row(cd.name[8:], cd_plus_1.name[8:])
        except ObjectDoesNotExist:
            pass
    bot.send_message(message.from_user.id, 'Обери модель', reply_markup=user_markup)




some_id = None



def some_func(call, page=1):
    global some_id, base_url
    list_menu = ["3587", "3671", "3679", "3735"]
    list_not_menu = ["3511", "3522"]
    # print("Some Function Call data = ", call.data, page)
    # print(call.message)
    if call.data.isdigit() and call.data not in list_menu:
        some_id = call.data
        string_all = ''
        ptc = ProductToCategory.objects.filter(category_id=call.data, product__status=1, product__price__gt=0).order_by("product__price")
        # print(ptc.count())
        if ptc.count()<=20:
            for p in ptc:
                # print(UrlAlias.objects.get(query__icontains=p.product.product_id).keyword)
                b_url = base_url + UrlAlias.objects.filter(query__icontains=p.product.product_id).first().keyword
                string_1 = "<a href='%s'>%s</a> - %s₴" %(b_url, p.product.prod_desc.name, round(p.product.price, 0))
                string_all = string_all + "\n" + string_1 + "\n"
        elif ptc.count()>20:
            count_number_page, obj_in_massages = just_func(ptc)
            count_number_page_start = (page-1) * obj_in_massages
            count_number_page_end = obj_in_massages*page -1    
            send_product_list_page(call.message, page, count_number_page, ptc[count_number_page_start:count_number_page_end])


        bot.send_message(call.message.chat.id, string_all, parse_mode='HTML', disable_web_page_preview=True)
        def_message = "Для замолвлення: \n\n 👨‍💻 На сайті - тицяй на обраний товар і замовляй; \n\n 🤙 За телефоном 0800330842 (Безкоштовні дзвінки); \n\n <a href='%s'>💬 В дірект.</a>" %('https://instagram.com/fopi.ua?igshid=YmMyMTA2M2Y=')
        bot.send_message(call.message.chat.id, def_message, parse_mode='HTML')
    
    # second Menu
    elif call.data.isdigit() and call.data in list_menu:
        # print("in second menu")
        some_id = call.data
        cp = CategoryPath.objects.filter(path_id=call.data, category__status=1).exclude(category_id=call.data)
        
        user_markup = telebot.types.InlineKeyboardMarkup()
        list_second_menu = []
        for c in cp:
            list_second_menu.append(c)

        # for even
        if len(list_second_menu)%2 == 0:
            for i in range(0, len(list_second_menu), 2):
                try:
                    cd = CategoryDescription.objects.get(category_id=list_second_menu[i].category_id)
                    cd_plus_1 = CategoryDescription.objects.get(category_id=list_second_menu[i+1].category_id)
                    b1 = types.InlineKeyboardButton(text=cd.name, callback_data=list_second_menu[i].category_id) #
                    b2 = types.InlineKeyboardButton(text=cd_plus_1.name, callback_data=list_second_menu[i+1].category_id) #
                    user_markup.row(b1, b2)
                except ObjectDoesNotExist:
                    pass
        # for uneven
        elif len(list_second_menu)%2 == 1:
            for i in range(0, len(list_second_menu), 2):

                # else:
                try:
                    if i+1 == len(list_second_menu):
                        cd = CategoryDescription.objects.get(category_id=list_second_menu[i].category_id)
                        b1 = types.InlineKeyboardButton(text=cd.name, callback_data=list_second_menu[i].category_id) #
                        user_markup.row(b1)
                    else:
                        cd = CategoryDescription.objects.get(category_id=list_second_menu[i].category_id)
                        cd_plus_1 = CategoryDescription.objects.get(category_id=list_second_menu[i+1].category_id)
                        b1 = types.InlineKeyboardButton(text=cd.name, callback_data=list_second_menu[i].category_id) #
                        b2 = types.InlineKeyboardButton(text=cd_plus_1.name, callback_data=list_second_menu[i+1].category_id) #
                        user_markup.row(b1, b2)
                except ObjectDoesNotExist:
                    pass

        bot.send_message(call.message.chat.id, 'Обери модель', reply_markup=user_markup)
    else:
        # print(some_id)
        ptc = ProductToCategory.objects.filter(category_id=some_id, product__status=1, product__price__gt=0).order_by("product__price")
        count_number_page, obj_in_massages = just_func(ptc)
        count_number_page_start = (page-1) * obj_in_massages
        count_number_page_end = obj_in_massages*page -1    
        send_product_list_page(call.message, page, count_number_page, ptc[count_number_page_start:count_number_page_end])


        # bot.send_message(call.message.chat.id, call.message.text)







@bot.callback_query_handler(func=lambda call:True)
def page_callback(call):
    if call.data.startswith("character"):
        order_page_callback(call)
    elif call.data.startswith("product"):
        product_page_callback(call)
    else:
        some_func(call)





def send_product_list_page(message, page=1, order_count=0, crw=None):
    global bot, base_url
    paginator = InlineKeyboardPaginator(
        order_count,
        current_page=page,
        data_pattern='product#{page}'
    )

    string_all= ''
    for crw1 in crw:
        b_url = base_url + UrlAlias.objects.filter(query__icontains=crw1.product.product_id).first().keyword
        string_1 = "<a href='%s'>%s</a> - %s₴" %(b_url, crw1.product.prod_desc.name, round(crw1.product.price, 0), )
        string_all = string_all + "\n" + string_1 + "\n"

    bot.send_message(
        message.chat.id,
        string_all,
        reply_markup=paginator.markup,
        parse_mode='HTML',
        disable_web_page_preview=True
    )


# @bot.callback_query_handler(func=lambda call: call.data.split('#')[0]=='product')
def product_page_callback(call):
    page = int(call.data.split('#')[1])
    bot.delete_message(
        call.message.chat.id,
        call.message.message_id
    )
    some_func(call, page)
    




@bot.message_handler(commands=['get_bonus'])
def get_bonus(message):
    #connect to Data Base SQLite
    conn = sqlite3.connect('db.sqlite3')
    bd = conn.cursor()
    #write var's in BD(table users)

    bd.execute('SELECT * FROM users WHERE chat_id={};'.format(message.chat.id))
    t = bd.fetchall()
    # phone='0500199890'
    phone=t[0][5]
    try:
        global c
        c = Client.objects.get(telephone__icontains=phone)
        crw_active = ClientReward.objects.filter(client_id=c, status=1)
        crw_wait = ClientReward.objects.filter(client_id=c, status=0)
        # print(crw_wait.count())
        sum_passive = 0
        sum_active = 0
        for cl in crw_active:
            sum_active = sum_active + cl.points

        bot.send_message(message.chat.id, "🥳 На твоєму рахунку: " + str(sum_active) +  " бонусних грн.")
        
        if crw_wait.count()>1:
            for cl_w in crw_wait:
                sum_passive = cl_w.points
                avaible_date = cl_w.date_added + datetime.timedelta(days=15)
                print(cl_w.date_added)
                bot.send_message(message.chat.id, "ще " + str(sum_passive) + " бонусних грн будуть нараховані - 🗓 " + avaible_date.strftime("%d-%m-%Y"))

        
        bot.send_message(message.chat.id, "Бонусами можна оплатити до 30% покупки 👏.")
    except Client.DoesNotExist:
        bot.send_message(message.chat.id, 'Упс🙊 ти не зареєстрований в бонусній програмі Fopi. Це легко виправити реєструйся за посиланням 👉 https://fopi.ua/create-account 👈 а потім повертайся до бота. \n \n⌛️ Я почекаю. \n \n❗️Реєструй той номер в якому в тебе є телеграм. Так нам буде простіше спілкуватись')



def just_func(crw):
    obj_in_massages = 10
    count_pages = int(crw.count()/10)
    a = count_pages * 10
    if a == crw.count():
        print(" == ")
    else:
        count_pages +=1

    return count_pages, obj_in_massages




@bot.message_handler(commands=['get_order'])
def get_order_list(message, page=1):
    # print(message)
    # contact(message)
    global phone
    print(phone)
    # phone='0500199890'
    string_all = ''
    try:
        c = Client.objects.filter(telephone__icontains=phone).first()
        crw = Order.objects.filter(client_id=c).exclude(order_status_id=0).order_by('-date_added')
        
        count_number_page, obj_in_massages = just_func(crw)
        count_number_page_start = (page-1) * obj_in_massages
        count_number_page_end = obj_in_massages*page -1        
        send_order_page(message, page, count_number_page, crw[count_number_page_start:count_number_page_end])

    except Client.DoesNotExist:
        bot.send_message(message.chat.id, 'Упс🙊 ти не зареєстрований в бонусній програмі Fopi. Це легко виправити реєструйся за посиланням 👉 https://fopi.ua/create-account 👈 а потім повертайся до бота. \n \n⌛️ Я почекаю. \n \n❗️Реєструй той номер в якому в тебе є телеграм. Так нам буде простіше спілкуватись')



def send_order_page(message, page=1, order_count=0, crw=None):
    global bot
    paginator = InlineKeyboardPaginator(
        order_count,
        current_page=page,
        data_pattern='character#{page}'
    )

    string_all= ''
    for crw1 in crw:
           
        
        if crw1.currency_id == 2:
            total = round(crw1.total*crw1.currency_value, 2)
            # url = 'https://api.telegram.org/bot'+API+'/sendMessage?chat_id='+ str(message.chat.id) + '&text='+str(crw1.order_id)
            # string_1 = "<a href='%s'>"%(url)  + str(crw1.order_id) + "</a>. Добавлен: " + crw1.date_added.strftime("%d.%m.%y") + "\n К-во.: " + str(crw1.orderproduct_set.count()) + ". Итого: $%s" %(total)
            string_1 = "🗓" + crw1.date_added.strftime("%d.%m.%y") +  "🧾№ " + "<a href='https://api.telegram.org/bot5576706434:AAHFT78UcKFHXW3F2XBjvg76TOZStIYzXCw/sendMessage?chat_id=355503529&text=Всем привет!'>" + str(crw1.order_id) + "</a> - сума - %s %s" %(total, crw1.currency_code)+ "\n"
        else:
            total = round(crw1.total*crw1.currency_value)
            # url = 'https://api.telegram.org/bot'+API+'/sendMessage?chat_id='+ str(message.chat.id) + '&text='+str(crw1.order_id)
            string_1 = "🗓" + crw1.date_added.strftime("%d.%m.%y") +  "🧾№ " + "<a href='https://api.telegram.org/bot5576706434:AAHFT78UcKFHXW3F2XBjvg76TOZStIYzXCw/sendMessage?chat_id=355503529&text=Всем привет!'>" + str(crw1.order_id) + "</a> - сума - %s %s" %(total, crw1.currency_code)+ "\n"

        # print(url)
        string_all = string_all + "\n" + string_1

    string_all = string_all + "\n\nДля того, щоб переглянути чек, введіть номер замовлення."

    bot.send_message(
        message.chat.id,
        string_all,
        reply_markup=paginator.markup,
        parse_mode='HTML'
    )



# @bot.callback_query_handler(func=lambda call: call.data.split('#')[0]=='character')
def order_page_callback(call):
    # print(call.data)
    page = int(call.data.split('#')[1])
    bot.delete_message(
        call.message.chat.id,
        call.message.message_id
    )
    get_order_list(call.message, page)



@bot.message_handler(commands=['stop'])
def stop(message):
    sent3 = bot.send_message(message.chat.id, 'bye')
    print(sent3)


def sec_level_catalog(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row(btn3,btn4)
    user_markup.row(btn5,btn7)
    bot.send_message(message.from_user.id, 'Зроби вибiр', reply_markup=user_markup)






# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    string_all = ''
    global btn1,btn2,btn3
    print(message.text)
    if message.text.isdigit():
        # print("digit")
        order_p = OrderProduct.objects.filter(order_id=message.text)
        order = Order.objects.get(order_id=message.text)
        print(order_p)
        if order_p.count()>1:
            for crw1 in order_p:
                price = str(round(crw1.price*crw1.order.currency_value, 2))
                total = str(round(crw1.total*crw1.order.currency_value, 2))
                string_1 = "🔘" + crw1.name + "\nкількість - " + str(crw1.quantity) + " шт. | 🏷" + price + " " + crw1.order.currency_code + "  |  " + total + " " + crw1.order.currency_code
                string_all = string_all + "\n\n" + string_1
        else:
            price = str(round(order_p.first().price*order.currency_value, 2))
            total = str(round(order_p.first().total*order.currency_value, 2))
            # string_1 = order_p.first().name + " | " + str(order_p.first().quantity) + " | " + price + " | " + total
            string_1 = "🔘" + order_p.first().name + "\nкількість - " + str(order_p.first().quantity) + " шт. | 🏷" + price + " " + order.currency_code + " | " + total + " " + order.currency_code
            string_all = string_1

        string_all = string_all + "\n\n🧾Усього: " + str(round(order.total*order.currency_value, 2)) + order.currency.code
        bot.send_message(message.chat.id, string_all)

    elif message.text == btn1:
        get_bonus(message)    
    
    elif message.text == btn2:
        get_order_list(message)
    
    elif message.text == btn3:
        sec_level_iphone_1(message)
    
    elif message.text == btn4:
        sec_level_apple_1(message)

    elif message.text == btn5:
        sec_level_uzhivani_1(message)    
    
    elif message.text == btn6:
        sec_level_catalog(message)

    elif message.text == btn7:
        start(message) 
    
    else:
        print("No digit")
    # print(message.text)
    # bot.send_message(message.chat.id, 'Вы написали: ' + message.text)





# Запускаем бота
bot.polling(none_stop=True, interval=0)



# if __name__ == '__main__':
#      bot.polling(none_stop=True)