import yaml

def yml_read(file_name):
    with open("./data/"+ file_name +".yml","r", encoding='utf-8') as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        return data
if __name__ == '__main__':
    yml_read("search_data")