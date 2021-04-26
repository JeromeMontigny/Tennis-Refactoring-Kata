# -*- coding: utf-8 -*-

class TennisGame1:

    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.p1points += 1
        else:
            self.p2points += 1
    
    def score(self):
        """renvoie une String donnant le score
        """
        results_dict = {
                    0 : "Love",
                    1 : "Fifteen",
                    2 : "Thirty",
                    3 : "Forty",
                }
        result = ""

        # si les joueurs sont à égalité
        if (self.p1points==self.p2points):
            if (self.p1points>=3) :
                result = "Deuce"
            else :
                result = results_dict[self.p1points] + "-All"
        # sinon, si l'un d'entre a au moins 4 points
        elif (self.p1points>=4 or self.p2points>=4):
            minusResult = self.p1points-self.p2points
            if (minusResult==1):
                result ="Advantage " + self.player1Name
            elif (minusResult ==-1):
                result ="Advantage " + self.player2Name
            elif (minusResult>=2):
                result = "Win for " + self.player1Name
            else:
                result ="Win for " + self.player2Name
        else:
            result = "{}-{}".format(results_dict[self.p1points],results_dict[self.p2points])
        return result

class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1 = Player(player1Name)
        self.player2 = Player(player2Name)
        
    def won_point(self, playerName):

        # Note : on pourrait ici refactoriser en passant directement le joueur qui a gagné le point et on n'aurait pas de if mais cela serait cassant
        if playerName == self.player1.name:
            self.player1.win_point()
        else:
            self.player2.win_point()
    
    def score(self):
        result = ""
        results_list = ["Love","Fifteen","Thirty","Forty"]
        p1score = self.player1.score
        p2score = self.player2.score
        if (p1score == p2score):
            if (p1score<3):
                result = results_list[p1score]
                result += "-All"
            else:
                result = "Deuce"
        elif (p1score<4 and p2score<4):
            P1res = results_list[p1score]
            P2res = results_list[p2score]
            result = P1res + "-" + P2res
        
        
        if (p1score > p2score and p2score >= 3):
            result = "Advantage " + self.player1.name
        if (p2score > p1score and p1score >= 3):
            result = "Advantage " + self.player2.name
        
        if (p1score>=4 and (p1score-p2score)>=2):
            result = "Win for " + self.player1.name
        if (p2score>=4 and (p2score-p1score)>=2):
            result = "Win for " + self.player2.name
        return result


class Player:
    def __init__(self,name):
        self.name = name
        self.score = 0
    
    def setScore(self,score):
        self.score = score

    def win_point(self):
        self.score += 1


class TennisGame3:
    def __init__(self, player1Name, player2Name):
        self.player1name = player1Name
        self.player2name = player2Name
        self.p1score = 0
        self.p2score = 0
        
    def won_point(self, player_name):
        if player_name == self.player1name:
            self.p1score += 1
        else:
            self.p2score += 1
    
    def score(self):
        # Note : on aurait pu mettre le résultat à r puisque le scope est assez court
        if (self.p1score < 4 and self.p2score < 4) and (self.p1score + self.p2score < 6):
            possible_scores = ["Love", "Fifteen", "Thirty", "Forty"]
            result = possible_scores[self.p1score]
            return result + "-All" if (self.p1score == self.p2score) else result + "-" + possible_scores[self.p2score]
        else:
            if (self.p1score == self.p2score):
                return "Deuce"
            result = self.player1name if self.p1score > self.p2score else self.player2name
            return "Advantage " + result if ((self.p1score-self.p2score)*(self.p1score-self.p2score) == 1) else "Win for " + result
