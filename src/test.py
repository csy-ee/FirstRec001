from FirstRec001.src.Config import Config

with open(Config.file_paths[0], 'r') as f:
    line = f.readlines()[0]
    print(line)
    print('end')
    print('end')