#Author: Menesay
#Duvi Game
#Start: 10/08/2022
#Finish: 15/08/2022

from tkinter import *
import time

def menu():

    def play():
        main.destroy()
        game()
        

    main = Tk()
    main.geometry("620x620+600+100")
    main.title("DUVİ GAME")
    main.config(background="black")

    icon_image = PhotoImage(file="duvi.png")
    main.iconphoto(True, icon_image)
    
    main_label = Label(main, text="DUVİ GAME", font=("Consolas", 30), pady=10, bg="black", fg="white")
    main_label.pack(side=TOP)

    mini_label = Label(main, text="Escape the DUVİ's", font=("Consolas", 15), pady=10, bg="black", fg="white")
    mini_label.pack()

    mini_label2 = Label(main, text="Use WASD", font=("Consolas", 13), pady=10, bg="black", fg="white")
    mini_label2.pack()
    
    play_button = Button(main, text="Play", font=("Conolas", 20), pady=10, padx=20, bg="black", fg="white", activebackground="black", activeforeground="white", command=play)
    play_button.pack()


    duvigame_image = PhotoImage(file="Duvi_Game.png")

    canvas = Canvas(main, height=300,width=300)

    canvas.create_rectangle(0,0,300,300, fill="black")
    canvas.create_image(140,130, image=duvigame_image)

    canvas.pack(side=BOTTOM)    

    creator_label = Label(main, text="Creator: Menesay", font=("Consolas", 15), pady=10, bg="black", fg="white")
    creator_label.pack()

    year_label = Label(main, text="2022", font=("Consolas", 13), pady=10, bg="black", fg="white")
    year_label.pack()

    main.mainloop()
#-------------------------------------#

stopwatch_running = False

hours, minutes, seconds = 0, 0, 0

