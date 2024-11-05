# CommandCapd
Visually interpret the active PowerShell/CMD window with OpenAI GPT


![image](https://github.com/user-attachments/assets/efd2dc4b-e573-4031-ba00-a646cf0b3534)




This is NOT a chat app. fF it's not in the window, then AI isn't aware. 

The point is to process only what is in the current scrolled state, like the last error message off your debugging.

Another good app would process the whole Powershell vertically, but I'm not interested in doing that for now. I don't want it to be so invasive.

# HOW TO CREATE A SYSTEM COMMAND IN WINDOWS

This is how I create "capd" command instead of typing "python capd.py" each time:

![image](https://github.com/user-attachments/assets/a7fce735-be25-4035-ba7e-1e6d050ad519)

https://www.yopa.page/blog/2024-09-14-transform-python-scripts-into-global-command-line-tools.html

(I already created the .bat file for you to download. You just need to add the folder to PATH.)

# API Key
Don't forget to add your own API Key in the python file, or it won't run.

You get one here:

https://platform.openai.com/settings/organization/api-keys
