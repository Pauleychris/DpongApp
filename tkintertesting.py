import tkinter as tk
import Dpong_V2 as D
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.draw_names() 
        #self.get_text()

        
    def create_widgets(self):
        #self.P1Hitcount = tk.StringVar()
        self.P1Hitcount = tk.StringVar()
        def get_text(self, P1Hitcount):
            P1Hitcount = tk.StringVar()
            P1Hitcount.set(D.count_actions(D.conn, D.PlayerName(D.conn, D.assign_matchId(D.conn)[0], D.positions[0])[0], "Hit")[0])
            self.after(1000,lambda:get_text(self, self.P1Hitcount))
            return P1Hitcount
        
        self.setupplayers = tk.Button(self)
        self.setupplayers["text"] = "Enter Players and \n Start New Game"
        self.setupplayers["command"] = self.popout#self.setup
        self.setupplayers.grid(row=0, column=0)
        #self.P1Hitcount = get_text(self, self.P1Hitcount)
        #self.P1Hitcount = get_text()
        #self.P1Hitcount = tk.StringVar(self)
        #self.P1Hitcount.set(D.count_actions(D.conn, D.PlayerName(D.conn, D.assign_matchId(D.conn)[0], D.positions[0])[0], "Hit")[0])
        #self.P1Hitcount_str = self.P1Hitcount
        self.P1Hit = tk.Button(self, text=root.P1Hitcount.get(), command=(self.player1_hit))#, self.get_text())
        self.P1Hit.grid(row=1, column=1)       
        
        self.P2Hit = tk.Button(self, text=" Hit ", command=self.player2_hit)
        self.P2Hit.grid(row=1, column=2)        
        self.P3Hit = tk.Button(self, text=" Hit ", command=self.player3_hit)
        self.P3Hit.grid(row=1, column=3)         
        self.P4Hit = tk.Button(self, text=" Hit ", command=self.player4_hit)
        self.P4Hit.grid(row=1, column=4)         
        
        self.P1Save = tk.Button(self, text="Save", command=self.player1_save)
        self.P1Save.grid(row=2, column=1)
        self.P2Save = tk.Button(self, text="Save", command=self.player2_save)
        self.P2Save.grid(row=2, column=2)
        self.P3Save = tk.Button(self, text="Save", command=self.player3_save)
        self.P3Save.grid(row=2, column=3)
        self.P4Save = tk.Button(self, text="Save", command=self.player4_save)
        self.P4Save.grid(row=2, column=4)

        self.P1Sink = tk.Button(self, text="Sink", command=self.player1_sink)
        self.P1Sink.grid(row=3, column=1)
        self.P2Sink = tk.Button(self, text="Sink", command=self.player2_sink)
        self.P2Sink.grid(row=3, column=2)
        self.P3Sink = tk.Button(self, text="Sink", command=self.player3_sink)
        self.P3Sink.grid(row=3, column=3)
        self.P4Sink = tk.Button(self, text="Sink", command=self.player4_sink)
        self.P4Sink.grid(row=3, column=4)
       
        self.P1ace = tk.Button(self, text=" Ace ", command=self.player1_ace)
        self.P1ace.grid(row=4, column=1)
        self.P2ace = tk.Button(self, text=" Ace ", command=self.player2_ace)
        self.P2ace.grid(row=4, column=2)
        self.P3ace = tk.Button(self, text=" Ace ", command=self.player3_ace)
        self.P3ace.grid(row=4, column=3)
        self.P4ace = tk.Button(self, text=" Ace ", command=self.player4_ace)
        self.P4ace.grid(row=4, column=4)

        self.GameOver = tk.Button(self, text="Game Over", command=self.Game_Over)
        self.GameOver.grid(row=9, column=1)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)           
        self.quit.grid(row=10,column=0)

        self.update = tk.Button(self, text="Update names", command=self.draw_names)
        self.update.grid(row=0,column=6)
        """self.matchIdtext = tk.IntVar(self)
        self.matchIdtext.set(self.matchId)
        self.matchid = tk.Button(self, text=matchIdtext, command=self.matchId)
        self.matchid.grid(row=8, column=0)"""

    def draw_names(self):
        self.playername = tk.StringVar(self) #define the variable as a tk.string 
        self.playername.set(D.PlayerName(D.conn, D.assign_matchId(D.conn)[0], D.positions[0])[0]) #set the value for the variable
        self.Player1name = tk.Label(self, text=self.playername.get())
        self.Player1name.grid(row=0,column=1)
        
        self.playername.set(D.PlayerName(D.conn, D.assign_matchId(D.conn)[0], D.positions[1])[0]) #set the value for the variable
        self.Player2name = tk.Label(self, text=self.playername.get())
        self.Player2name.grid(row=0,column=2)
        
        self.playername.set(D.PlayerName(D.conn, D.assign_matchId(D.conn)[0], D.positions[2])[0]) #set the value for the variable
        self.Player3name = tk.Label(self, text=self.playername.get())
        self.Player3name.grid(row=0,column=3)
        
        self.playername.set(D.PlayerName(D.conn, D.assign_matchId(D.conn)[0], D.positions[3])[0]) #set the value for the variable
        self.Player4name = tk.Label(self, text=self.playername.get())
        self.Player4name.grid(row=0,column=4)
        
        self.playername.set(D.assign_matchId(D.conn)[0]) #set the value for the variable
        self.Player4name = tk.Label(self, text="Match ID \n" + self.playername.get())
        self.Player4name.grid(row=1,column=0)

    def setup(self):
        D.setup()
    def matchId(self):
        #database = os.getcwd() + "\Database.db"
        #conn = D.create_connection(database)
        matchid = D.assign_matchId(D.conn)
        print(matchid[0])
        return matchid[0]

    def player1_hit(self):
        D.player_hit(D.positions[0], D.stats[0])
    def player2_hit(self):
        D.player_hit(D.positions[1], D.stats[0])
    def player3_hit(self):
        D.player_hit(D.positions[2], D.stats[0])
    def player4_hit(self):
        D.player_hit(D.positions[3], D.stats[0])
    
    def player1_save(self):
        D.player_hit(D.positions[0], D.stats[1])
    def player2_save(self):
        D.player_hit(D.positions[1], D.stats[1])
    def player3_save(self):
        D.player_hit(D.positions[2], D.stats[1])
    def player4_save(self):
        D.player_hit(D.positions[3], D.stats[1])
    
    def player1_sink(self):
        D.player_hit(D.positions[0], D.stats[2])
    def player2_sink(self):
        D.player_hit(D.positions[1], D.stats[2])
    def player3_sink(self):
        D.player_hit(D.positions[2], D.stats[2])
    def player4_sink(self):
        D.player_hit(D.positions[3], D.stats[2])
    
    def player1_ace(self):
        D.player_hit(D.positions[0], D.stats[3])
    def player2_ace(self):
        D.player_hit(D.positions[1], D.stats[3])
    def player3_ace(self):
        D.player_hit(D.positions[2], D.stats[3])
    def player4_ace(self):
        D.player_hit(D.positions[3], D.stats[3])
    
    def player1_FR(self):
        D.player_hit(D.positions[0], D.stats[4])    
    def player2_FR(self):
        D.player_hit(D.positions[1], D.stats[4])       
    def player3_FR(self):
        D.player_hit(D.positions[2], D.stats[4])       
    def player4_FR(self):

        D.player_hit(D.positions[3], D.stats[4])       
    def Game_Over(self):
        D.game_over()
    def popout(self):
        self.w=popupWindow(self.master)
        self.setupplayers["state"] = "disabled" 
        self.master.wait_window(self.w.top)
        self.setupplayers["state"] = "normal"
    #playername = tk.StringVar()
    #playername.set(D.PlayerName(D.conn, D.assign_matchId(D.conn)[0], D.positions[0])[0])

