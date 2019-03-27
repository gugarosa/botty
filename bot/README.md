# Smart Bot: A Telegram Python-Inspired Bot

## Welcome to Smart Bot.

An easy-to-use solution to your botting needs. Firstly, implemented along the Telegram API, you can define your own handlers and tasks. Lastly, you can also use your own API. We offer both solutions and all the basic tools that you need in order to construct a bot. Please, follow along the next sections in order to learn more about this awesome tool.

Smart Bot is compatible with: **Python 3.6**.

---

## Package guidelines

1. The very first information you need is in the very **next** section.
2. **Installing** is also easy, if you wish to read the code and bump yourself into, just follow along.
3. Note that there might be some **additional** steps in order to use our solutions.
4. If there is a problem, please do not **hesitate**, call us.

---

## Getting started: 60 seconds with Smart Bot

First of all. Code is all commented. Yes, they are commented. Just browse to any file, chose your subpackage and follow it. We have high-level code for most tasks we could think of.

Or if you wish to learn even more, please take a minute:

Smart Bot is based on the following structure, and you should pay attention to its tree:

```
- smart_bot
    - api
        - handlers
        - utils
    - data
    - handlers
        - error
        - text
        - voice
    - tasks
        - spacy
    - utils
        - lang
        - locale
```

### API

Essentialy, you can define what you want in the api module. Just follow the examples and you will have your custom tools in no more than 5 minutes.

```handlers```: Each handler is responsible for receiving a direct request for consuming the API. Will follow HTTP standards at every time.

```utils```: An utilities package, if needed, to load external features. One example we can think of would be your machine learning toolkit.

### Data

We will generate data. Any data, lots of data, it is up to you. Use this module to save your files.

```voice```: A voice folder to storage voice saved files.

### Handlers

This is why we are called Smart Bot. This will deal with all the inputs your users can perform from the Telegram application. Again, you can define whatever your desire. Please note that we are using python-telegram-bot to handle the service, so follow along them as well.

```error```: This will handle any possible errors that surfaces.

```text```: Any incoming message text will be handled by this module.

```voice```: Any incoming message voice will be handled by this module.

### Tasks

Tasks are your bot actions. If you need to implement your own or gather external tools, here is the place to define them. You can define basically anything, just remember as we are dealing with external API calls, whatever comes in will be a JSON, whatever comes out will be a JSON.

```spacy```: A spacy module to hold any spacy-related tasks. This will be one of our external machine learning toolkits.

### Utils

This is an utilities package. Common things shared across the application should be implemented here. It is better to implement once and use as you wish than re-implementing the same thing over and over again.

```lang```: A folder holding several language translation files encoded in json format.

```locale```: Package to build your own localization system. You can define your own methods if additional procedures are required.

---

## Installation

We belive that everything have to be easy. Not difficult or daunting, Smart Bot will be the one-to-go package that you will need, from the very first instalattion to the daily-tasks implementing needs. If you may, just run the following under your most preferende Python environment (raw, conda, virtualenv, whatever)!:

```Python
pip install -r requirements.txt
```

---

## Environment configuration

Note that sometimes, there is a need for an additional implementation. If needed, from here you will be the one to know all of its details.

### Ubuntu

No specific additional commands needed.

### Windows

No specific additional commands needed.

### MacOS

No specific additional commands needed.

---

## Running

There are two basics steps in order to start this application.

First, please proceed to ```api/``` and start its service:

```Python
python api.py
```

Finally, go back to the main folder and start the bot service. Do not forget to create your own ```custom.ini``` file with the appropriate values:

```Python
python bot.py
```



---

## Support

We know that we do our best, but it's inevitable to acknowlodge that we make mistakes. If you every need to report a bug, report a problem, talk to us, please do so! We will be avaliable at our bests at this repository or gth.rosa@uol.com.br.

---
