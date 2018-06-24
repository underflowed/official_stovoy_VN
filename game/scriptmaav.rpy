define rpypos = Position(xpos=0.15, xanchor=0.0, ypos=0.5, yanchor=0.5)
define rpy = Character("Ren'Py Logo", color="#FF7F7F")

label rpymeme: #selectable by choosing to actually develop Evades.io
    scene bg room with fade
    show rpy at rpypos with dissolve
    rpy "What the hell is this!?"
    show m kukuru at Position(xpos=0.95, xanchor=1.0, ypos=0.5, yanchor=0.5) with dissolve
    m   "a visual novel? :^)"
    rpy "You call this a visual novel?  This is an abomination of the fantastic Ren'Py engine!"
    m   "is that an issue? :^)"
    rpy "YES"
    m   "Well...  We can't have that now, can we..."
    rpy "..."
    m   "..."
    show m kukugun at Position(xpos=0.25, xanchor=0.0, ypos=0.5, yanchor=0.5)
    m   "u die now"
    show image(im.Grayscale("rpy.png")) as rpy at rpypos
    rpy "shit"

    play music "hl2_song23_suitsong3.mp3" noloop
    scene black with Fade(8.5, 0.0, 0.0)

    play sound "gunshot.ogg"
    "Maavrik mercilessly murders that stupid Ren'Py logo before she could possibly shittalk this VN any longer."
    "that was a joke i think the ren'py logo is very cute"
    play sound "Wilhelm_Scream.ogg"
    rpy "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

    stop music
    stop sound
    scene bg room
    show m kukuru at truecenter
    m   "Great, now that we have that dumb logo out of the way, Stovoy can finally get back to developing Evades.io!"

    #get back to main game and remove this choice
    scene black with fade
    "Good work, you got the Good Developer ending." #improve this ending? idk :^)
    return
