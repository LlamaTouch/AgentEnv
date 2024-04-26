import yaml
import uiautomator2 as u2
import time

def install_apps(d, install_yaml_file):
    with open(install_yaml_file, 'r') as file:
        data = yaml.safe_load(file)

    apps = data['apps'] 
    for app in apps:
        installed = False
        print(f"Installing {app['app_name']}")
        d.open_url(app['action_seq']['open_url'])
        time.sleep(10) 
        try:
            element = d.xpath(app['action_seq']['click_xpath'])
            if element.exists:
                element.click()
                installed = True
                print(f"Waiting for {app['app_name']} app to install...")
                time.sleep(40)  
                print(f"{app['app_name']} is installed.")
            else:
                uninstall_element = d.xpath('//*[@content-desc="Uninstall"]')
                if uninstall_element.exists:
                    print(f"{app['app_name']} is already installed.")
                    installed = True
                else:
                    print(f"Install button not found for {app['app_name']}.")

        except Exception as e:
            print(f"Error installing {app['app_name']}: {str(e)}")

        if not installed:
            raise Exception(f'Failed to install {app["app_name"]}.')   
        
if __name__ == "__main__":
    device = u2.connect("emulator-5554")
    install_yaml_file = "pre_install.yaml"
    install_apps(device,install_yaml_file)