import sqlite3, os
from sqlite3 import Error
import tkinter as tk
positions = ["Team1-Left", "Team1-Right", "Team2-Left", "Team2-Right"]
stats = ["Hit", "Save", "Sink", "Ace", "FR"]
global player1, player2, player3, player4 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def add_player_action(conn, actionDetails):
    """
    Create a new action into the actions table
    :param conn:
    :param player:
    :return: project id
    """
    sql = ''' INSERT INTO actions(id, playerName, action)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, actionDetails)
    return cur.lastrowid
    
def select_all_actions(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM actions")

    rows = cur.fetchall()

    for row in rows:
        print(row)    

class Action:
    def __init__(self, PlayerName, actionType):
        self.PlayerName = PlayerName #input("\n PlayerName: ")
        self.actionType = actionType #input("\n Action Type: ")
        #self.turn = turn #input("\n turn: ")

def action_intput(player, action):
    """creates an object reqiring input for name, action type and turn
    """
    #actioninput = Action(input("name: "),input("action type: "), input("turn: "))
    actioninput = Action(player, action)
    return actioninput

def new_game(conn, name, matchid, position):
    insertPlayer = ''' INSERT INTO players(name, matchId, position, hits, saves, sinks, aces, FRs)
              VALUES(?,?,?, 0, 0, 0, 0, 0) '''
    
    cur = conn.cursor()
    cur.execute(insertPlayer, (name, matchid, position))
    
def assign_matchId(conn):
    select_matchId = "SELECT matchId from players order by matchId desc LIMIT 1"
    cur = conn.cursor()
    cur.execute(select_matchId)
    matchid = cur.fetchone()
    return matchid

def assign_actionId(conn):
    select_actionId = "SELECT id from actions order by id desc LIMIT 1"
    cur = conn.cursor()
    cur.execute(select_actionId)
    #print("id")
    id=cur.fetchone()
    if id is None:
        id = 0
    elif type(id) is tuple:
        id = id[0]+1       
    else:
        id = id+1
    return id

def count_actions(conn, player, action):
    count = "SELECT count(*) from actions where playerName = ? and action = ?"
    cur = conn.cursor()
    cur.execute(count, (player, action))
    value = cur.fetchone()
    return value

def PlayerName(conn, matchId, position):
    select_player = "SELECT name from players where matchId = ? and position = ?"
    cur = conn.cursor()
    cur.execute(select_player, (matchId, position))
    #print("id")
    player=cur.fetchone()
    return player

def setup(players):
    #database = r"C:\Python\sqlite\db\DB1.db"
    database = os.getcwd() + "\Database.db"
    sql_create_actions_table = """ CREATE TABLE IF NOT EXISTS actions (
                                        id integer PRIMARY KEY,
                                        playerName text NOT NULL,
                                        action text
                                        
                                    ); """
    sql_create_players_table = """ CREATE TABLE IF NOT EXISTS players (
                                        name text,
                                        matchId int,
                                        position text,
                                        hits int,
                                        saves int,
                                        sinks int,
                                        aces int,
                                        FRs int
                                    ); """
    

    conn = create_connection(database)
    #print("connected to %s" %conn)
    if conn is not None:
        # create actions and players tables
        create_table(conn, sql_create_actions_table)
        create_table(conn, sql_create_players_table)
        
    else:
        print("Error! cannot create the database connection.")
    matchid = assign_matchId(conn)  #Pull the last used match id then add 1
    if matchid is not None:
        matchid = matchid[0] + 1
    else:
        matchid = 000

    for  position, player in zip(positions, players):

        #player = input("input %s's name: " %position)
        new_game(conn, player, matchid, position)

    global player1, player2, player3, player4 
    player1 = PlayerName(conn, matchid, positions[0]) 
    player2 = PlayerName(conn, matchid, positions[1])
    player3 = PlayerName(conn, matchid, positions[2])
    player4 = PlayerName(conn, matchid, positions[3])
    player1 = player1[0]
    player2 = player2[0]
    player3 = player3[0]
    player4 = player4[0]
    
    #while True:
    #    rungame(conn)
    #select_all_actions(conn)
    conn.commit()
    conn.close()
    
    #return matchid, player1, player2, player3, player4

def rungame():    
    database = os.getcwd() + "\Database.db"
    conn = create_connection(database)
    id1 = assign_actionId(conn)
    
    #while console != "done":

    a = action_intput("Chris", "Hit")
    actionDetails = (id, a.PlayerName, a.actionType)
    add_player_action(conn, actionDetails)
    conn.commit()
    #select_all_actions(conn)
    conn.close()

def player_hit(position, stat):
    database = os.getcwd() + "\Database.db"
    conn = create_connection(database)
    id1 = assign_actionId(conn)
    matchid = assign_matchId(conn)
    player = PlayerName(conn, matchid[0], position)
    id = assign_actionId(conn)
    a =  Action(player[0], stat)
    action = (id, a.PlayerName, a.actionType)
    add_player_action(conn, action)
    conn.commit()
    conn.close()



def print_stats():
    #database = os.getcwd() + "\Database.db"
    #conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT * FROM actions")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def game_over():
    database = os.getcwd() + "\Database.db"
    conn = create_connection(database)
    matchid = assign_matchId(conn)
    update_players_table = """
                            UPDATE players--(name, matchid, position, hits, saves, sinks, aces, FRs)
                            SET hits = hits + (select count(*) from actions where action = 'Hit' and playerName = ?), 
                                saves = saves + (select count(*) from actions where action = 'Save' and playerName = ?),
                                sinks = sinks + (select count(*) from actions where action = 'Sink' and playerName = ?),
                                aces = aces + (select count(*) from actions where action = 'Ace' and playerName = ?),
                                FRs = FRs + (select count(*) from actions where action = 'FR' and playerName = ?)  
                            Where matchid = ? and name = ?;
                            """
    delete_actions = """ 
                     Delete from actions;   
                        """
    matchid = matchid[0]
    player1 = PlayerName(conn, matchid, positions[0]) 
    player2 = PlayerName(conn, matchid, positions[1])
    player3 = PlayerName(conn, matchid, positions[2])
    player4 = PlayerName(conn, matchid, positions[3])
    player1 = player1[0]
    player2 = player2[0]
    player3 = player3[0]
    player4 = player4[0]
    players = [player1, player2, player3, player4]
    for player in players:
        cur = conn.cursor()  
        cur.execute(update_players_table, (player, player, player, player, player, matchid, player))
        #cur.execute(update_players_table)
        conn.commit()
    cur = conn.cursor()
    cur.execute(delete_actions)
    conn.commit()
if __name__ == '__main__':
    setup()
    #player_hit(positions[0])
    #game_over()

    #matchid, player1, player2, player3, player4 = setup() 
    #print(player1, player2, player3, player4)  

database = os.getcwd() + "\Database.db"
conn = create_connection(database)
#matchid = assign_matchId(conn)

