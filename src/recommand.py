from FirstRec001.src.Config import Config
from FirstRec001.src.fetch_user_info import FirstRec
from FirstRec001.src.pearson import pearson


def recommand(self: FirstRec, user_id):
    neighbour_user = dict()
    for user in self.trainset.keys():
        if user != user_id:
            distance = pearson(self, user_id, user)
            neighbour_user[user] = distance
    nearest_neigh = sorted(neighbour_user.items(), key=lambda k: k[1], reverse=True)

    movie = dict()
    for sim_user, sim in nearest_neigh[:self.k]:
        for mov in self.trainset[sim_user].keys():
            movie.setdefault(mov, 0)
            movie[mov] += sim * int(self.trainset[sim_user][mov])
    rec_movies = sorted(movie.items(), key=lambda k: k[1], reverse=True)

    return rec_movies[:self.n_items]


if __name__ == "__main__":
    firstrec = FirstRec(Config.file_paths, 42, 15, 20)
    print(recommand(firstrec, "2590061"))