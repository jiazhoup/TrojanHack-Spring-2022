
class Node:
    def __init__(self, name):
        self.children = []
        self.acceptedRegexs = []
        self.parent = None
        self.name = name

    """
    childNode: an instance of the Node object
    """
    def addChild(self, childNode):
        childNode.parent = self
        self.children.append(childNode)

    """
    regex: A string in the form of a regex expression
    """
    def add_regex(self, regex):
        self.acceptedRegexs.append(regex)

    def getChildren(self):
        return self.children

    def getParent(self):
        return self.parent

    def getName(self):
        return self.name

    def getAcceptedRegexs(self):
        return self.acceptedRegexs
    

