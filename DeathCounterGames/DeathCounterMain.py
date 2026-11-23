import flet as ft
import json
from pynput import keyboard

def main(page: ft.Page):

    # Window Sizes & Behavior
    page.window.width = 350
    page.window.height = 250
    page.window.always_on_top = True
    page.theme_mode = ft.ThemeMode.DARK
    page.title = "Death Counter"

    # State & UI Variables
    deaths = 0
    add_key = "+"
    sub_key = "-"
    death_text = ft.Text(f"Deaths: {deaths}", size=30, weight=ft.FontWeight.BOLD)
    game_input = ft.TextField(label="Game Name", hint_text="Enter Game Name")

    # Event Functions
    
    # Add Deaths Function to add to the death counter and update the UI
    def add_death(e=None):
        nonlocal deaths
        deaths += 1
        death_text.value = f"Deaths: {deaths}"
        page.update()

    # Subtract Deaths Function to subtract from the death counter and update the UI
    def subtract_death(e=None):
        nonlocal deaths
        if deaths > 0:
            deaths -= 1
        death_text.value = f"Deaths: {deaths}"
        page.update()

    # Reset Deaths Function to reset the death counter and update the UI
    def reset_deaths(e):
        nonlocal deaths
        deaths = 0
        death_text.value = f"Deaths: {deaths}"
        page.update()

    # Save Deaths Function to save the death counter to a JSON file
    async def save_game(e):
        # Opens Windows "Save As" dialog to save the death counter to a JSON file
        file_path = await ft.FilePicker().save_file(
            dialog_title="Save Death Counter",
            file_name="death_counter.json",
            allowed_extensions=["json"],
        )
        # Write data to the JSON file
        if file_path:
            if not file_path.endswith(".json"):
                file_path += ".json"
            data = {
                "game_name": game_input.value,
                "deaths": deaths
            }
            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)

    # Open Deaths Function to open a JSON file and load the death counter
    async def open_game(e):
        nonlocal deaths
        files = await ft.FilePicker().pick_files(
            dialog_title="Open Death Counter",
            allowed_extensions=["json"],
            allow_multiple=False,
        )
        if files:
            try:
                with open(files[0].path, "r") as f:
                    data = json.load(f)
                game_input.value = data.get("game_name", "")
                deaths = data.get("deaths", 0)
                death_text.value = f"Deaths: {deaths}"
                page.update()
            except Exception as err:
                print(f"Could not open file: {err}")

    # Global Hotkey Listener (Works over Steam games)
    def on_press(key):
        pressed = getattr(key, 'char', None)

        # Support Numpad 0-9 on Windows (virtual key codes 96 to 105)
        if pressed is None and getattr(key, 'vk', None) is not None:
            if 96 <= key.vk <= 105:
                pressed = str(key.vk - 96)

        if pressed and pressed.lower() == add_key.lower():
            page.run_thread(add_death)
        elif pressed and pressed.lower() == sub_key.lower():
            page.run_thread(subtract_death)

    # Start the keyboard listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Stop the listener when the app is closed
    page.window.on_event = lambda e: listener.stop() if e.data == "close" else None

    # UI Settings 
    add_key_input = ft.TextField(label="Add Death Key", value=add_key, 
                                 max_length=1, width=150)
    sub_key_input = ft.TextField(label="Subtract Death Key", value=sub_key, 
                                max_length=1, width=150)

    # Save Settings Function to save the hotkey settings and update the UI
    def save_settings(e):
        nonlocal add_key, sub_key
        if add_key_input.value:
            add_key = add_key_input.value
        if sub_key_input.value:
            sub_key = sub_key_input.value
        page.pop_dialog()

    # Settings Dialog to change the hotkey settings
    settings_dialog = ft.AlertDialog(
        title=ft.Text("Settings"),
        content=ft.Column([add_key_input, sub_key_input]),
        actions=[ft.TextButton("Cancel", on_click=lambda e: page.pop_dialog()),
                 ft.TextButton("Save", on_click=save_settings)],
    )

    # Open Settings Function to open the settings dialog and update the UI
    def open_settings(e):
        add_key_input.value = add_key
        sub_key_input.value = sub_key
        page.show_dialog(settings_dialog)

    # Add Controls to Page & Connect on_click
    page.add(
        ft.Row(
            [
                ft.PopupMenuButton(
                    content=ft.Text("File"),
                    items=[
                        ft.PopupMenuItem(content="Save Game", on_click=save_game),
                        ft.PopupMenuItem(content="Open Game", on_click=open_game),
                    ]
                ),
                ft.TextButton("Settings", on_click=open_settings),
            ],
            alignment=ft.MainAxisAlignment.START,
        ),

        # Game Name Input, Death Counter Display, and Control Buttons
        game_input,
        death_text,
        ft.Row([
            ft.Button("+1", on_click=add_death),
            ft.Button("-1", on_click=subtract_death),
            ft.Button("Reset", on_click=reset_deaths),
        ])
    )

ft.run(main)