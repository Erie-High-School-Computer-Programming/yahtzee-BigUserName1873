class Scorecard:
    def __init__(self):
        self.score = 0
        self.aces_used = False
        self.two_used = False
        self.threes_used = False
        self.fours_used = False
        self.fives_used = False
        self.sixes_used = False
        self.three_of_kind_used = False
        self.four_of_kind_used = False
        self.full_house_used = False        
        self.sm_straight_used = False
        self.lg_stragith_used = False
        self.yahtzee_used = False
        self.chance_used = False
        
        def score_aces(self, dice:list):
            '''Scores the aces. Adds all the ones and adds it to the scorecard.'''
            round_score = 0
            for die in dice:
                if die == 1:
                    round_score += 1

            self.aces_used = True
            return round_score
        
        def score_twos(self, dice:list):
            '''Scores the twos. Adds all the twos and adds it to the scorecard.'''
            round_score = 0
            for die in dice:
                if die == 2:
                    round_score += 2

            self.two_used = True
            return round_score
        
        def score_threes(self, dice:list):
            '''Scores the threes. Adds all the threes and adds it to the scorecard.'''
            round_score = 0
            for die in dice:
                if die == 3:
                    round_score += 3

            self.threes_used = True
            return round_score
        
        def score_fours(self, dice:list):
            '''Scores the fours. Adds all the fours and adds it to the scorecard.'''
            round_score = 0
            for die in dice:
                if die == 4:
                    round_score += 4

            self.fours_used = True
            return round_score
        
        def score_fives(self, dice:list):
            '''Scores the fives. Adds all the fives and adds it to the scorecard.'''
            round_score = 0
            for die in dice:
                if die == 5:
                    round_score += 5

            self.fives_used = True
            return round_score
        
        def score_sixes(self, dice:list):
            '''Scores the sixes. Adds all the sixes and adds it to the scorecard.'''
            round_score = 0
            for die in dice:
                if die == 6:
                    round_score += 6

            self.sixes_used = True
            return round_score