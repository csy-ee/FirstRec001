import sys
import os


class Config:
    """
    configuration params of this project
    """
    trainset_json = os.path.join(os.getcwd(), '..', 'data', 'trainset.json')
    validset_json = os.path.join(os.getcwd(), '..', 'data', 'validset.json')