#-------------------------------------#
def game():

    def move_up(event):
        canvas.move(vaddab_i, 0, -10)
    def move_down(event):
        canvas.move(vaddab_i, 0, 10)
    def move_left(event):
        canvas.move(vaddab_i, -10, 0)
    def move_right(event):
        canvas.move(vaddab_i, 10, 0)

    def gameover(event):
        pass


    window = Tk()

    window.title("DUVİ GAME")
    window.geometry("800x880+600+100")
    window.config(background="black")
    

    icon_image = PhotoImage(file="duvi.png")
    window.iconphoto(True, icon_image)

    #---------------------------------------------#
    window.bind("<w>", move_up)
    window.bind("<s>", move_down)
    window.bind("<a>", move_left)
    window.bind("<d>", move_right)
    #---------------------------------------------#

    canvas = Canvas(window, height=800, width=800)

    canvas.create_rectangle(0,0,800,800, fill="black")
    canvas.create_text(500,500, text="GAME OVER", font=("Consolas", 30), fill="white", state="hidden")

    canvas.pack()

    #---------------------------------------------#
    
    def stopwatch_start():

        global stopwatch_running

        if not stopwatch_running:
            stopwatch_update()
            stopwatch_running = True

    
    def stopwatch_pause():

        global stopwatch_running

        if stopwatch_running:
            
            stopwatch_label.after_cancel(update_time)
            stopwatch_running = False

    
    def stopwatch_reset():

        global stopwatch_running

        if stopwatch_running:
            
            stopwatch_label.after_cancel(update_time)
            stopwatch_running = False
        
        global hours, minutes, seconds
        hours, minutes, seconds = 0, 0, 0
        
        stopwatch_label.config(text='00:00:00')


    def stopwatch_update():
        
        global hours, minutes, seconds
        seconds += 1

        if seconds == 60:

            minutes += 1
            seconds = 0
        if minutes == 60:

            hours += 1
            minutes = 0
        
        hours_string = f'{hours}' if hours > 9 else f'0{hours}'
        minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
        seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
        
        stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
        
        global update_time
        update_time = stopwatch_label.after(1000, stopwatch_update)
        

    stopwatch_label = Label(window, text='00:00:00', font=('Consolas', 30), bg="black", fg="white")
    stopwatch_label.pack()

    #-----------------Back to Main-------------------#

    def backtomain():
        stopwatch_reset()
        window.destroy()
        menu()

    backtomain_button = Button(window, text="Back", font=("Consolas", 20), bg="black", fg="white", activebackground="black", activeforeground="white")
    backtomain_button.config(command=backtomain)
    backtomain_button.pack(side=BOTTOM)

    
    #-------------------IMAGES-----------------------#
    vaddab_image = PhotoImage(file="vaddab.png")
    vaddab_i = canvas.create_image(400,400, image=vaddab_image, anchor=NW)

    vaddab_i_width = vaddab_image.width()
    vaddab_i_height = vaddab_image.height()


    duvi_image1 = PhotoImage(file="duvi.png")
    duvi_i1 = canvas.create_image(0,0, image=duvi_image1, anchor=NW)

    duvi_i1_width = duvi_image1.width()
    duvi_i1_height = duvi_image1.height()


    duvi_image2 = PhotoImage(file="duvi.png")
    duvi_i2 = canvas.create_image(50,0, image=duvi_image2, anchor=NW)

    duvi_i2_width = duvi_image2.width()
    duvi_i2_height = duvi_image2.height()


    duvi_image3 = PhotoImage(file="duvi.png")
    duvi_i3 = canvas.create_image(0,50, image=duvi_image3, anchor=NW)

    duvi_i3_width = duvi_image3.width()
    duvi_i3_height = duvi_image3.height()

    #--------------------END-IMAGES--------------------#


    duvi_i1_xVelocity = 1
    duvi_i1_yVelocity = 4 

    duvi_i2_xVelocity = 3
    duvi_i2_yVelocity = 1

    duvi_i3_xVelocity = 3
    duvi_i3_yVelocity = 5


    while True:

        coordinates0 = canvas.coords(vaddab_i)
        coordinates1 = canvas.coords(duvi_i1)
        coordinates2 = canvas.coords(duvi_i2)
        coordinates3 = canvas.coords(duvi_i3)

        ###########Cross Coordinates###########
        xcoordinates0 = canvas.coords(vaddab_i)
        xcoordinates0[0] += 10

        ycoordinates0 = canvas.coords(vaddab_i)
        ycoordinates0[1] += 10
        #######################################
        xcoordinates1 = canvas.coords(duvi_i1)
        xcoordinates1[0] += duvi_i1_width
            
        ycoordinates1 = canvas.coords(duvi_i1)
        ycoordinates1[1] += duvi_i1_height
        #######################################
        xcoordinates2 = canvas.coords(duvi_i2)
        xcoordinates2[0] += duvi_i2_width

        ycoordinates2 = canvas.coords(duvi_i2)
        ycoordinates2[1] += duvi_i2_height
        #######################################
        xcoordinates3 = canvas.coords(duvi_i3)
        xcoordinates3[0] += duvi_i3_width

        ycoordinates3 = canvas.coords(duvi_i3)
        ycoordinates3[1] += duvi_i3_height


        #############Cross Events###############
        if xcoordinates1[0] >= coordinates0[0] >= coordinates1[0] and ycoordinates1[1] >= coordinates0[1] >= coordinates1[1]:
            canvas.create_text(400,400, text="GAME OVER", font=("Consolas", 30), fill="white")
            window.bind("<w>", gameover)
            window.bind("<s>", gameover)
            window.bind("<a>", gameover)
            window.bind("<d>", gameover)

            canvas.create_text(400,500, text="Press R to play again", font=("Consolas", 20), fill = "white")
            canvas.create_text(400,550, text="Press Q to quit", font=("Consolas", 15), fill = "white")

            stopwatch_pause()

            break

        if xcoordinates2[0] >= coordinates0[0] >= coordinates2[0] and ycoordinates2[1] >= coordinates0[1] >= coordinates2[1]:
            canvas.create_text(400,400, text="GAME OVER", font=("Consolas", 30), fill="white")
            window.bind("<w>", gameover)
            window.bind("<s>", gameover)
            window.bind("<a>", gameover)
            window.bind("<d>", gameover)

            canvas.create_text(400,500, text="Press R to play again", font=("Consolas", 20), fill = "white")
            canvas.create_text(400,550, text="Press Q to quit", font=("Consolas", 15), fill = "white")

            stopwatch_pause()

            break

        if xcoordinates3[0] >= coordinates0[0] >= coordinates3[0] and ycoordinates3[1] >= coordinates0[1] >= coordinates3[1]:
            canvas.create_text(400,400, text="GAME OVER", font=("Consolas", 30), fill="white")
            window.bind("<w>", gameover)
            window.bind("<s>", gameover)
            window.bind("<a>", gameover)
            window.bind("<d>", gameover)

            canvas.create_text(400,500, text="Press R to play again", font=("Consolas", 20), fill = "white")
            canvas.create_text(400,550, text="Press Q to quit", font=("Consolas", 15), fill = "white")

            stopwatch_pause()

            break
        ########################################



        if (coordinates0[0] < 0):
            canvas.move(vaddab_i, 10, 0)
            
        if (coordinates0[1] < 0):   
            canvas.move(vaddab_i, 0, 10)

        if (coordinates0[0] >= (800 - vaddab_i_width)):
            canvas.move(vaddab_i, -10, 0)

        if (coordinates0[1] >= (800 - vaddab_i_height)):
            canvas.move(vaddab_i, 0, -10)


        if (coordinates1[0] >= (800 - duvi_i1_width) or coordinates1[0] < 0):
            duvi_i1_xVelocity = -duvi_i1_xVelocity
        if (coordinates1[1] >= (800 - duvi_i1_height) or coordinates1[1] < 0):
            duvi_i1_yVelocity = -duvi_i1_yVelocity

        if (coordinates2[0] >= (800 - duvi_i2_width) or coordinates2[0] < 0):
            duvi_i2_xVelocity = -duvi_i2_xVelocity
        if (coordinates2[1] >= (800 - duvi_i2_height) or coordinates2[1] < 0):
            duvi_i2_yVelocity = -duvi_i2_yVelocity

        if (coordinates3[0] >= (800 - duvi_i3_width) or coordinates3[0] < 0):
            duvi_i3_xVelocity = -duvi_i3_xVelocity
        if (coordinates3[1] >= (800 - duvi_i3_height) or coordinates3[1] < 0):
            duvi_i3_yVelocity = -duvi_i3_yVelocity

        canvas.move(duvi_i1, duvi_i1_xVelocity, duvi_i1_yVelocity)
        canvas.move(duvi_i2, duvi_i2_xVelocity, duvi_i2_yVelocity)
        canvas.move(duvi_i3, duvi_i3_xVelocity, duvi_i3_yVelocity)

        stopwatch_start()
        window.update()
        time.sleep(0.01)
        #----------------While-End-----------------------#

    #-------------------HABULEN---------------------#

        def habulen7(event):
            print("Duvi: Uüa, ıvyg (öldü)")

        def habulen6(event):
            window.bind("<n>", habulen7)

        def habulen5(event):
            window.bind("<e>", habulen6)

        def habulen4(event):
            window.bind("<l>", habulen5)

        def habulen3(event):
            window.bind("<u>", habulen4)

        def habulen2(event):
            window.bind("<b>", habulen3)

        def habulen1(event):
            window.bind("<a>", habulen2)

        def habulen():
            window.bind("<h>", habulen1)


        habulen()


    #--------------------HABULEN--------------------#
        
    ##########GAME#END#########################

    def playagain(event):

        stopwatch_reset()
        window.destroy()
        game()
        

    def quit(event):

        window.destroy()

    window.bind("<r>", playagain)
    window.bind("<q>", quit)
    window.mainloop()

menu()
