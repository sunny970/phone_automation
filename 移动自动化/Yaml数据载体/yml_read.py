import yaml


def main():

    # 读取
    with open("./data.yml","r",encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        print(data)


    # 写入
    # data = {'search': {'search_a':"[4,5,6]"}}
    # with open("./test.yml","w") as f:
    #     yaml.dump(data,f,encoding='utf-8',allow_unicode=True)

if __name__ == '__main__':
    main()

