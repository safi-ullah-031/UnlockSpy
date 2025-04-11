# Startup Shortcut Setup for UnlockSpy

If you'd prefer to run **UnlockSpy** automatically when your computer boots, you can set up a **Startup Shortcut**.

## Steps:

1. **Create a Batch File (`.bat`) (Optional):**
   - Open a text editor and create a new `.bat` file with the following content:
     ```bash
     pythonw "path\to\unlockspy.pyw"
     ```
   - Replace `path\to\unlockspy.pyw` with the actual path to the `unlockspy.pyw` file.
   - Save the file with the `.bat` extension (e.g., `start_unlockspy.bat`).

2. **Open the Startup Folder:**
   - Press `Win + R`, type `shell:startup`, and hit `Enter`.
   - This will open the **Startup folder**.

3. **Create a Shortcut:**
   - Right-click in the **Startup folder**, select **New > Shortcut**.
   - Browse to your `.bat` file (or directly to `unlockspy.pyw` if you don't want a `.bat`).
   - Follow the on-screen instructions to finish creating the shortcut.

4. **Set the Shortcut to Run Minimally:**
   - Right-click the shortcut and select **Properties**.
   - Under the **Shortcut** tab, change the **Run** dropdown to `Minimized`.
   - Click **OK**.

Now, every time the system boots up, **UnlockSpy** will run in the background silently.

---

If you want to run it only after unlocking the device, use Task Scheduler for more control.
