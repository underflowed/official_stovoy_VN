define rpypos = Position(xpos=0.15, xanchor=0.0, ypos=0.5, yanchor=0.5)
define mpos = Position(xpos=0.95, xanchor=1.0, ypos=0.5, yanchor=0.5)
define rpy = Character("Ren'Py Logo", color="#FF7F7F")

label rpymeme: #selectable by choosing to actually develop Evades.io, leads to Good Developer ending
    scene bg room with fade
    show rpy at rpypos with dissolve
    rpy "What the hell is this!?"
    show m kukuru at mpos with dissolve:
        zoom 0.5
    m   "a visual novel? :^)"
    rpy "You call this a visual novel?  This is an abomination of the fantastic Ren'Py engine!"
    m   "is that an issue? :^)"
    rpy "YES"
    m   "Well...  We can't have that now, can we..."
    rpy "..."
    m   "..."
    show m kukugun at Position(xpos=0.25, xanchor=0.0, ypos=0.5, yanchor=0.5):
        zoom 1.0
    m   "u die now"
    show image(im.Grayscale("rpy.png")) as rpy at rpypos
    rpy "shit"

    play music "hl2_song23_suitsong3.mp3" noloop
    scene black with Fade(8.5, 0.0, 0.0)

    play sound "gunshot.ogg"
    "Maavrik mercilessly murders that stupid Ren'Py logo before she could possibly shittalk this VN any longer.{p}(that was a joke i think the ren'py logo is very cute)"
    play sound "Wilhelm_Scream.ogg"
    rpy "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

    stop music
    stop sound
    scene bg room
    show m kukuru at truecenter
    m   "Great, now that we have that dumb logo out of the way, Stovoy can finally get back to developing Evades.io!"
    show m kukuru at mpos:
        zoom 0.5
    show s normal at rpypos
    s   "Wow, thanks a bunch Maavrik!  Now I can finally be at peace and finish refactoring Evades.io while Twitch chat tries to figure out what the fuck just happened!"

    #Good Developer ending
    #probably needs music, along with the rest of this game
    scene black with fade
    "And with that, Stovoy finished refactoring Evades.io successfully.{p}Stovoy felt the satisfaction of actually completing something he set out to do, and lived life happily ever after."
    "{b}Good work, you got the Good Developer ending.{/b}"
    return
