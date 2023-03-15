class Player:
    def __init__(self,name):
        self.nom= name
        self.musiques = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        
        }
    
    #on fait en sorte que si le score de la musique qui la précède alors elle devient le meilleur score du joueur
    def add_musiques(self,idSong,score):
        if score > self.musiques[idSong]:
            self.musiques[idSong] = score
    #on definit le meilleur score du joueur
    def get_best_score(self):
        return max(self.musiques.values())

    #On définit le pire score du joueur 
    def get_worst_score(self):
        return min([score for score in self.musiques.values() if score > 0], default=50)

    #On définit la moyenne des scores obtenues par le joueur
    def get_average_score(self):
        scoretotal = sum([score for score in self.musiques.values() if score > 0])
        count = len([score for score in self.musiques.values() if score > 0])
        return scoretotal / count if count > 0 else 0

class Karaoke:
    def __init__(self, songs):
        self.players = []
        self.musiques = songs

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        if len(self.players) > 1:
            self.players.remove(player)

    def get_best_score(self, song_id):
        best_score = 0
        for player in self.players:
            score = player.musiques[song_id]
            if score > best_score:
                best_score = score
        return best_score

    def get_best_score_total(self):
        best_score_total = 0
        for player in self.players:
            score_total = sum(player.musiques.values())
            if score_total > best_score_total:
                best_score_total = score_total
        return best_score_total

    def get_best_average(self):
        best_average = 0
        for player in self.players:
            average = player.get_average_score()
            if average > best_average:
                best_average = average
        return best_average
karaoke = Karaoke(['musique 1', 'musique 2', 'musique 3'])



