class WrittenText: 
    def __init__(self, text):
        self._text = text
  
    def render(self):
        return self._text
  
class UnderlineWrapper(WrittenText):
    def __init__(self, wrapped):
        self._wrapped = wrapped
  
    def render(self):
        return "<u>{}</u>".format(self._wrapped.render())
  
class ItalicWrapper(WrittenText):
    def __init__(self, wrapped):
        self._wrapped = wrapped
  
    def render(self):
        return "<i>{}</i>".format(self._wrapped.render())
  
class BoldWrapper(WrittenText):  
    def __init__(self, wrapped):
        self._wrapped = wrapped
  
    def render(self):
        return "<b>{}</b>".format(self._wrapped.render())
  
  
if __name__ == '__main__':
  
    before_c = WrittenText("coding")
    after_c = ItalicWrapper(UnderlineWrapper(BoldWrapper(before_c)))
  
    print("before :", before_c.render())
    print("after :", after_c.render())