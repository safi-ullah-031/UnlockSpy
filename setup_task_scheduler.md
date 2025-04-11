# Setup: Windows Task Scheduler

Follow these steps to run UnlockSpy every time your PC is unlocked.

### 1. Open Task Scheduler
- Press `Win + S`, type **Task Scheduler**, and open it.

### 2. Create New Task
- Go to **Action > Create Task**

#### General Tab
- Name: `UnlockSpyStealth`
- ✔ Run with highest privileges
- ✔ Run whether user is logged in or not

#### Triggers Tab
- New trigger:
  - Begin the task: `On workstation unlock`
  - ✔ Any user

#### Actions Tab
- New action:
  - Program/script: `pythonw.exe`
  - Arguments: `"C:\Path\To\unlockspy.pyw"`
  - Start in: `C:\Path\To\ScriptFolder`

#### Conditions/Settings
- ❌ Disable "Start only if idle"
- ❌ Disable "Start only on AC power"
- ✔ Stop task if runs longer than 1 minute (optional)

Done! Now UnlockSpy runs invisibly on unlock.
