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
        "excellent": [
            "http://4.bp.blogspot.com/-w2dZIP16sew/TpE1L7g8IbI/AAAAAAAAAKA/kshUsHepP00/s1600/free-MrBurnsExcellent.gif",
            "http://www.scancrit.com/wp-content/uploads/2011/11/excellent-4689_preview.png",
            "http://static.rcgroups.net/forums/attachments/1/6/9/8/4/9/a2213358-88-mister-burns-excellent.jpg"
        ]
    }

    def callback_message(self, conn, mess):
        body = mess.getBody().lower()
        for meme in self.memes:
            if body.find(meme) != -1 and randint(1, 10) <= len(self.memes[meme]):
                self.send(
                    mess.getFrom(),
                    choice(self.memes[meme]),
                    message_type='groupchat'
                )
