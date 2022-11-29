# Desktop Assistant

My Virtual Desktop Assistant Written in Python. Reginald = BIG (Minis Forum mini PC), Regy = SILVER (Lenovo 10" laptop)

# Requirements for windows

Steps to run the Assistant on your pc (use python 3.9)

## Check for `PIP` installation

- PIP is a tool that is used to install python packages. PIP is automatically installed with Python 2.7. 9+ and Python 3.4+.
- Open the command prompt and enter the below command to check whether pip is installed.

```md  
pip --version
```

- If you are receiving an error, it means that you might be having `pip3` installed, so try this command.

```md
pip3 --version
```

```md
python --version
```

> If you are still facing issues, try installing pip from [here](https://github.com/pypa/pip#readme)
## Pyttsx3

<!-- Pyttsx3 -->

- pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3
- Open the command prompt/terminal and enter the below command to install `pyttsx3`

```md
pip install pyttsx3
```

> Visit the [Pyttsx3 documentation](https://pypi.org/project/pyttsx3/) to know more about this library.
## Speech Recognition

- SpeechRecognition is a library for performing speech recognition, with support for several engines and APIs, online and offline.
- Open the command prompt/terminal and enter the below command to install `SpeechRecognition`

```md
pip install pyaudio SpeechRecognition
```

> Visit the [Speech Recognition documentation](https://pypi.org/project/SpeechRecognition/) to know more about this library.
<!-- pygame -->

## Pygame <br>

- Pygame is a set of Python modules designed for writing video games. Pygame adds functionality on top of the excellent SDL library. This allows you to create fully featured games and multimedia programs in the python language.
- Open the command prompt/terminal and enter the below command to install `Pygame`

```md
pip install pygame
```

# Suitable IDE for running this program

- Desktop Assistant can be run in the following code editor IDEs.
  - [Pycharm](https://www.jetbrains.com/help/pycharm/installation-guide.html)
  - [Visual Studio Code](https://code.visualstudio.com/docs)
  - [Jupyter-lab](https://jupyterlab.readthedocs.io/en/latest/)
  - [Replit](https://docs.replit.com/)

# Commands to interact with program.

After successful installation of the aforementioned dependencies, you can use the following commands (speak out) to interact with Reginald, your `Desktop-Assistant`

```
Start with  : Hello
Random Ans  : How are you?
            : Google
            : Youtube
send email  : Open email
            : Nothing
            : Abort
            : Stop
End with    : Bye
```


Installing all the necessary python module using

```
pip install -r requirements.txt
```

# Dependency for Ubuntu

```
sudo apt-get update
```

```
sudo apt-get install espeak
```

```
pip install -r ubuntu_requirements.txt
```

Wow All done! Now give the command to REGY.

# Run

For windows user run

```
python Reginald.py
```

For ubuntu user run
# file

```
python ReginaldUbuntu.py
```


