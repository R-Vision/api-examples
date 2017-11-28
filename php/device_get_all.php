<?php

require 'vendor/autoload.php';

$client = new GuzzleHttp\Client([
    'base_uri' => 'http://127.0.0.1', // Адрес сервера
    'cookies' => true
]);

# Авторизируемся
$client->post('/login', [
    'json' => [
        'username' => 'admin', // Логин существующего пользователя
        'password' => 'admin'  // Пароль
    ],
    'verify' => false // Отключаем проверку SSL-сертификата
]);

$res = $client->get('/api/v1/am/devices', [
    'query' => [
        'page' => 1, // Пагинация, номер страницы
        'start' => 0, // Пагинация, позиция элемента с которого начать поиск
        'limit' => 10 // Сколько всего выводить
    ],
    'verify' => false
]);

/*

// Следующая страница из десяти устройств
$page2 = $client->get('/api/v1/am/devices', [
    'query' => [
        'page' => 2,
        'start' => 10,
        'limit' => 10
    ],
    'verify' => false
]);

// Все устройства
$all = $client->get('/api/v1/am/devices', [
    'query' => [
        'page' => 1,
        'start' => 0,
        'limit' => 999999 // Итоговое количество может быть ограничено лицензией
    ],
    'verify' => false
]);

*/

echo $res->getBody();