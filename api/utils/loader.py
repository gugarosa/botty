import spacy


def load_spacy():
    """Pre-loads a model from Spacy.
    
    """

    # Loads the model
    model = spacy.load('pt_core_news_sm')

    return model
