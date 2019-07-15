print "Hello World!\n"
import re

class ipl():
    teamName = "No team name set"
    def __init__(self):
        self.teamName = "Team name is not set yet"
    def setTeamName(self, teamname):
        self.teamName = teamname
    def getTeamName(self):
        print(self.teamName)


ip = ipl();
#ip.setTeamName('csk');
print(ip.getTeamName());

name = "tast"

nm = re.search('^t\.*t$', name)

print(nm)
