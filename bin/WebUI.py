from flask import Flask, render_template, request
from GameEngine import GameEngine
from GameSettings import GameSettings

class WebUI:
  '''
  Provides user interface to game and starts game
  Site server
  '''

  def __init__(self):
    self.app = Flask(__name__)
    self._game_settings = GameSettings() # GameSettings link
    self._game = GameEngine()
    self.SetupRoutes()

  def SetupRoutes(self):

    @self.app.route('/')
    def Load():
      return render_template('index.html')

    @self.app.route('/query', methods=['POST'])
    def UserQueryListener(self):
      '''
      Listener for user send query
      '''
      self._game.UserQuery(request.json['text'])
    
    @self.app.route('/reset', methods=['GET'])
    def ResetListener(self):
      '''
      Reset button listener
      '''
      self._game.ResetState()
      return "Reset successful"

    @self.app.route('/settings_change', methods=['POST'])
    def SettingsChangeListener(self):
      '''
      Settings change listener
      '''
      data = request.json

      ### change _game_settings

      self._game.ChangeSettings(self._game_settings)
      
      return "Settings changed"

  def run(self):
    '''
    Start site
    '''
    self.app.run(debug=True)

if __name__ == '__main__':
  WebUI().run()