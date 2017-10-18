def main():
    from machine import Pin
    from time import sleep
    import ujson as json

    from ubot import Bot
    import oak

    with open('bot_config.json') as f:
        config = json.load(f)

    def admin_only(func):
        def wrapper(bot, update, *args):
            user = update['message']['from']
            username = user['username'].lower().strip('@')

            if username not in config['whitelist']:
                chat_id = update['message']['chat']['id']
                text = ('`Username is not in the sudoers file. '
                        'This incident will be reported`')
                bot.send_message(chat_id, text, parse_mode='Markdown')
                return
            else:
                return func(bot, update, *args)
        return wrapper

    bot = Bot(config['token'])
    pin = Pin(oak.PINS[config['pin_number']], Pin.OUT)

    @bot.command('start')
    def start(bot, update):
        chat_id = update['message']['chat']['id']
        text = 'Hello! Type a slash to see the available commands.'
        bot.send_message(chat_id, text)

    @bot.command('unlock')
    @admin_only
    def unlock(bot, update):
        chat_id = update['message']['chat']['id']
        text = 'Unlocking door!'
        bot.send_message(chat_id, text)

        pin.on()
        sleep(2)
        pin.off()

    @bot.command('allow', pass_args=True)
    @admin_only
    def allow(bot, update, args):
        config['whitelist'].extend(username.lower().strip('@')
                                   for username in args)
        with open('bot_config.json', 'w') as f:
            f.write(json.dumps(config))

        chat_id = update['message']['chat']['id']
        text = 'Whitelist updated:\n'
        text += '\n'.join('@' + username for username in config['whitelist'])
        bot.send_message(chat_id, text)

    @bot.command('whitelist')
    @admin_only
    def whitelist(bot, update):
        chat_id = update['message']['chat']['id']
        text = '\n'.join('@' + username for username in config['whitelist'])
        bot.send_message(chat_id, text)

    bot.poll()
