# Task Scheduler Setup for UnlockSpy

This guide will walk you through setting up **UnlockSpy** to run automatically when your system is unlocked using **Windows Task Scheduler**.

## Steps:

1. **Open Task Scheduler:**
   - Press `Win + R`, type `taskschd.msc`, and hit `Enter`.
   - The **Task Scheduler** window will open.

2. **Create a New Task:**
   - On the right panel, click **Create Task...**.
   - In the **General** tab, give the task a name like `UnlockSpy`.
   - Set the **Security Options** to `Run only when the user is logged on` and check the box for `Run with highest privileges`.

3. **Set Trigger for Unlock:**
   - Go to the **Triggers** tab and click **New...**.
   - In the **Begin the task** dropdown, select `On workstation unlock`.
   - Click **OK**.

4. **Set Action to Run Script:**
   - Go to the **Actions** tab and click **New...**.
   - In the **Action** dropdown, select `Start a program`.
   - In **Program/script**, browse to your `unlockspy.pyw` file (or `.bat` if you used a wrapper).
   - Click **OK**.

5. **Configure Conditions (Optional):**
   - In the **Conditions** tab, you can configure options like:
     - Only running if the system is idle.
     - Running only if the device is on AC power (for laptops).

6. **Finish:**
   - Click **OK** to save the task.
   - You should now see the task listed in **Task Scheduler**.

---

Now, whenever you unlock your system, **UnlockSpy** will run silently and send the WhatsApp notification.