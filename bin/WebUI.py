'''Module containing WebUI class.'''

from copy import deepcopy
from flask import Flask, render_template, request, redirect, flash
from bin.game_engine import GameEngine


class WebUI:
    '''
    Provides user interface to game and starts game.
    Site server + creates game instance.
    '''

    def __init__(self):
        self.app = Flask(__name__, template_folder='../static')
        self.app.secret_key = 'your_secret_key_here'  # make it secret
        self._game = GameEngine()
        self._game_settings = deepcopy(self._game.state._game_settings)
        self.setup_routes()

    def setup_routes(self):
        '''Setup routes for game server.'''

        @self.app.route('/')
        def load():
            return render_template('index.html',
                                   message_history_length=self._game_settings.message_history_length,
                                   context_messages=self._game_settings.context_messages,
                                   assistant_instruction=self._game_settings.assistant_instruction)

        @self.app.route('/query', methods=['POST'])
        def user_query_listener():
            '''Listener to user query.'''
            self._game.user_query(request.form.get('user_query'))

            flash("Query resolved", "success")
            return redirect('/')

        @self.app.route('/reset', methods=['GET'])
        def reset_listener():
            '''Reset button listener.'''
            self._game.reset_state()

            flash("Reset", "success")
            return redirect('/')

        @self.app.route('/settings_change', methods=['POST'])
        def settings_change_listener():
            '''Settings change listener.'''
            data = request.form
            self._game_settings.assistant_instruction = data.get(
                'assistant_instruction')
            self._game_settings.context_messages = data.get('context_messages')
            self._game_settings.message_history_length = data.get(
                'message_history_length')

            self._game.settings_change(self._game_settings)

            flash("Settings changed", "success")
            return redirect('/')

    def run(self):
        '''Start site.'''
        self.app.run(debug=True)


if __name__ == '__main__':
    WebUI().run()
