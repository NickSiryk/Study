'''
MODEL FILE

A simple prototype of a TV controller in Python
'''


class TVController:

    def __init__(self, loc):
        '''
        :param loc: list of channels
        '''
        self.loc = loc
        self.N = 0  # current channel position

    def first_channel(self):
        '''
        turns on the first channel from the list
        :return: current channel
        '''
        self.N = 0
        return self.current_channel()

    def last_channel(self):
        '''
        turns on the last channel from the list
        :return: current channel
        '''
        self.N = len(self.loc) - 1
        return self.current_channel()

    def turn_channel(self, n):
        '''
        turns on the N channel from the list
        :param n: number of chsnnel
        :return: current channel
        '''
        n -= 1  # correcting number for using as list marker
        if n >= len(self.loc):
            return self.first_channel()
        elif n < 0:
            return self.last_channel()
        else:
            self.N = n
            return self.current_channel()

    def next_channel(self):
        '''
        turns on the next channel
        '''
        return self.turn_channel(self.N + 2)

    def previous_channel(self):
        '''
        turns on the previous channel
        '''
        return self.turn_channel(self.N)

    def current_channel(self):
        '''
        :return: the name of the current channel.
        '''
        return self.loc[self.N]

    def is_exist(self, quest):
        '''
        :param quest: the number N or the string 'name'
        :return:
            "Yes", if the channel N or 'name' exists in the list
            "No" - in the other case
        '''
        quest = str(quest)
        if quest.isdigit():
            if 0 < int(quest) <= len(self.loc):
                return 'Yes'
            else:
                return 'No'
        else:
            if quest in self.loc:
                return 'Yes'
            else:
                return 'No'


CHANNELS = ["BBC", "Discovery", "TV1000", "CNN", "Euronews", "CNBC", "Reuters TV", "DW-TV", "SkyNews"]
controller = TVController(CHANNELS)