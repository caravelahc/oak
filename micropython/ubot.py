try:
    import requests
except ImportError:
    import urequests as requests

from time import sleep
import gc


class Bot:
    def __init__(self, token):
        self._token = token
        self._handlers = []

    def _request(self, method, parse_response=True, **kwargs):
        url = 'https://api.telegram.org/bot{}/{}?'.format(self._token, method)
        url += '&'.join('{}={}'.format(k, v) for k, v in kwargs.items())
        response = requests.get(url)
        gc.collect()
        if parse_response:
            response = response.json()
            if not response['ok']:
                raise IOError(response['description'])
            return response['result']

    def get_updates(self, **kwargs):
        return self._request('getUpdates', **kwargs)

    def send_message(self, chat_id, text, **kwargs):
        self._request('sendMessage', parse_response=False,
                      chat_id=chat_id, text=text, **kwargs)

    def poll(self, interval=1):
        try:
            last_id = 0
            while True:
                updates = self.get_updates(offset=last_id + 1)
                for u in updates:
                    self.handle_update(u)
                    last_id = max(last_id, u['update_id'])
                gc.collect()
                sleep(interval)
        except KeyboardInterrupt:
            pass

    def handle_update(self, update):
        for handler in self._handlers:
            handler(self, update)
            gc.collect()

    def callback(self, func):
        self._handlers.append(func)
        return func

    def command(self, cmd, pass_args=False):
        def wrapper(func):
            def callback(bot, update):
                try:
                    text = update['message']['text']
                except KeyError:
                    return
                if text.startswith('/') and len(text) > 1:
                    command, *args = text.split()
                    if command[1:].lower() == cmd:
                        if pass_args:
                            return func(bot, update, args)
                        else:
                            return func(bot, update)

            self._handlers.append(callback)
            return func
        return wrapper
