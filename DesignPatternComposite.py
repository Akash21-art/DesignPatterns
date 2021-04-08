class LeafElement:  
    def __init__(self, *args):
        self.position = args[0]
  
    def showDetails(self):
        print("\t", end ="")
        print(self.position)
  
  
class CompositeElement:
  
    def __init__(self, *args):
        self.position = args[0]
        self.children = []
  
    def add(self, child):
        self.children.append(child)
  
    def remove(self, child):
        self.children.remove(child)
  
    def showDetails(self):
        print(self.position)
        for child in self.children:
            print("\t", end ="")
            child.showDetails()
  
  

if __name__ == "__main__":
  
    topLevelMenu = CompositeElement("CEO")
    subMenuItem1 = CompositeElement("CTO")
    subMenuItem2 = CompositeElement("Manager")
    subMenuItem11 = LeafElement("Developer1")
    subMenuItem12 = LeafElement("Developer2")
    subMenuItem21 = LeafElement("Developer3")
    subMenuItem22 = LeafElement("Developer4")
    subMenuItem1.add(subMenuItem11)
    subMenuItem1.add(subMenuItem12)
    subMenuItem2.add(subMenuItem22)
    subMenuItem2.add(subMenuItem22)
  
    topLevelMenu.add(subMenuItem1)
    topLevelMenu.add(subMenuItem2)
    topLevelMenu.showDetails()