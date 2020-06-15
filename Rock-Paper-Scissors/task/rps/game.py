# Write your code here
import random


class RockPaperScissors:

    def __init__(self):
        self.command = None
        self.options = ['rock', 'paper', 'scissors']
        self.AI_answer = None
        self.ai_word = None
        self.pl_name = None
        self.file = None
        self.rating = 0
        self.new_options = []
        self.winners_list = None
        self.losers_list = None
        self.num = 1

    def lost(self):
        print(f'Sorry, but computer chose {self.ai_word}')

    def win(self):
        print(f'Well done. Computer chose {self.ai_word} and failed')
        self.rating += 100

    def read_rating(self, pl_name):
        self.file = open('rating.txt', 'r')
        for line in self.file:
            if line.split()[0] == pl_name:
                self.rating = int(line.split()[1])
        self.file.close()

    def new_rules(self):
        self.command = input()
        if ',' in self.command:
            self.new_options = self.command.split(',')
            self.options = self.new_options
        elif self.command == '':
            pass
        else:
            return

    def get_winner_list(self, command):
        self.winners_list = []
        try:
            for i in self.options:

                if (self.options.index(i) - self.options.index(command) > self.num) or (self.options.index(i) != self.options.index(command) and (
                        self.options.index(command) - self.options.index(i) <= self.num and self.options.index(i) < self.options.index(command))):
                    self.winners_list.append(i)
        except ValueError:
            print('Invalid input')

    def start_game(self):
        if self.pl_name is None:
            self.pl_name = input('Enter your name:')
            print('Hello,', self.pl_name)
            self.new_rules()
            print("Okay, let's start")

        while True:
            self.read_rating(self.pl_name)
            self.command = input()
            self.AI_answer = random.randrange(0, len(self.options))
            self.ai_word = self.options[self.AI_answer]

            self.num = int(len(self.options)) // 2
            self.get_winner_list(self.command)
            if self.command in self.options:
                if self.command == self.ai_word:
                    print(f'There is a draw ({self.command})')
                    self.rating += 50
                elif self.ai_word in self.winners_list:
                    self.win()
                elif self.ai_word not in self.winners_list:
                    self.lost()

            elif self.command == '!exit':
                print('Bye!')
                exit()
            elif self.command == '!rating':
                print('Your rating:', self.rating)



rps = RockPaperScissors()
rps.start_game()
