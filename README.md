# Lab Manager
The official source code for the Lab Manager Discord Bot.


## Config
You should set your `Discord Token`, `MongoDB` connection URL and any applicable channel ID's in the `main.py` file. There are also other optional configurations in almost all other files. In the case that you want to use the statuspage.io integration, make sure to set your `API token`, `page id` & `metric id` in the `cogs/api.py` file.

## Setup
```shell
git clone https://github.com/labdiscord/manager
cd manager
pip3 install -r requirements.txt
python3 main.py
```

Note: A mongoDB instance is **required** to run this bot.

## Instant Deployment
Alternatively, just click this button to develop in [Repl.it](https://repl.it), a top quality in-browser IDE! [![Run on Repl.it](https://repl.it/badge/github/labdiscord/bot)](https://repl.it/github/labdiscord/bot)

## Changelog

### V2.0
- Added Statuspage.io API Posting
- Ticket system now works in a new server.
- Removed Moderation Commands (Migrated to [helper](http://dbots.cc/toast))
- Removed Reaction Roles (Migrated to [Helper](http://dbots.cc/helper))
- Removed Certification Commands (Migrated To Discord Bot Labs - Private Bot)

## Features
This bot has the following set of features.
- Info commands to set predefined msgs.
- Ticket system to apply for certification w/automated questions (Works in seperate server.).
- Automatic updates to bot status & avatar that happen every few minutes.
- Automated posting to statuspage.io API.


## Contributing
Contributions are always welcome!
Take a look at any existing issues on this repository for starting places to help contribute towards, or simply create your own new contribution to the project.

When you are ready, simply create a pull request for your contribution and we will review it whenever we can!


### Donating

You can also help me and the project out by sponsoring me through a [donation on PayPal](http://paypal.me/discordlabs).


## Discussion, Support and Issues

Need support with this project, have found an issue or want to chat with others about contributing to the project?
> Please check the project's issues page first for support & bugs!

Not found what you need here?

* If you have an issue, please create a GitHub issue here to report it, include as much detail as you can.
* _Alternatively,_ You can join our Discord server to discuss any issue or to get support for the project.:

<a href="http://discordlabs.org/discord" target="_blank">
    <img src="https://discordapp.com/api/guilds/608711879858192479/embed.png" alt="Discord" height="30">
</a>
