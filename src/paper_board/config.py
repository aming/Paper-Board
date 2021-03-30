import os, configparser, io

config_dir = os.path.expanduser("~") + "/.config/paper-board"
config_file = config_dir + "/config.ini"
config = configparser.ConfigParser(allow_no_value=True)

def write_default():
    os.makedirs(config_dir, exist_ok=True)
    with open(config_file, "w") as file:
        config.add_section("weather")
        config['location'] = "Seattle"
        config['api_token'] = ""
        config.write(file)
    
if not os.path.isfile(config_file):
    write_default()

config.read(config_file)
