# Games Death Counter (GDC)

A lightweight, LiveSplit-style desktop death counter overlay built with Python and Flet for tracking deaths while playing Steam and PC games.

## Features

* **Always-on-Top Dark Overlay:** Floats cleanly above borderless windowed games without getting in the way.
* **Global Hotkeys:** Track deaths in the background even while your game is focused (supports both top-row and Numpad keys).
* **Custom Hotkey Settings:** Rebind your add and subtract keys anytime via **Settings**—ideal for laptops without a numpad.
* **Save & Load Runs:** Save individual game playthroughs to `.json` files and reload them later via **File > Save Game / Open Game**.
* **Responsive Resizing:** Dynamically scales text, buttons, and spacing as you drag the window down to a compact corner box.

## Download & Run (Windows)

1. Go to the **[Releases](https://github.com)** page.
2. Download **`DeathCounter.exe`** from the latest release.
3. Double-click **`DeathCounter.exe`** to launch—no Python installation required.

*(Note: For the overlay to stay visible over Steam games, set your game's display mode to **Borderless Windowed**.)*

## Default Controls

| Action | Default Hotkey | UI Control |
| :--- | :---: | :--- |
| **Add Death (+1)** | `+` | Click **`+1`** |
| **Subtract Death (-1)** | `-` | Click **`-1`** |
| **Reset Counter** | *(None — prevents accidental resets)* | Click **`Reset`** |
| **Change Hotkeys** | — | Top Menu > **`Settings`** |
| **Save / Open Run** | — | Top Menu > **`File`** |
