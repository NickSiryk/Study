class TVController:
    '''
    A simple prototype of a TV controller in Python
    '''

    def __init__(self, loc):
        '''
        :param loc: list of channels
        '''
        self.loc = loc
        self.n = 0

    def first_channel(self):
        '''
        turns on the first channel from the list
        :return: current channel
        '''
        self.n = 0
        return self.current_channel()

    def last_channel(self):
        '''
        turns on the last channel from the list
        :return: current channel
        '''
        self.n = len(self.loc) - 1
        return self.current_channel()

    def turn_channel(self, n):
        '''
        turns on the N channel from the list
        :param n: number of chsnnel
        :return: current channel
        '''
        if n >= len(self.loc):
            return self.first_channel()
        elif n <= 0:
            return self.last_channel()
        else:
            self.n = n - 1
            return self.current_channel()

    def next_channel(self):
        '''
        turns on the next channel
        '''
        return self.turn_channel(self.n + 2)

    def previous_channel(self):
        '''
        turns on the previouns channel
        '''
        return self.turn_channel(self.n)

    def current_channel(self):
        '''
        :return: the name of the current channel.
        '''
        return self.loc[self.n]

    def is_exist(self, quest):
        '''
        :param quest: the number N or the string 'name'
        :return:
            "Yes", if the channel N or 'name' exists in the list
            "No" - in the other case
        '''
        quest = str(quest)
        if quest.isdigit():
            if 1 < int(quest) < len(self.loc):
                return 'Yes'
            else:
                return 'No'
        else:
            if quest in self.loc:
                return 'Yes'
            else:
                return 'No'


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)


print(controller.first_channel() == "BBC")
print(controller.last_channel() == "TV1000")
print(controller.turn_channel(1) == "BBC")
print(controller.next_channel() == "Discovery")
print(controller.previous_channel() == "BBC")
print(controller.current_channel() == "BBC")
print(controller.is_exist(4) == "No")
print(controller.is_exist("BBC") == "Yes")