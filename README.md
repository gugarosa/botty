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
            - google
        - keys
        - utils
    - bot
        - handlers
            - entry
            - error
            - fallback
            - states
                - await_options
                - client
                - incidence
                - suggestion
        - tasks
            - google
            - mock
        - utils
            - constants
            - voice
    - storage
        - voices
```

### API

Essentialy, you can define what you want in the api module. Just follow the examples and you will have your custom tools in no more than 5 minutes.

```handlers```: Each handler is responsible for receiving a direct request for consuming the API. Will follow HTTP standards at every time.

```keys```: All external API's keys should be added here. We commonly use a .json format to ease our needs.

```utils```: An utilities package, if needed, to load external features. One example we can think of would be your machine learning toolkit.

### Bot

Essentialy, you can define what you want in the bot module. Just follow the examples and you will have your custom bot in no more than 5 minutes.

#### Handlers

This is why we are called Smart Bot. This will deal with all the inputs your users can perform from the Telegram application. Again, you can define whatever your desire. Please note that we are using python-telegram-bot to handle the service, so follow along them as well.

```entry```: An handler for any entry point.

```error```: This will handle any possible errors that surfaces.

```fallback```: If any fallback happens, this should be the place for it.

```states```: Handles any possible conversation states.

#### Tasks

Tasks are your bot actions. If you need to implement your own or gather external tools, here is the place to define them. You can define basically anything, just remember as we are dealing with external API calls, whatever comes in will be a JSON, whatever comes out will be a JSON.

```google```: A google module to hold any google-related tasks. As for now, we are only using Google's speech-to-text API.

```mock```: A mock module to hold any fake API tasks.

#### Utils

This is an utilities package. Common things shared across the application should be implemented here. It is better to implement once and use as you wish than re-implementing the same thing over and over again.

```constants```: Pre-defined constants used to help across the application.

```voice```: Pre-defined voice messages handling used to help across the application.

### Storage

We will generate data. Any data, lots of data, it is up to you. Use this module to save your files.

```voices```: A voices folder to storage voice saved files.

---

## Installation

We belive that everything have to be easy. Not difficult or daunting, Smart Bot will be the one-to-go package that you will need, from the very first instalattion to the daily-tasks implementing needs.

### Development

First of all, define the Python environment you are going to use (raw, conda, virtualenv) and enter it, for example:

```
conda activate <environment>
```

Next, install the needed requirements by performing the following commands:

```Python
pip install -r api/requirements.txt
pip install -r bot/requirements.txt
```

Before running any application, you need to enter in ```bot/``` folder and create a ```config.ini``` file by copying it from ```config.ini.example```.

```
[BOT]
TELEGRAM_KEY = <telegram's bot key>

[TASKS]
GOOGLE = http://localhost:8080/google/
MOCK = https://app.fakejson.com/q
```

As we are using Google Cloud Platform, we need to define an environment variable that points to its key:

```
export GOOGLE_APPLICATION_CREDENTIALS=<path to google's json key file>
```

Finally, you can start both API and Bot services:

```
python api/api.py
python bot/bot.py
```

### Production

To ease your needs in a production environment, we ship this package in a Docker container. Make sure that ```docker``` and ```docker-compose``` are installed and accessible from the command line.

Before running any application, you need to enter in ```bot/``` folder and create a ```config.ini``` file by copying it from ```config.ini.example```.

```
[BOT]
TELEGRAM_KEY = <telegram's bot key>

[TASKS]
GOOGLE = http://api:8080/google/
MOCK = https://app.fakejson.com/q
```

Remember that, as we are using Google Cloud Platform, you need to get your own Google's key file and add to ```api/key/google.json```.

Finally, you can build the container by using:

```
docker-compose build
```

After the build process is finished, you can run the container in detached mode:

```
docker-compose up -d
```

If you ever need to perform a maintance or update the repository, please put the container down:

```
docker-compose down
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

## Support

We know that we do our best, but it's inevitable to acknowlodge that we make mistakes. If you every need to report a bug, report a problem, talk to us, please do so! We will be avaliable at our bests at this repository or gth.rosa@uol.com.br.

---
