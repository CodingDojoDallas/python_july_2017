class Call(object):
    def __init__(self, id, caller, phone_number, time, reason):
        self.id = id
        self.caller = caller
        self.phone_number = phone_number
        self.time = time
        self.reason = reason

    def display(self):
        print "ID: {} CALLER NAME: {} CALLER PHONE NUMBER: {} TIME OF CALL: {} REASON FOR CALL: {}".format(
            self.id + "\n",
            self.caller + "\n",
            self.phone_number + "\n",
            self.time + "\n",
            self.reason
        )

firstcall = Call("1", "lillian", "2152645675", "10:03am", "asking a question")
firstcall.display()

secondcall = Call("2", "michael", "4435556666", "1:43pm", "asking a question")
secondcall.display()

thirdcall = Call("3", "fraz", "9879990656", "4:39pm", "asking a question")
thirdcall.display()

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = len(self.calls)

    def addCall(self, call):
        self.calls.append(call)
        return self

    def removeCall(self):
        self.calls.pop(0)
        return self

    def info(self):
        for call in self.calls:
            print "Name: {} Phone Number: {}".format(
            call.caller,
            call.phone_number,
            )

    def queuelength(self):
        print len(self.calls)
        return self


newcall = CallCenter()

newcall.addCall(firstcall).addCall(secondcall).queuelength().removeCall().queuelength()
