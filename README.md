# Smart Bot: A Python-Inspired Telegram Bot

## Welcome to Smart Bot.

An easy-to-use solution to your botting needs. Firstly, implemented along the Telegram API, you can define your handlers and tasks. Lastly, you can also use your API. We offer both solutions and all the essential tools that you need in order to construct a bot. Please, follow along the next sections in order to learn more about this excellent tool.

Smart Bot is compatible with: **Python 3.6**.

---

## Package guidelines

1. The very first information you need is in the very **next** section.
2. **Installing** is also easy if you wish to read the code and bump yourself into, follow along.
3. Note that there might be some **additional** steps in order to use our solutions.
4. If there is a problem, please do not **hesitate**, call us.

---

## Getting started: 60 seconds with Smart Bot

First of all. Code is all commented. Yes, they are commented. Just browse to any file, chose your subpackage, and follow it. We have high-level code for most tasks we could think of.

Alternatively, if you wish to learn even more, please take a minute:

Smart Bot is based on the following structure, and you should pay attention to its tree:

```
- smart_bot
    - api
        - handlers
            - google
            - spacy
        - keys
        - utils
    - bot
        - handlers
            - common
            - entry
            - error
            - fallback
            - states
                - await_options
                - client
                - incidence
                - suggestion
        - tasks
            - aws
            - google
            - mock
            - spacy
            - weather
        - utils
            - constants
            - transcript
            - voice
    - storage
        - transcripts
        - voices
```

### API

Necessarily, you can define what you want in the api module. Just follow the examples, and you will have your custom tools in no more than 5 minutes.

```handlers```: Each handler is responsible for receiving a direct request for consuming the API. Will follow HTTP standards at every time.

```keys```: All external API's keys should be added here. We commonly use a .json format to ease our needs.

```utils```: An utility package, if needed, to load external features. One example we can think of would be your machine learning toolkit.

### Bot

Essentially, you can define what you want in the bot module. Just follow the examples, and you will have your custom bot in no more than 5 minutes.

#### Handlers

This is why we are called Smart Bot. This will deal with all the inputs your users can perform from the Telegram application. Again, you can define whatever you desire. Please note that we are using python-telegram-bot to handle the service, so follow along with them as well.

```common```: A handler for standard uses.

```entry```: A handler for any entry point.

```error```: This will handle any possible errors that surface.

```fallback```: If any fallback happens, this should be the place for it.

```states```: Handles any possible conversation states.

#### Tasks

Tasks are your bot actions. If you need to implement your own or gather external tools, here is the place to define them. You can define anything, remember as we are dealing with external API calls, whatever comes in will be a JSON, whatever comes out will be a JSON.

```aws```: An amazon web services module to hold any aws-related tasks. As for now, we are only using AWS' S3 storage.

```google```: A google module to hold any Google-related tasks. As for now, we are only using Google's speech-to-text API.

```mock```: A mock module to hold any fake API tasks.

```spacy```: A Spacy module to hold any spacy-related tasks. As for now, we are only using Spacy's named entity recognition.

```weather```: A weather module to hold any Weather API tasks.

#### Utils

This is a utility package. Common things shared across the application should be implemented here. It is better to implement once and use as you wish than re-implementing the same thing over and over again.

```constants```: Pre-defined constants used to help across the application.

```transcript```: Pre-defined voice transcription handling used to help across the application.

```voice```: Pre-defined voice messages handling used to help across the application.

### Storage

We will generate data. Any data, lots of data, it is up to you. Use this module to save your files.

```transcripts```: A transcripts folder to store voices' transcriptions.

```voices```: A voices folder to store voice saved files.

---

## Installation

We believe that everything has to be easy. Not tricky or daunting, Smart Bot will be the one-to-go package that you will need, from the very first installation to the daily-tasks implementing needs.

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

[AWS]
ACCESS_KEY = <s3 bucket access key>
SECRET_KEY = <s3 bucket secret key>
BUCKET_URL = <s3 bucket url>

[TASKS]
GOOGLE = http://localhost:8080/google
MOCK = https://app.fakejson.com/q
SPACY = http://localhost:8080/spacy
WEATHER = https://api.worldweatheronline.com/premium/v1/weather.ashx?

[PORTAL]
LOGIN = https://smart-portal-dev.netpartners.com.br/auth/login
API = https://smart-portal-dev.netpartners.com.br/api
```

As we are using the Google Cloud Platform, we need to define an environment variable that points to its key:

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

[AWS]
ACCESS_KEY = <s3 bucket access key>
SECRET_KEY = <s3 bucket secret key>
BUCKET_URL = <s3 bucket url>

[TASKS]
GOOGLE = http://api:8080/google
MOCK = https://app.fakejson.com/q
SPACY = http://api:8080/spacy
WEATHER = https://api.worldweatheronline.com/premium/v1/weather.ashx?

[PORTAL]
LOGIN = https://smart-portal-dev.netpartners.com.br/auth/login
API = https://smart-portal-dev.netpartners.com.br/api
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

If you ever need to perform maintenance or update the repository, please put the container down:

```
docker-compose down
```

---

## Environment configuration

Note that sometimes, there is a need for additional implementation. If needed, from here you will be the one to know all of its details.

### Ubuntu

No specific additional commands needed.

### Windows

No specific additional commands needed.

### MacOS

No specific additional commands needed.

---

## Support

We know that we do our best, but it is inevitable to acknowledge that we make mistakes. If you ever need to report a bug, report a problem, talk to us, please do so! We will be available at our bests at this repository or gth.rosa@uol.com.br.

---
