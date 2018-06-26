init python:

    import os
    #config.log = os.path.join(config.gamedir, "test.log")

    # Set the default value.
    if persistent.autofinish is None:
        persistent.autofinish = True

    class ExplodeFactory: # the factory that makes the particles

        def __init__(self, theDisplayable, explodeTime=0, numParticles=10):
            self.displayable = theDisplayable
            self.time = explodeTime
            self.particleMax = numParticles

        def create(self, partList, timePassed):
                newParticles = None
                if partList == None or len(partList) < self.particleMax:
                    if timePassed < self.time or self.time == 0:
                        newParticles = self.createParticles()
                return newParticles


        def createParticles(self):
            timeDelay = renpy.random.random() * 0.6
            return [ExplodeParticle(self.displayable, timeDelay)]

        def predict(self):
            return [self.displayable]

    class ExplodeParticle:



        def __init__(self, theDisplayable, timeDelay):
            self.displayable = theDisplayable
            self.delay = timeDelay
            self.xSpeed = (renpy.random.random() - 0.5) * 25
            self.ySpeed = (renpy.random.random() - 0.5) * 25
            self.x = 640
            self.y = 360

        def update(self, theTime):

            if (theTime > self.delay):
                self.ySpeed += 0.2
                self.x += self.xSpeed
                self.y += self.ySpeed

                if self.x > 1280 or self.x < 0 or self.y > 720 or self.y < 0:
                    return None

            return (self.x, self.y, theTime, self.displayable)

init:
    image bg table = "#262F"
    image dim = "#0008"
    image boom = Particles(ExplodeFactory("card/back.png", numParticles=10, explodeTime = 5.0))

    # Some styles for show text.
    $ style.centered_text.drop_shadow = (2, 2)
    $ style.centered_text.drop_shadow_color = "#000b"

label solstart:
    menu solchoice:
        m "How good are you at Klondike Solitaire?"

        "I'm the fucking best":
            $k = DblKlondike(1)
            m "Alright, how do you like this?"

        "I'm fucking trash":
            $k = Klondike(1)
            m "Alright, go at it then."

label pre_start_game:
    scene bg table
    show dim with dissolve
    #$ k = Klondike(1) #or DblKlondike(1)

label start_game:
    python:
        k.set_sensitive(False)
        k.show()

label quick_continue:
    hide dim with dissolve
    while True:
        python:
            ui.textbutton("Retry", ui.jumps("pre_start_game"), xalign=.02, yalign=.98)
            k.set_sensitive(True)
            event = k.interact()
            if event:
                renpy.checkpoint()
        if event == "win":
            jump win

label win:
    show boom
    show dim
    with dissolve
    m "good work :^){p}this part of the VN brought to you in part by {a=https://github.com/SusanTheCat/SolitaireProject}this GitHub project{/a}"
