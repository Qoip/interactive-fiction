'''Module containing ContentGenerator class.'''

from message import Message
from game_state import GameState
from openai import OpenAI


class ContentGenerator:
    '''Provides API for resolving game queries.'''

    def __init__(self, game_state: GameState):
        self.__game_state: GameState = game_state  # GameState link!
        self.client = OpenAI()  # env OPENAI_API_KEY

    def user_query(self, user_message: str) -> Message:
        '''Query to chatGPT from user.'''
        text = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.__game_state.game_settings.assistant_instruction},
                {"role": "user", "content": self.__get_body()},
                {"role": "user", "content": f"Next user message: {user_message}"}
            ]
        )
        return Message("assistant", text.choices[0].message.content)

    def system_query(self, system_message: str) -> Message:
        '''Query from system to category items clarify or storyline intervention.'''
        text = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": self.__game_state.game_settings.assistant_instruction},
                {"role": "user", "content": self.__get_body()},
                {"role": "system", "content": system_message}
            ]
        )
        return Message("assistant", text.choices[0].message.content)

    def __get_body(self) -> str:
        '''Return body of the message.'''
        return "- context messages:\n" + "\n".join([str(msg) for msg in self.__game_state.context_messages()]) + \
            "- system context:\n" + "\n".join([str(msg) for msg in self.__game_state.system_context]) + \
            "- bars:\n" + "\n".join([f"{key}: {value}" for key, value in self.__game_state.bars.items()])
