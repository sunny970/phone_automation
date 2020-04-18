import yaml

def yml_read(data_file_name,key):
    with open("./test_data/"+ data_file_name +".yml","r", encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)[key]
        case_data_list = list()
        for case_data in data.values():
            case_data_list.append(case_data)
        return case_data_list
