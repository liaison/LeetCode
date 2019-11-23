"""
Design a logger system that receive stream of messages along with 
its timestamps, each message should be printed if and only if it 
is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true
if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

"""

class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._msg_dict = {}
    
    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if message not in self._msg_dict:
            self._msg_dict[message] = timestamp
            return True
        else:
            to_print= False
            old_timestamp = self._msg_dict[message]
            if timestamp - old_timestamp >= 10:
                to_print = True
                # update the timestamp
                self._msg_dict[message] = timestamp

            return to_print
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)