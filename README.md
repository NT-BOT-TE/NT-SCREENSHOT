## SCREENSHOT BOT

[![Screenshot bot logo](https://te.legra.ph/file/ce0319aa547a63876b28c.jpg)](http://t.me/NT_SCREENSHOT_BOT)

### Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/NT-BOT-TE/NT-SCREENSHOT)

### Public URL of streaming service
<a href="https://github.com/NT-BOT-TE/NT-FILES-TREAM"><img src="https://img.shields.io/badge/2ndlink%20Open%3F-!-green?&style=flat-square!&logo=GitHub" width=220px></a></p>
<a href="https://t.me/NT_BOT_CHANNEL"><img src="https://www.1tamilmv.pro/uploads/monthly_2018_01/torrborder.gif.a36a064cf6ccdffab1019892c8caca2d.gif" width=320px></a></p>

## Support
<a href="https://t.me/NT_BOT_CHANNEL"><img src="https://img.shields.io/badge/Channel%20Join%3F-yes-green?&style=flat-square!&logo=telegram" width=220px></a></p>
<a href="https://t.me/Ntbotgroup"><img src="https://img.shields.io/badge/Group%20Join%3F-yes-green?&style=flat-square!&logo=telegram" width=220px></a></p>
### Environment Variables

Properly setup the environment variables or populate `config.py` with the values (some of the values are sensitive data, so keep them safe).

* `API_ID`(required) - Get your telegram API_ID from [https://my.telegram.org/](https://my.telegram.org/).
* `API_HASH`(required) - Get your telegram API_HASH from [https://my.telegram.org/](https://my.telegram.org/).
* `BOT_TOKEN`(required) - Obtain your bot token from [Bot Father](https://t.me/BotFather "Bot Father").
* `SESSION_NAME`(required) - Name you want to call your bot's session, Eg: bot username.
* `LOG_CHANNEL`(required) - Log channel's id.
* `DATABASE_URL`(required) - Mongodb database URI.
* `AUTH_USERS`(required) - Authorised user(s) id separated by space.
* `HOST`(required) - Public URL of streaming service ([Source](https://github.com/NT-BOT-TE/NT-FILES-TREAM)).
* `MAX_PROCESSES_PER_USER`(optional) - Number of parallel processes each user can have, defaults to 2.
* `MAX_TRIM_DURATION`(optional) - Maximum allowed seconds for trimming. Defaults to 600.
* `TRACK_CHANNEL`(optional) - User activity tracking channel's id. Only needed if you want to track and block any user. Disabled by default.
* `SLOW_SPEED_DELAY`(optional) - Delay required between each request. Defaults to 15s.

### Commands

* `/start` - Command to start bot or check whether bot is alive.
* `/settings` - Command to configure bot's behavior'
* `/set_watermark` - Command to add custom watermark text to screenshots. Usage: `/set_watermark watermark_text`.

* `/status` - Admin/Auth users only command. Returns number of total users.
* `/ban_user` - Admin/Auth users only command. Command to ban any user. Usage: `/ban_user user_id ban_duration ban_reason`. `user_id` - telegram id of the user, `ban_duration` - ban duration in days, `ban_reason` - reason for ban. All 3 parameters are required.
* `/unban_user` - Admin/Auth users only command. Command to ban any banned user. Usage: `/unban_user user_id`. `user_id` - telegram id of the user. The parameter is required.
* `/banned_users` - Admin/Auth users only command. Command to view all banned users. Usage: `/banned_users`. This takes no parameters.
* `/broadcast` - Admin/Auth user only command. Command to broadcast some message to all users. Usage: reply `/broadcast` to the message you want to broadcast.


### Settings
In bot settings.
* `Upload Mode` - Screenshot upload mode. Either `as image file` or `as document file`. Defaults to `as image file`.
* `Watermark` - Watermark text to be embedded to screenshots. Texts upto 30 characters supported. Disabled by default.
* `Watermark Color` - Font color to be used for watermark. Any of `white`, `black`, `red`, `blue`, `green`, `yellow`, `orange`, `purple`, `brown`, `gold`, `silver`, `pink`. Defaults to `white`.
* `Watermark Font Size` - Font size to be used for watermarks. Any of `small(30)`, `medium(40)`, `large(50)`. Defaults to `medium`.
* `Sample Video Duration` - Sample video's duration. Any of `30s`, `60s`, `90s`, `120s`, `150s`. Defaults to `30s`.
* `Screenshot Genetation Mode` - Either `random` or `equally spaced`. Defaults to `equally spaced`.

[![Screenshot bot logo](https://te.legra.ph/file/dba336d48033a57871bd4.mp4)](https://te.legra.ph/file/dba336d48033a57871bd4.mp4)

