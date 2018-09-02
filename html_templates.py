#!/python37-32/python
# -*- coding: utf-8 -*-

import cgi
# шаблон входа
signin_tmp = '''
    <!doctype html>
    <html lang="ru">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta name="description" content="Тестовое задание">
        <title>Страница входа | Тестовое задание </title>
        <link href="css/bootstrap.css" rel="stylesheet">
        <link href="css/style.css" rel="stylesheet">
    </head>
    <body class="text-center">
        <form class="form-signin" action="index.py" method="post">
            <h1 class="h3 mb-3 font-weight-normal">Войдите, пожалуйста</h1>
            <label for="inputLogin" class="sr-only">Логин</label>
            <input name="login" type="text" id="inputLogin" class="form-control" placeholder="Логин" required autofocus>
            <label for="inputPassword" class="sr-only">Пароль</label>
            <input name="password" type="password" id="inputPassword" class="form-control" placeholder="Пароль" required>
            <input type="hidden" name="action" value="login">
            <div class="checkbox mb-3">
                <label>
                    <input name="remember_me" type="checkbox" value="remember-me"> Запомнить меня
                </label>
            </div>
            <button class="btn btn-lg btn-primary btn-block" type="submit">Войти</button>
        </form>
        <script src='js/jquery-3.3.1.js'></script>
        <script src="js/bootstrap.js"></script>
    </body>
    </html>
    '''
# шаблон ошибки при входе
signin_err_tmp = '''
    <!doctype html>
    <html lang="ru">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta name="description" content="Тестовое задание">
        <title>Ошибка входа | Тестовое задание </title>
        <link href="css/bootstrap.css" rel="stylesheet">
        <link href="css/style.css" rel="stylesheet">
    </head>
    <body class="text-center">
        <div class="container">
            <div class="row">
                <div class="col-xs-12">
                    <h1 class="h3 mb-3 font-weight-normal">Неверный логин или пароль</h1>
                </div>
            </div>
            <div class="row">
                <div class="col-xs-5"></div>
                <div class="col-xs-2">
                    <form class="form-return" action="index.py" method="post">
                        <button class="btn btn-lg btn-primary btn-block" type="submit">Вернуться</button>
                    </form>
                </div>
                <div class="col-xs-5"></div>
            </div>
        </div>
        <script src='js/jquery-3.3.1.js'></script>
        <script src="js/bootstrap.js"></script>
    </body>
    </html>
    '''
# шаблон основной страницы 
signin_ok_tmp = '''
    <!doctype html>
    <html lang="ru">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta name="description" content="Тестовое задание">
        <title>Основная страница | Тестовое задание </title>
        <link href="css/bootstrap.css" rel="stylesheet">
        <link href="css/style.css" rel="stylesheet">
    </head>
    <body class="text-center">
        <div class="container">
            <div class="row">
                <div class="col-xs-12">
                    <h1 class="h3 mb-3 font-weight-normal">Основная страница</h1>
                </div>
            </div>
             <div class="row">
                <div class="col-xs-4"></div>
                <div class="col-xs-2">
                    <form class="form-exit" action="index.py" method="post">
                        <input type="hidden" name="action" value="exit">
                        <button class="btn btn-lg btn-primary btn-block" type="submit">Выйти</button>
                    </form>
                </div>
                <div class="col-xs-2">
                    <button id="btn-test" class="btn btn-lg btn-primary btn-block" type="submit">Тест</button> 
                </div>        
                <div class="col-xs-4"></div>
            </div>
            <div class="lines"></div>
            <div class="row" id="test">
                <div class="col-xs-3"></div>
                <div class="col-xs-6">
                    <div id="progress-test">
                        <div class="progress">
                            <div id="progress-bar-test" class="progress-bar progress-bar-striped" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="30">
                            </div>
                        </div>
                        <div id="progress-text" class="text-center font-weight-bold">
                            <p class="text-success"> Осталось <span id="seconds"></span> секунд</p>
                        </div>
                    </div>
                    <div id="rand-result">
                        <div class="alert alert-success" role="alert">
                            <h4 class="alert-heading">Результат теста линии:</h4>
                            <p> <span id="impuls"></span> импульсов </p>
                        </div>
                    </div>                 
                </div>
                <div class="col-xs-3"></div>
            </div>
        </div>
        <script src='js/jquery-3.3.1.js'></script>
        <script src='js/test.js'></script>
        <script src="js/bootstrap.js"></script>
    </body>
    </html>
    '''
# вывод в stdout, который сейчас перенаправлен
def print_function(str_tmp, change_str=""):
    print("Content-type: text/html\n")
    if not change_str:
        print(str_tmp)
    else:
        print(str_tmp.format(change_str))
