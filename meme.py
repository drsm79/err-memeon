from errbot import BotPlugin
from random import choice, randint


class MemeOn(BotPlugin):

    memes = {
        "oh my": [
            "http://925rebellion.com/wp-content/uploads/2013/09/3q7rym.jpg",
            "http://media1.giphy.com/media/FoUHKTJhoQU6I/200_s.gif",
            "http://ruadouche.com/wp-content/uploads/2013/05/George-Takei-oh-my.jpg",
            "http://newnownext.mtvnimages.com/2013/11/george-takei-oh-my.png",
        ],
    }

    def callback_message(self, conn, mess):
        body = mess.getBody().lower()
        for meme in self.memes:
            if body.find(meme) != -1 and randint(1, 10) == 1:
                self.send(
                    mess.getFrom(),
                    choice(self.memes[meme]),
                    message_type='groupchat'
                )
