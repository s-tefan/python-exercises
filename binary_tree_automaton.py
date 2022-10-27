

class BinaryTreeAutomaton:
    def __init__(self, godict = {}, restart = None):
        self.godict = godict

    def do(self):
        input = self.get_input()
        try:
            go = self.godict[input]
        except:
            raise Exception("Før Søren!")
        if type(go) == type(self):
            go.do()
        else:
            self.output(go)
            self.restart.do()

    def output(self, mess):
        print(mess)
