# Japanese Quizz Generator
With this app, you create kanji and word banks that you can save. From those banks, you can generate quizzes that will be displayed on a webpage. All quizzes will be randomly generated with different multiple choices and questions in a different order.

# What you need:
- python 3.6
- pip3
- Tkinter
- bs4

# Instalation process
## Linux (Ubuntu 18)
```bash
sudo apt-get install python3.6
sudo apt install python3-pip
sudo apt-get install python3.6-tk
pip3 install bs4
```

## Windows (10)
1. Install python3.6 from official release (https://www.python.org/downloads/release/python-366/)
2. In a 'cmd' type the following commands:
```bash
#Upgrade just in case your pip, if another command is suggested to be run, run that one
pip install --upgrad pip
pip install bs4
```



# How to start the app:
## Linux (Ubuntu 18):
```bash
# Move to the app directory and run
python3.6 src/GUI.py
# A window should appear with some options
```

## Windows (10)
Navigate to directory where you downloaded the project and double click on GUI.py


# Manual
I am kind of lazy to write that part and the UI should be intuitive enough.

However, here some tips:

- Just like your school projects, save your bank regulary. We never know when the program can bug.

- Since the files are JSON, you should be able to modify them directly and even create some, just follow a temple after saving a random bank.

- Small detail: When a kanji has multiple meanings, for example, it is asked to divide them with a ';'. However, for some reason the American keyboard ';' is different from the Japanese keyboard '；', therefore the meanings would not be properly divided in the JSON file. This detail doesn't interfere with the application or the quizzes.

- This application, unfortunately, opens multiple tabs, therefore if you wish to close all of them at once, just close the main tab (the first one you will see).

- If by any reason the quizzPage.html gets its content erased, just copy the one from quizzPage.copy.html


# Bugs and problems:
If you ever found a bug or something that isn't properly working, please create an issue in Github. Be as precise as possible, vague issues are not helping, screenshots and your used files are welcome. Although I am not going to lie, I will probably not solve it, unless it is dramatic.

# License and stuff
Yes, feel free to take this project and modify it as you wish for different purposes. I know that the code is kind of 'spaghetti code' and not optimized, therefore I won't blame anyone who improves it. Just give a small mention about this project if you ever publish yours  :)


# Tkinter helpful documentation
https://medium.com/swlh/build-a-gui-on-python-using-tkinter-from-scratch-step-by-step-for-beginners-69466223bcdf
https://www.tutorialspoint.com/python/python_gui_programming.htm
https://tkdocs.com/tutorial/index.html