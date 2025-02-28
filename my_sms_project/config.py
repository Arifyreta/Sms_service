import toml
#Загружаем данные из файла конфигурации
def load_config():
    with open('config_1.toml','r') as f:
        return toml.load(f)

