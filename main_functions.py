import cgi
import html
import json
import os
import sys
import urllib
import random

def files_init(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8'):
            pass
    except FileNotFoundError:
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump({}, f)

class SignUserData:
    
    USERS = 'tmp/users.json'

    def __init__(self, login, password, remember_me):
        self.login = login
        self.password = password
        self.remember_me = remember_me
        files_init(self.USERS)

    def is_remember_me_checked(self):
        return self.remember_me
    
    def is_login_ok(self):
        with open(self.USERS, 'r', encoding='utf-8') as f:
            users = json.load(f)
        if self.login in users and self.password == users[self.login]: 
            return True     
        return False
        
    def get_login(self):
        return self.login
    
    def get_password(self):
        return self.password


class CookieHandler:
    
    COOKIE = 'tmp/cookie.json'

    def __init__(self):
        files_init(self.COOKIE)

    def find_cookie(self, cookie):
        with open(self.COOKIE, 'r', encoding='utf-8') as f:
            cookies = json.load(f)
        return cookies.get(cookie)
    
    def set_cookie(self, login, password):
        with open(self.COOKIE, 'r', encoding='utf-8') as f:
            cookies = json.load(f)
        # Генерируем куку с помощью хеш-функции для пользователя
        scookie = str(login) + str(password)
        cookie = hash(scookie)
        cookies[cookie] = login
        with open(self.COOKIE, 'w', encoding='utf-8') as f:
            json.dump(cookies, f)
        return cookie
    
    def delete_cookie(self, cookie):
        with open(self.COOKIE, 'r', encoding='utf-8') as f:
            cookies = json.load(f)
        if cookies.get(cookie) is not None:
            cookies.pop(cookie)
        with open(self.COOKIE, 'w', encoding='utf-8') as f:
            json.dump(cookies, f)
        return 0

class PostHandler:

    GET_SERVER = 'http://localhost/index.py'
    POST = 'tmp/post.json'

    def __init__(self, name_user_key):
        self.name_user_key = name_user_key
        files_init(self.POST)
    
    def get_post_data(self, form): 
        self.post_data = {}
        str_post_hash = ""
        self.post_data['action'] =html.escape(form.getfirst("action", ""))
        self.post_data['login'] = html.escape(form.getfirst("login", ""))
        self.post_data['password'] = html.escape(form.getfirst("password", ""))
        self.post_data['remember_me'] = html.escape(form.getfirst("remember_me", ""))
        for post_arg in self.post_data: 
            str_post_hash += str(post_arg)
        str_post_hash += str(random.random())
        self.post_hash = hash(str_post_hash)
        # print(self.post_data)

    def create_straddres_for_redirect(self):
        post_key = {self.name_user_key: self.post_hash}
        return '?'.join((self.GET_SERVER, urllib.parse.urlencode(post_key)))

    def redirect_to_get_server(self):
        print ("Content-Type: text/html")
        print ("Location: {}".format(self.create_straddres_for_redirect()))
        print ("")
    
    def save_post_data(self):
        with open(self.POST, 'r', encoding='utf-8') as f:
            post_tmp = json.load(f)
        post_tmp[self.post_hash] = self.post_data
        # print(post_tmp)
        with open(self.POST, 'w', encoding='utf-8') as f:
            json.dump(post_tmp, f)
    
    def find_post_data(self, post_key):
        with open(self.POST, 'r', encoding='utf-8') as f:
            post_tmp = json.load(f)
            if post_tmp.get(post_key) is None: 
                return False
            post_data_tmp = post_tmp.get(post_key)
            if not post_data_tmp:
                return False
            self.post_data = post_data_tmp
        return True
    
    def get_value(self, name, default = ""):
        if self.post_data[name] is None:
            return default
        return self.post_data[name]
    
    def delete_post_data(self, post_key):
        with open(self.POST, 'r', encoding='utf-8') as f:
            post_tmp = json.load(f)
        if post_tmp.get(post_key) is not None:
            post_tmp.pop(post_key)
        with open(self.POST, 'w', encoding='utf-8') as f:
            json.dump(post_tmp, f)