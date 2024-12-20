class SmartDevice:

    def __init__(self, model_number, brand, screen_size, app_list=None):
        if app_list is None:
            app_list = []
        self.model_number = model_number
        self.brand = brand
        self.screen_size = screen_size
        self.app_list = app_list

    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)

    def install_app(self, app_name="calculator"):
        print(f"Installing {app_name}...")
        if app_name not in self.app_list:
            self.app_list.append(app_name)
        else:
            print(f"{app_name} is already installed.")
        return self.app_list

    def delete_app(self, app_name):
        if app_name in self.app_list:
            self.app_list.remove(app_name)
            print(f"{app_name} has been deleted.")
        else:
            print(f"{app_name} is not installed on this device.")

device_a = SmartDevice(1233244, 'CLG', 5.7)
device_a.report()

device_a.install_app("Instagram")
print(device_a.app_list)

device_a.install_app("Facebook")
print(device_a.app_list)

device_a.install_app("Facebook")
print(device_a.app_list)

device_a.delete_app("Instagram")
print(device_a.app_list)

device_a.delete_app("Twitter")