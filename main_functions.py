import cgi
import html
import json

def files_init(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8'):
            pass
    except FileNotFoundError:
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump({}, f)

class SignUserData:
    
    USERS = 'tmp/users.json'

    def __init__(self, form):
        self.form = form
        self.login =  html.escape(form.getfirst('login',''))
        self.password = html.escape(form.getfirst('password',''))
        self.remember_me = self.form.getvalue('remember_me')
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