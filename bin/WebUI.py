'''Module containing WebUI class.'''

from copy import deepcopy
from flask import Flask, render_template, request, redirect, flash
from game_engine import GameEngine


class WebUI:
    '''
    Provides user interface to game and starts game.
    Site server + creates game instance.
    '''

    def __init__(self):
        self.app = Flask(__name__, template_folder='../static')
        self.app.secret_key = 'your_secret_key_here'  # make it secret
        self.__game = GameEngine()
        self.__game_settings = deepcopy(self.__game.state.game_settings)
        self.setup_routes()

    def setup_routes(self):
        '''Setup routes for game server.'''

        @self.app.route('/')
        def load():
            return render_template('index.html',
                                   history_length=self.__game_settings.history_length,
                                   context_messages=self.__game_settings.context_messages,
                                   assistant_instruction=self.__game_settings.assistant_instruction)

        @self.app.route('/query', methods=['POST'])
        def user_query_listener():
            '''Listener to user query.'''
            self.__game.user_query(request.form.get('user_query'))

            flash("Query resolved", "success")
            return redirect('/')

        @self.app.route('/reset', methods=['GET'])
        def reset_listener():
            '''Reset button listener.'''
            self.__game.reset_state()

            flash("Reset successful", "success")
            return redirect('/')

        @self.app.route('/settings_change', methods=['POST'])
        def settings_change_listener():
            '''Settings change listener.'''
            data = request.form
            self.__game_settings.assistant_instruction = data.get(
                'assistant_instruction')
            self.__game_settings.context_messages = data.get('context_messages')
            self.__game_settings.history_length = data.get('history_length')

            self.__game.state.game_settings = self.__game_settings

            flash("Settings changed", "success")
            return redirect('/')

    def run(self):
        '''Start site.'''
        self.app.run(debug=True)


if __name__ == '__main__':
    WebUI().run()
