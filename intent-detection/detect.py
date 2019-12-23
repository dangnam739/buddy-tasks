
class Gintent:
    def __init__(self, model):
        self.model = model
    
    def intent_of(self, sentence: str) -> str:
        """Return intention of a sentence"""
        return "<intent>"