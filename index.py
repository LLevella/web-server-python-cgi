#!/python37-32/python
# -*- coding: utf-8 -*-
import random
import cgi
import http.cookies
import os


from main_functions import SignUserData
from main_functions import CookieHandler
from main_functions import PostHandler

from html_templates import signin_tmp
from html_templates import signin_err_tmp
from html_templates import signin_ok_tmp
from html_templates import print_function

def get_random():
    rnd_int_array = [i for i in range(1002, 1011) if not (i==1007) and not (i==1009)]
    rnd_int = random.randint(0,6)
    return rnd_int_array[rnd_int]

if __name__ == "__main__":

    name_user_key = "user_key"
    form = cgi.FieldStorage()
    user_key = form.getfirst(name_user_key, "")
    ph = PostHandler(name_user_key)

    ch = CookieHandler()
    cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
    hash_key_value = cookie.get("key")
    
    if hash_key_value is not None:
        hash_key_value = hash_key_value.value

    if user_key == "":
    # если post - запрос не сериализован и ключ пользователю не назначен
        action = form.getfirst("action", "")
        if action:
        # если post - запрос был отправлен
            ph.get_post_data(form)
            ph.save_post_data()
            ph.redirect_to_get_server()
        else:
        # если активности еще не было
            user_by_cookie = ch.find_cookie(hash_key_value)
            if user_by_cookie is None:
            #если куки не установлены или пользователь не найден - страница входа
                print_function(signin_tmp) 
            else:
            #куки стоят и такой пользователь есть - основная
                print_function(signin_ok_tmp, str(get_random()))
    else:
    # если уже post - запрос сериализован и выдан ключ пользователю
        if ph.find_post_data(user_key):
        # если ключ валидный
            action = ph.get_value("action", "")
            if action == "":
                user = ch.find_cookie(hash_key_value)
                if user is None:
                #если куки не установлены или пользователь не найден - страница входа
                    print_function(signin_tmp) 
                else:
                #куки стоят и такой пользователь есть - основная
                    print_function(signin_ok_tmp, str(get_random()))

            if action == "exit":
            #удаляем куки при выходе
                key = ch.delete_cookie(hash_key_value)
                print('Set-cookie: key={}'.format(key))
                print_function(signin_tmp)

            if action == "login":
            # логинимся 
                login = ph.get_value("login")
                password = ph.get_value("password")
                remember_me = ph.get_value("remember_me")
                sud = SignUserData(login, password, remember_me)
                if sud.is_login_ok():
                    if sud.is_remember_me_checked():
                        key = ch.set_cookie(sud.get_login(),sud.get_password)
                        print('Set-cookie: key={}'.format(key))
                    print_function(signin_ok_tmp, str(get_random()))
                else:
                    print_function(signin_err_tmp)
            ph.delete_post_data(user_key)
        else:
        # если ключ не найден
            print_function(signin_tmp)
