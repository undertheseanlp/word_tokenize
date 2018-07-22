from src.train.train import CRFWrapper


def train_model():
    CRFWrapper('tmp/cleaned/').execute()
