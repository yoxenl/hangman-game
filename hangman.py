import funktioner as f
import turtle #grafik gui osv

playing = True

#creates three brushes 
t = turtle.Turtle()
t1 = turtle.Turtle() 
t2 = turtle.Turtle()

scr = turtle.Screen()

scr.setup(
    startx = 70, 
    starty = None)

scr.title('Hangman Game')

while playing: #gameloop
    f.hide_brushes(t, t1, t2)
    tema = f.welcome()
    if tema.lower() == 'q':
        break
    ordet = f.choose_word(tema)
    f.gissning(ordet, tema)
    fortsätta = f.play_again()
    if fortsätta == False:
        playing = False

#this is the end of the code