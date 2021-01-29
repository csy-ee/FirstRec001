import os
import math
from FirstRec001.src.fetch_user_info import FirstRec
from FirstRec001.src.Config import Config


def pearson(cls: FirstRec, x, y):
    """
    x: user1
    y: user2
    """
    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x2 = 0
    sum_y2 = 0
    n = 0
    for key, value in list(cls.trainset[x].items()):
        if key in list(cls.trainset[y].keys()):
            sum_x += int(value)
            sum_y += int(cls.trainset[y][key])
            sum_xy += int(value) * int(cls.trainset[y][key])
            n += 1
            sum_x2 += int(value) ** 2
            sum_y2 += int(cls.trainset[y][key]) ** 2

    if n == 0:
        return 0
    else:
        """
            sometimes the denominator of pearson function is Zero, this means the two user has no similarity
        """
        denominator = math.sqrt((sum_x2 - (sum_x ** 2) / n) * (sum_y2 - (sum_y ** 2) / n))
        if denominator == 0:
            return 0
        pearson_coef = (sum_xy - (sum_x * sum_y) / n) / denominator
        return pearson_coef


if __name__ == "__main__":
    firstrec = FirstRec(Config.file_paths, 42, 15, 20)
    print(pearson(firstrec, "2590061", "1569513"))
