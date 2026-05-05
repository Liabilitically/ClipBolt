#⚡ ClipBolt
The simplest, most private way to sync your clipboard between Windows and iPhone. Takes less than 5 min to setup.

ClipBolt creates a private "data tunnel" between your devices. No clouds, no big-tech tracking, and no latency. If you can copy and paste, you can use ClipBolt.

**🛠 Step 1: Set up the "Tunnel" (Tailscale)**
Before the devices can talk, they need to be on the same private network.

On your PC: Download Tailscale for Windows and log in. [https://tailscale.com/download]

On your iPhone: Download Tailscale from the App Store and log in with the same account.

The Name: Open the Tailscale app on your PC. You will see a name for your computer (e.g., desktop-ra79nh or laptop). Write this down.

**💻 Step 2: Set up your PC**
Download: Go to the Releases page on this GitHub and download ClipBolt.exe. [https://github.com/Liabilitically/ClipBolt/releases]

Folder: Create a new folder on your Desktop called ClipBolt and move the ClipBolt.exe into it.

Run: Double-click ClipBolt.exe.

Note: Windows might say "Protected your PC." Click More Info and then Run Anyway.

Configure: A file called config.txt will automatically appear in your folder.

Open it with Notepad.

You will see API_KEY=Secret123. You can leave this as-is or change it to your own custom password.

Restart: Close the black window and run ClipBolt.exe again to save your settings.

**📱 Step 3: Set up your iPhone**
Get the Shortcut: Click these two links on your iPhone to install the ClipBolt Shortcuts:

- Shortcut to copy text from your PC onto your phone: [https://www.icloud.com/shortcuts/5a6deaa85c6540209ed4d52ca4ba239f]
- Shortcut to copy text from your phone onto you PC: [https://www.icloud.com/shortcuts/50e22a377f4643159267ed41a14dccda]

Configure: When you install it, you have to do two simple things:

1) PC Name: Enter the Tailscale name you wrote down in Step 1 in the URL field where it says '[Your-Tailscale-Name]'.
2) Secret Token: Open the Headers dropdown in the Shortcut and enter the API_KEY from your config.txt (default is Secret123).

Permissions: The first time you run it, tap "Always Allow" so it can talk to your PC.

#🚀 How to Use It
PC to Phone: Just copy anything on your PC. Tap the ClipBolt icon on your iPhone home screen (or use the Widget). The text is now on your iPhone clipboard!

Phone to PC: Tap the "Send to PC" Shortcut. The text is instantly pasted into your computer's clipboard.

#❓ Troubleshooting
It’s not working! Make sure Tailscale is turned ON (showing a green light) on both your PC and your iPhone.

Firewall: If it still fails, Windows Firewall might be blocking it. Allow main.exe through your Firewall settings.

Background Running: To keep it running forever, move main.exe to your Windows Startup folder (Win + R, type shell:startup, and paste a shortcut to the exe there).

#🔒 Privacy & Security
No Servers: Your data never goes to a ClipBolt server. It travels directly from PC to Phone via WireGuard encryption.

Open Source: You can read every line of code in main.py to see exactly how your data is handled.
