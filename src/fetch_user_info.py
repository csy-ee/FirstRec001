import os 
import json 
import random 
import math 


class FirstRec:
    """
    file_paths: list of file_path of trainset
    seed: 
    k:  k value of kneighbour
    n_items:
    """
    def __init__(self, file_paths, seed, k, n_items):
        self.file_paths = file_paths 
        self.users_1000 = self.__select_1000_users()
        self.seed = seed 
        self.k = k
        self.n_items = n_items 
        self.train, self.test = self._load_and_split_data()


    def __select_1000_users(self):
        if os.path.exists("data/train.json") and os.path.exists("data/train.json"):
            return list()
        else:
            users = set()
            for file_path in self.file_paths:
                with open(file_path, 'r') as f:
                    for line in f.readlines()[1:]:
                        if len(line.split(','))==3:
                            user_id, _, _ = line.split(',')
                            users.add(user_id)
            
            users_1000 = random.sample(list(user_id), 1000)
            return users_1000

    def _load_and_split_data(self):
        trainset = dict()
        validset = dict()
        
        now_movie_id = -1
        for file_path in file_paths:
            with open(file_path, 'r') as f:
                for line in f.readlines():
                    if len(line.strip().split(','))==1:
                        now_movie_id = int(line[0:-2])
