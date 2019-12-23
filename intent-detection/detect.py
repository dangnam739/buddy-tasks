
class Gintent:
    def __init__(self, model):
        self.model = model
    
    def intent_of(self, sentence):
        pred = self.model.predict(sentences)
        return pred[0][0]
