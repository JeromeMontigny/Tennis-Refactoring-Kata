class TennisGame3:
    #on pourrait ici mettre le seuil de 4 pour deuce, mais je ne sais pas le nommer. deuce_threshold peut-être?
    points_as_text = ["Love", "Fifteen", "Thirty", "Forty"]
    
    def __init__(self, player1Name, player2Name):
        self.player1 = Player(player1Name)
        self.player2 = Player(player2Name)
        
    def won_point(self, player_name):
        if player_name == self.player1.name:
            self.player1.win_point()
        else:
            self.player2.win_point()
    
    def score(self):
        if self.before_deuce():
            if self.are_score_equals():
                return self.point_as_text(self.player1.points) + "-All"
            else :
                return self.point_as_text(self.player1.points) + "-" + self.point_as_text(self.player2.points)
        else:
            if self.are_score_equals():
                return "Deuce"
            elif self.is_score_difference_one():
                return "Advantage " + self.leader()
            else :
                return "Win for " + self.leader()
    
    def before_deuce(self):
        return (self.player1.points < 4 and self.player2.points < 4) and (self.player1.points != 3 or self.player2.points != 3)

    def are_score_equals(self):
        return (self.player1.points == self.player2.points)
        
    def point_as_text(self,point):
        return self.points_as_text[point]

    def leader(self):
        if self.player1.points > self.player2.points:
            return self.player1.name
        else:
            return self.player2.name

    def is_score_difference_one(self):
        return self.player1.points-self.player2.points in [-1,1]

    
class Player:
    def __init__(self,name):
        self.name = name
        self.points = 0
    
    def setPoints(self,points):
        self.points = points

    def win_point(self):
        self.points += 1