class popupWindow(object):
    def __init__(self,master):
        top=self.top=tk.Toplevel(master)
        self.l=tk.Label(top,text="Enter Player Names")
        self.l.grid(row=0,column=1)
        self.p1l=tk.Label(top, text="Team 1- Left")
        self.p1l.grid(row=1,column=0)
        self.p2l=tk.Label(top, text="Team 1- Right")
        self.p2l.grid(row=2,column=0)
        self.p3l=tk.Label(top, text="Team 2- Left")
        self.p3l.grid(row=3,column=0)
        self.p4l=tk.Label(top, text="Team 2- Right")
        self.p4l.grid(row=4,column=0)
        self.e1=tk.Entry(top)
        self.e1.grid(row=1,column=1)
        self.e2=tk.Entry(top)
        self.e2.grid(row=2,column=1)
        self.e3=tk.Entry(top)
        self.e3.grid(row=3,column=1)
        self.e4=tk.Entry(top)
        self.e4.grid(row=4,column=1)
        self.b=tk.Button(top,text='Ok',command=self.cleanup)
        self.b.grid(row=5,column=5)
        
    def cleanup(self):
        self.player1=self.e1.get()
        self.player2=self.e2.get()
        self.player3=self.e3.get()
        self.player4=self.e4.get()
        self.players = [self.player1, self.player2, self.player3, self.player4]
        D.setup(self.players)
        self.top.destroy()

root = tk.Tk()
root.geometry('600x300')
root.title('Dpong')
matchIdtext = tk.IntVar()
matchIdtext.set(D.assign_matchId(D.conn))
"""playername = tk.StringVar() #define the variable as a tk.string 
playername.set(D.PlayerName(D.conn, D.assign_matchId(D.conn)[0], D.positions[0])[0]) #set the value for the variable
Player1name = tk.Label(text=playername.get())
Player1name.grid(row=0,column=1)"""
def get_text(root, P1Hitcount):
    root.P1Hitcount = tk.StringVar()
    root.P1Hitcount.set(D.count_actions(D.conn, D.PlayerName(D.conn, D.assign_matchId(D.conn)[0], D.positions[0])[0], "Hit")[0])
    print(root.P1Hitcount.get())
    root.after(1000, lambda:get_text(root, root.P1Hitcount))

    #return P1Hitcount.get()
#P1Hitcount = get_text(root)
P1Hitcount = tk.StringVar(value="")
get_text(root, P1Hitcount)
app = Application(master=root)
app.mainloop()