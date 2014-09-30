from errbot import BotPlugin, botcmd
from random import choice, randint, getrandbits
import requests
from lxml import html


class MemeOn(BotPlugin):

    memes = {
        "cage": [
            "http://img.izismile.com/img/img4/20110718/1000/that_crazy_nicholas_cage_02.gif",
            "http://media2.giphy.com/media/642o0uCyKFMPe/200_s.gif",
            "http://i.imgur.com/wSSULuB.gif",
            "http://www.esquire.com/cm/esquire/images/iu/esq-cage-xlg.jpg",
            "http://38.media.tumblr.com/e699f86ad0d8c4c839a3ab8f4da0023a/tumblr_mf1vh2KyL81r4etbjo1_500.gif",
            "https://www.wow247.co.uk/wp-content/uploads/2014/06/Face-Off-gif-1.gif",
            "http://img.izismile.com/img/img4/20110718/1000/that_crazy_nicholas_cage_06.gif",
            "http://i.minus.com/iseKAgDLLLLsQ.gif",
            "http://38.media.tumblr.com/tumblr_m32pr52hIU1rrbb7uo1_250.gif",
            "http://media.tumblr.com/tumblr_ly0risWleD1qjod0b.jpg",
            "http://33.media.tumblr.com/tumblr_me4mxy2ssl1rozti5o1_400.gif",
            "http://heavyeditorial.files.wordpress.com/2012/12/crycage.gif",
            "http://media.tumblr.com/tumblr_lo22s0NGhU1qzxr43.gif",
            "http://i.minus.com/idXROKk76N0jM.gif",
            "http://im.ezgif.com/tmp/gif_300x169_1e5bc1.gif",
            "http://33.media.tumblr.com/tumblr_mb4ueqFOXr1rozti5o1_500.gif"
        ],
        "reason": [
            "http://static.bips.channel4.com/bips/520x390/noel-fieldings-luxury-comedy/characters/82de29d9-2f49-4682-8ee2-f735c3183a3f.jpg"
        ],
        "push it": [
            "http://media.tumblr.com/tumblr_m56cfsr9Mz1qzfgf0.gif",
            "http://stream1.gifsoup.com/view4/1396666/push-it-real-good-o.gif",
        ],
        "plan": [
            "http://thetriathloncoach.com/wp-content/uploads/2012/08/I-love-it-when-a-plan-comes-together.jpeg",
            "http://www.bradycarlson.com/wp-content/uploads/2012/12/ateamrecipeforheavybread032010-06.jpg",
            "http://images6.fanpop.com/image/photos/35300000/Hannibal-Smith-the-a-team-35362783-200-200.png",
            "http://www.beingabusinesscelebrity.com/wp-content/uploads/2011/10/i-love-it-when-a-plan-comes-together-the-original-a-team.jpg",
        ],
        "ship it":[
            "http://i.imgur.com/fL6eNiK.jpg",
            "http://c3270052.r52.cf0.rackcdn.com/westerdam-ship-size.jpg",
            "http://welovelocalgovernment.files.wordpress.com/2011/01/ship.jpg",
            "http://media-cdn.tripadvisor.com/media/photo-s/01/57/fd/70/brunel-s-ss-great-britain.jpg",
        ],
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
        ],
        "my kind of": [
            "http://www.biography.com/imported/images/Biography/Images/Profiles/S/Telly-Savalas-9542523-1-402.jpg"
        ],
        "yay": [
            "http://31.media.tumblr.com/0e9d3c5353afe255aab03101db5bc24c/tumblr_mjzn9l8cQ31r6ph6uo1_500.gif",
            "http://25.media.tumblr.com/tumblr_mdm2kdZZVz1rxdkjwo1_500.gif",
            "http://www.reactiongifs.com/wp-content/gallery/dance-party/willsmith.gif",
            "http://www.reactiongifs.com/wp-content/uploads/2013/11/stoked.gif"
        ],
        "savalas": [
            "http://upload.wikimedia.org/wikipedia/commons/9/90/Telly_Savalas_Kojak_1973.JPG",
            "http://images3.makefive.com/images/entertainment/movies/best-james-bond-bad-guys/ernst-stavro-blofeld-as-played-by-telly-savalas-7.jpg",
            "http://www.biography.com/imported/images/Biography/Images/Profiles/S/Telly-Savalas-9542523-1-402.jpg",
            "http://image1.findagrave.com/photos/2010/323/1832_129030321490.jpg",
            "http://img.kimdir.com/kimdir/t/e/5b16633ed7c0fb9a2fa50607696dfdd9e0eeaecb.jpg",
            "http://www.recordsale.de/cdpix/t/telly_savalas-sweet_surprise(1).jpg",
            "http://content9.flixster.com/photo/40/08/13/4008139_ori.jpg"
        ],
        "sad": [
            "http://www.mykindarain.com/wp-content/uploads/2011/10/no-one-likes-sad-panda-no-one-likes-sad-panda.jpg",
            "http://mashable.com/wp-content/uploads/2013/07/Dr.-Who.gif",
            "http://lookrobot.co.uk/files/2013/06/SadCat.jpg",
            "http://tearsoftime.com/wp-content/uploads/2012/07/katy-perry-crying.jpg",
        ],
        "dreams": [
            "http://cdn.shopify.com/s/files/1/0210/4540/products/urban_graphic_cards040_1024x1024.png"
        ],
        "lazy": [
            "http://cdn.shopify.com/s/files/1/0210/4540/products/urban_graphic_cards037_1024x1024.png"
        ],
        "kitten": [
            "http://i.imgur.com/Hr1g87q.gif",
            "http://i.imgur.com/MKyhKRF.gif",
            "http://i.imgur.com/iKHhx1q.gif",
            "http://i.imgur.com/EAheTq8.gif",
            "http://i.imgur.com/4P9RET6.gif",
            "http://i.imgur.com/pVoj4tD.gif",
            "http://cdn.sheknows.com/articles/2014/02/Mike/SheKnows_US/1029471/GIF5.gif",
            "http://www.cutecatgifs.com/wp-content/uploads/2014/02/soon.gif",
            "http://f.cl.ly/items/403c411k0Z1n0j0O052c/raveCats.gif",
            "http://i.imgur.com/act5nY0.gif",
        ],
        "like a boss": [
            "http://upload.wikimedia.org/wikipedia/commons/4/4d/Bruce_Springsteen_1988.jpg",
            "http://i.imgur.com/aEG1ENr.jpg",
            "http://i.telegraph.co.uk/multimedia/archive/02604/Bruce_Springsteen_2604860k.jpg",
            "http://i.imgur.com/eHGYCrv.jpg",
            "http://audiophileparadise.files.wordpress.com/2012/07/bruce-springsteen-002.jpg",
            "http://www.peterguy.merseyblogs.co.uk/bruce-springsteen.jpg",
            "http://www.legacyrecordings.com/media/cache/86/26/86268187fb270d1f4af374b3ef28d53b.jpg",
            "http://static.guim.co.uk/sys-images/Guardian/Pix/pictures/2009/5/25/1243248389162/Bruce-Springsteen-And-The-003.jpg",
            "http://the-flack.com/wp-content/uploads/2014/02/Bruce-Springsteen-1.jpg",
            "http://static.tvtropes.org/pmwiki/pub/images/bruce-springsteen.jpg",
            "http://imgur.com/93k3zBe",
            "http://marshallmatlock.com/wp-content/uploads/2011/05/bruce-springsteen-banner.jpg",
        ],
        "heard": [
            "http://imgur.com/WNf5vJj.jpg",
            "http://www.eabf.org.uk/upload/news/dame-thora-hird.jpg",
            "http://bonfirehealth.com/wp-content/uploads/2011/09/herd.1.gif",
            "http://upload.wikimedia.org/wikipedia/commons/5/5a/Wilderbeest.jpg",
            "http://upload.wikimedia.org/wikipedia/commons/a/a9/Herd_Of_Goats.jpg"
        ],
        "love": [
            "https://www.youtube.com/watch?v=xhrBDcQq2DM",
            "http://www.grammy.com/files/styles/news_photos/public/news/haddaway3.jpg",
            "http://www.becomethesinger.com/wp-content/uploads/2012/11/Haddaway-what-is-love-lyrics-300x197.jpg",
            "http://cdn.7static.com/static/img/sleeveart/00/031/227/0003122749_500.jpg",
            "http://www.blackgate.com/wp-content/uploads/2013/09/image4full.jpg"
        ]
    }

    gifs = ['abandon thread', 'amused', 'birthday', 'bored', 'confused', 'cry', 'crying', 'dance', 
            'deal with it', 'derp', 'disappointed', 'disgusted', 'do not want', 'do want', 'excited', 
            'eye roll', 'facepalm', 'fail',  'funny', 'good job', 'high five', 'hug', 'idk', 
            'i give up', 'incredulous', 'interesting', 'judging you', 'laughing', 'lol', 'love', 'mad', 
            'meh', 'no', 'nod', 'nomming', 'not bad', 'omg', 'o rly', 'party hard', 'pleased', 'popcorn', 
            'rad', 'rage', 'rejected', 'sad', 'sarcastic', 'say what', 'scared', 'serious', 'shut up', 
            'sleepy', 'sorry', 'success', 'suspicious', 'thank you', 'what', 'thumbs up', 'who cares', 
            'wtf', 'yes', 'you don\'t say', 'you tried']


    def get_gif_for_tag(self, tag):
        tag = tag.replace(' ','-').replace('\'','')
        r = requests.get("http://www.reactiongifs.com/tag/" + tag)
        tree = html.fromstring(r.text)
        return tree.xpath('//p/a/img/@src')

    def callback_message(self, conn, mess):
        body = mess.getBody().lower()

        if (getrandbits(3) == 1):
            for keyword in self.gifs:
                if body.startswith(keyword + " ") or \
                body.endswith(" " + keyword) or \
                (" " + keyword + " ") in body:
                    return choice(self.get_gif_for_tag(keyword))

        else:
            for meme in self.memes:
                if body.startswith(meme.replace(' ', '')):
                    self.send(
                        mess.getFrom(),
                        choice(self.memes[meme]),
                        message_type='groupchat'
                    )
                    break
                if body.find(meme) != -1 and randint(1, 10) <= len(self.memes[meme]):
                    self.send(
                        mess.getFrom(),
                        choice(self.memes[meme]),
                        message_type='groupchat'
                    )

    @botcmd
    def sealion(self, mess, args):
        return "http://i.imgur.com/bmfwvDl.gif"

    @botcmd
    def polarpalm(self, mess, args):
        return "http://www.reactionface.info/sites/default/files/images/1310561236052.jpg"

    @botcmd
    def catcloud(self, mess, args):
        return "http://i.imgur.com/11lqTad.jpg"

    @botcmd
    def shipit(self, mess, args):
        return "http://i.imgur.com/fL6eNiK.jpg"
    
    def chuck_norris(self):
        return requests.get("http://api.icndb.com/jokes/random").json()['value']['joke']
        
    @botcmd
    def chuck(self, mess, args):
        return self.chuck_norris()
    
    @botcmd
    def norris(self, mess, args):
        return self.chuck_norris()
        
    @botcmd
    def cage(self, mess, args):
        return choice(self.memes['cage'])
        
    @botcmd
    def basso(self, mess, args):
        panfer = [
            "http://38.media.tumblr.com/2a2eacbd9c5128f423a70e45ef124a2e/tumblr_n9hd3lE80S1qfqs3do2_500.gif",
            "http://static.bips.channel4.com/bips/520x390/noel-fieldings-luxury-comedy/characters/b3dc73e5-892c-4f9d-bb02-e7067ae67f47.jpg",
            "http://boards.420chan.org/mtv/src/1407464476367.gif"
        ]
        return choice(panfer)
