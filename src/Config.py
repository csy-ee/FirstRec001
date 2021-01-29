import sys
import os


class Config:
    """
    configuration params of this project
    """
    trainset_json = os.path.join(os.getcwd(), '..', 'data', 'trainset.json')
    validset_json = os.path.join(os.getcwd(), '..', 'data', 'validset.json')
    file_paths = [
        os.path.join(r'D:\Projects\Recommandation\datasets\Netflix', "combined_data_{}.txt".format(x))
        for x in range(1, 5)
    ]