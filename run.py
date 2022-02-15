import enchant
import argparse
import string


class BruteForceWordleSolver:
    alphabet = set(string.ascii_lowercase)
    d = enchant.Dict('en_US')

    def __init__(self, args):
        self.grays = {} if args.grays is None else set(args.grays)
        self.yellows = self.dictionarize(args.yellows)
        self.greens = self.dictionarize(args.greens)
        self.yellows_list = set(self.yellows.values()).difference('?')
        print('\nGreens :', self.greens)
        print('Yellows:', self.yellows)
        print('Grays  :', self.grays)
        print('\nValid wordles:')

    def dictionarize(self, pair):
        d = dict()
        for i in range(1, 6):
            d[i] = '?'
        if pair is not None:
            for row in pair:
                d[int(row[1])] = row[0]
        return d

    def valid_ith_alphabet(self, i):
        # valid_ith_alphabet = lambda i: alphabet.difference(self.grays).difference(set(self.yellows[i])) if self.greens[i] == '?' else self.greens[i]
        if self.greens[i] == '?':
            return self.alphabet.difference(self.grays).difference(set(self.yellows[i]))
        else:
            return self.greens[i]

    def run(self):
        for _1 in self.valid_ith_alphabet(1):
            for _2 in self.valid_ith_alphabet(2):
                for _3 in self.valid_ith_alphabet(3):
                    for _4 in self.valid_ith_alphabet(4):
                        for _5 in self.valid_ith_alphabet(5):
                            word = f'{_1}{_2}{_3}{_4}{_5}'
                            if self.d.check(word) and all(x in word for x in self.yellows_list):
                                print(word)


if __name__ == '__main__':
    pair = lambda x: x.split(',')
    parser = argparse.ArgumentParser('Brute Force Wordle Answer Generation Program')
    parser.add_argument('--yellows', type=pair, nargs='+', help='list {alphabet, index} pairs eg) a,2 b,3')
    parser.add_argument('--greens', type=pair, nargs='+', help='list {alphabet, index} pairs eg) c,4 d,5')
    parser.add_argument('--grays', type=str, nargs='+', help='list alphabet eg) q w e')

    args = parser.parse_args()
    BruteForceWordleSolver(args).run()
