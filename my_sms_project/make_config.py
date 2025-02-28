import toml
#Создаём файл конфигурации в формате TOML
data_dict = {
    "SMS_SERVICE": {
        "url": "http://localhost:4010",
        "username": "Slava",
        "password": "1234qwerty"
    }
}

with open('config_1.toml', 'w') as file:
    toml.dump(data_dict, file)