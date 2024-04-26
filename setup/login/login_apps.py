from app_factory import app_factory
import yaml
import uiautomator2 as u2

def login_apps(d, app_names):
    for app_name in app_names:
        app = app_factory(d, app_name)
        app.login()

if __name__ == "__main__":
    device = u2.connect("emulator-5554")
    login_yaml_file = "login_apps.yaml"
    with open(login_yaml_file, 'r') as file:
        data = yaml.safe_load(file)
    login_apps(device,app_names=data["apps"])