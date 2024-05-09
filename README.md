# Interactive fiction

## How to run

get OPENAI_API_KEY as environment variable

```bash
run start.sh
```

## Description

User plays an interactive fiction game via web interface. Game content (text, images) and storyline mostly generating real-time by OpenAI generative neural networks accessed by api. Game screen, like in most interactive fiction games has a big text block where user (player) writes his answers relying on current situation, earns items to inventory, gets various effects and different bars. Also there is image under text block describing current location or situation. On side there are current bars with player's stats, inventory, and settings changer block.

User interface is pretty easy, player can reset game, play it by texting in the textbox, change settings in corresponding block (saved last messages, count of context messages, assistant instruction for chatGPT)

~~Project saves all visited locations and meeted persons to file, so it can accessed much later.~~ It was removed because of hard realization and not much affect on gameplay.

Also current game state (context, location image, settings, etc.) is always saved to file, which means user can close game anytime and proceed later.

## Gameplay

Since you probably have no OPENAI_API_KEY, you can see how game works by watching this video (clickable):

[![Watch the video](https://img.youtube.com/vi/WEEWDhriioY/maxresdefault.jpg)](https://youtu.be/WEEWDhriioY)
Page load long when new location is generated, because of waiting for API request to generate it.

Created by:
- Kozyrev Konstantin
