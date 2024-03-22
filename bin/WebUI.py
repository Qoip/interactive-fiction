from flask import Flask, render_template, request, redirect, flash, session
from GameEngine import GameEngine
from GameSettings import GameSettings

class WebUI:
  '''
  Provides user interface to game and starts game
  Site server
  '''

  def __init__(self):
    self.app = Flask(__name__, template_folder='../static')
    self.app.secret_key = 'your_secret_key_here' # make it secret
    self._game_settings = GameSettings()
    self._game = GameEngine()
    self.SetupRoutes()

  def SetupRoutes(self):

    @self.app.route('/')
    def Load():
      return render_template('index.html',
                           message_history_length=self._game_settings.message_history_length,
                           context_messages=self._game_settings.context_messages,
                           assistant_instruction=self._game_settings.assistant_instruction)

    @self.app.route('/query', methods=['POST'])
    def UserQueryListener():
      '''
      Listener for user send query
      '''
      self._game.UserQuery(request.form.get('user_query'))

      flash("Query resolved", "success")
      return redirect('/')
    
    @self.app.route('/reset', methods=['GET'])
    def ResetListener():
      '''
      Reset button listener
      '''
      self._game.ResetState()

      flash("Reset", "success")
      return redirect('/')

    @self.app.route('/settings_change', methods=['POST'])
    def SettingsChangeListener():
      '''
      Settings change listener
      '''
      data = request.form
      self._game_settings.assistant_instruction = data.get('assistant_instruction')
      self._game_settings.context_messages = data.get('context_messages')
      self._game_settings.message_history_length = data.get('message_history_length')

      self._game.ChangeSettings(self._game_settings)
      
      flash("Settings chenged", "success")
      return redirect('/')

  def run(self):
    '''
    Start site
    '''
    self.app.run(debug=True)

if __name__ == '__main__':
  WebUI().run()