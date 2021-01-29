import os
import json
import random
import math
# import FirstRec001.src.Config as Config
from FirstRec001.src.Config import Config
import tqdm as tqdm


class FirstRec(object):
    """
    file_paths: list of file_path of trainset
    seed: 
    k:  k value of kneighbour
    n_items: num of movies recommanded to users
    """

    def __init__(self, file_paths, seed, k, n_items):
        self.file_paths = file_paths
        self.users_1000 = self.__select_1000_users()
        self.seed = seed
        self.k = k
        self.n_items = n_items
        self.trainset, self.validset = self._load_and_split_data()

    def __select_1000_users(self):
        if os.path.exists(Config.trainset_json) and os.path.exists(Config.validset_json):
            return list()
        else:
            users = set()
            for file_path in self.file_paths:
                with open(file_path, 'r') as f:
                    for line in tqdm.tqdm(f.readlines(), desc="loading {}".format(file_path)):
                        if len(line.strip().split(',')) == 3:
                            user_id, _, _ = line.split(',')
                            users.add(user_id)

            users_1000 = random.sample(list(users), 1000)
            return users_1000

    def _load_and_split_data(self):
        trainset = dict()
        validset = dict()

        if os.path.exists(Config.trainset_json) and os.path.exists(Config.validset_json):
            print("trainset and validset have already been generated!")
            trainset = json.load(open(Config.trainset_json))
            validset = json.load(open(Config.validset_json))
            return trainset, validset

        now_movie_id = -1
        user_id = None
        rate = None
        data = None
        for file_path in self.file_paths:
            with open(file_path, 'r') as f:
                for line in tqdm.tqdm(f.readlines()):
                    if len(line.strip().split(',')) == 1:
                        now_movie_id = int(line.strip()[0:-1])
                    else:
                        user_id, rate, data = line.strip().split(',')

                    if user_id in self.users_1000:
                        if random.randint(1, 50) == 1:
                            validset.setdefault(user_id, {})[now_movie_id] = rate
                        else:
                            trainset.setdefault(user_id, {})[now_movie_id] = rate

        json.dump(trainset, open(Config.trainset_json, 'w'))
        json.dump(validset, open(Config.validset_json, 'w'))
        print("trainset and validset are generated: /n {} /n {}".
              format(Config.trainset_json, Config.validset_json))

        return trainset, validset


if __name__ == "__main__":
    firstrec = FirstRec(Config.file_paths, 42, 15, 20)
