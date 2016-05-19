# Rasberry PI and Telegram Chat Bot
<br/>
<img src="https://raw.githubusercontent.com/sjmach/raspberrypi-telegram-bot/master/Raspberrypi-telegram-bot.png" alt="Rasberry Pi Telegram BOT" align="center" />

<br />

<div align="center"><strong>A bot that runs yours Jenkins job and gives you status of a current run</strong></div>
<div align="center">A bot which runs a Jenkins job via Chat and uses the Telegram API</div>

<br />


## Features

<dl>
  <dt>Know the status of your Jenkins build</dt>
  <dd>This helps to know whether your job is running or last job is successful instantaneously</dd>

  <dt>Run new jobs</dt>
  <dd>This helps in craeting new jobs for your configured project</dd>

</dl>


<sub><i>Keywords: jenkins, telegram, API, python, bot,</i></sub>

## Quick start

1. Clone this repo using `$ git clone git@github.com/sjmach/raspberrypi-telegram-chat-bot.git`.
2. Visit the link to configure Raspberry Pi and telegram : http://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/<br />
3. You will get a token in above step
4. Change the path of Jenkins and Build Name in the bot.py file
5. Run the bot using 
```shell
python bot.py <token>
```


## License

This project is licensed under the MIT license, Copyright (c) 2016 Sundeep Joseph Machado. For more information see `LICENSE.md`.
