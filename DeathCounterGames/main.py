import flet as ft
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
    death_text = ft.Text(f"Deaths: {deaths}", size=30, weight=ft.FontWeight.BOLD)

    # Event Functions
    def add_death(e=None):
        nonlocal deaths
        deaths += 1
        death_text.value = f"Deaths: {deaths}"
        page.update()

    def reset_deaths(e):
        nonlocal deaths
        deaths = 0
        death_text.value = f"Deaths: {deaths}"
        page.update()

    # Global Hotkey Listener (Works over Steam games)
    def on_press(key):
        if getattr(key, "char", None) == "+":
            page.run_thread(add_death)

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    # Add Controls to Page & Connect on_click
    page.add(
        ft.TextField(label="Game Name", hint_text="enter game name"),
        death_text,
        ft.Row([
            ft.Button("+1", on_click=add_death),
            ft.Button("Reset", on_click=reset_deaths),
        ])
    )

ft.run(main)