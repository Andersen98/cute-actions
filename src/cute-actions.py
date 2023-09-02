import dearpygui.dearpygui as dpg

def cute_callback(sender,app_data,userdata):
    print(f"sender is: {sender}")
    print(f"app_data is: {app_data}")
    print(f"user_data is: {user_data}")
dpg.create_context()

cute_commands = [
        "xrander --output DP-0 --rotate left",
        "xrander --output HDMI-0 --rotate left",
        ]

with dpg.window(label="Cute Actions"):
    dpg.add_listbox(items=cute_commands,
                    width=1200,
                    callback=cute_callback,
                    user_data="Cute User Data <3")

dpg.create_viewport(title='Cute Actions <3', width=1200,height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

