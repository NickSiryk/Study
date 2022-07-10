'''
Controller FILE

A simple prototype of a TV controller in Python
'''

import pult_M as p_M

class Controller:
    def __init__(self, view):
        '''
        :param view: view class object
        '''

        # connecting to the model class object
        self.model = p_M.controller

        # connecting to the viev class object
        self.view = view

        # Work marker
        self.ON = False

    def start(self):
        '''
        start/stop button control
        '''
        if not self.ON:
            self.ON = True
            # updating view with start parameters
            self.view.update(self.model.current_channel(), self.model.N+1)
        else:
            self.view.stop()

    
    def set(self, nomer):
        '''
        A channel set method

        :param nomer: channel number
        '''
        if not self.ON:
            self.start()

        # set channel if exist
        if self.model.is_exist(nomer) == 'Yes':
            self.view.update(self.model.turn_channel(nomer), self.model.N+1)



    def next(self):
        '''
        "Turn next channel" method
        Turns TV on, if off
        '''
        if self.ON:
            self.view.update(self.model.next_channel(), self.model.N + 1)
        else:
            self.start()
    
    def prev(self):
        '''
        "Turn previous channel" method
        Turns TV on, if off
        '''
        if self.ON:
            self.view.update(self.model.previous_channel(), self.model.N + 1)
        else:
            self.start()
    
    def find(self, chan):
        '''
        Method for checking the existence of a channel
        turns channel on if exist
        Turns TV on, if off
        '''
        chan = str(chan)
        if not self.ON:
            self.start()
        try:
            chan = int(chan)
            if self.model.is_exist(chan) == 'Yes':
                self.view.update(self.model.turn_channel(chan), self.model.N+1)
            else:
                self.view.msg('No such channel!')
        except ValueError:
            if self.model.is_exist(chan) == 'Yes':
                self.view.update(self.model.turn_channel(self.model.chan.index(chan)+1), self.model.N + 1)
            else:
                self.view.msg('No such channel!')