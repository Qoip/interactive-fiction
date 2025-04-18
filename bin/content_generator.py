'''Module containing ContentGenerator class.'''

from message import Message
from game_state import GameState
from data_storage import DataStorage
from openai import OpenAI


class ContentGenerator:
    '''Provides API for resolving game queries.'''

    def __init__(self, game_state: GameState, storage: DataStorage):
        self.__game_state: GameState = game_state  # GameState link!
        self.client = OpenAI()  # env OPENAI_API_KEY
        self.storage = storage

    def user_query(self, user_message: str) -> Message:
        '''Query to chatGPT from user.'''
        self.storage.message_log(Message("user", self.__get_body()))
        self.storage.message_log(Message("user", user_message))
        text = self.client.chat.completions.create(
            model="gpt-4-turbo-2024-04-09",
            messages=[
                {"role": "user", "content": self.__game_state.game_settings.assistant_instruction},
                {"role": "user", "content": self.__get_body()},
                {"role": "user", "content": f"Next user message: {user_message}"}
            ]
        )
        answer = Message("assistant", text.choices[0].message.content)
        self.storage.message_log(answer)
        return answer

    def image_generate(self, query: str) -> str:
        '''Generate image link.'''
        link = self.client.images.generate(
            model="dall-e-3",
            prompt=query,
            size="1024x1024",
            quality="standard",
            n=1
        ).data[0].url
        print("Image generated:", link)
        return link

    def __get_body(self) -> str:
        '''Return body of the message.'''
        body = "- context messages:\n" + "\n".join([str(msg) for msg in self.__game_state.context_messages()]) + \
            "\n- bars:\n" + "\n".join([f"{key}: {value}" for key, value in self.__game_state.bars.items()])
        if self.__game_state.system_context:
            body += "\n- system context:\n" + "\n".join([str(msg) for msg in self.__game_state.system_context])
        if not self.__game_state.image_link:
            body += "\nNo location currently, you should add location field to this responce."
        return body
