# Advanced Usage of UnlockSpy

Here are some advanced tips for running **UnlockSpy** more stealthily and efficiently.

## 1. Convert to an Executable File

You can convert the `.pyw` script into an `.exe` file to make it even more lightweight and to hide the script execution window.

- Use **PyInstaller** or **cx_Freeze** to convert the `.pyw` script into a standalone executable:
  ```bash
  pyinstaller --onefile --noconsole unlockspy.pyw
```