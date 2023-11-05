team_2_players = {}




#map team name to players in dict
def team_dict():
    team_name = input("What is your team name?").upper()
    team_size = input("How many players are on your team?")
    team_members = input("Who is on your team? (Enter UBITs, include yourself and split UBITs by commas)")
    if team_name in team_2_players:
        print("Team name already taken")
        team_dict()
    else:
        members = team_members.split(",") #splits members of team up
        mem_list = () #list of members 
        i = 0
        while i < team_size:
            mem_list += members[i]
            i+=1
        team_2_players[team_name] = mem_list #maps team name to list of members

#remove team from dict
def team_remove():
    teamName = input("What is your team name?").upper()
    del team_2_players[teamName]