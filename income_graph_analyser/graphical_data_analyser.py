from datetime import datetime
import matplotlib as plt
import sys


def open_file(file_name='input.txt'):
    f = open(file_name)
    data = f.readlines()
    f.close()
    return data


def create_list_of_dicts(data):
    headers = data.pop(0).strip(' ').strip('\n').split(',')
    data_str_dic = []
    for data_row in data:
        data_str_dic.append(dict(zip(headers, data_row.split(','))))
    return data_str_dic


def filter_data(data, key, value):
    return list(filter(lambda elem: elem[key] == value, data))


def sort_data(data, sort_key):
    return sorted(data, key=lambda k: datetime.strptime(k[sort_key], '%Y-%M'))


def prepare_data(data, data_filter=None):
    if data_filter is not None:
        for one_data_filter in data_filter.split(','):
            key = one_data_filter.split('=')[0]
            value = one_data_filter.split('=')[1]
            data = filter_data(data, key, value)
    return data


def make_plot(data, ordinate_key, abscissa_key='date', data_filter=''):
    ordinate = []
    abscissa = []
    for data_row in data:
        ordinate.append(data_row[ordinate_key])
        abscissa.append(data_row[abscissa_key])
    if abscissa_key == 'date':
        abscissa = list(map(lambda x: str(x)[0:7], abscissa))

    plt.title('{}({})'.format(ordinate_key, abscissa_key))
    plt.xlabel(abscissa_key)
    plt.ylabel(ordinate_key)
    plt.plot(abscissa, ordinate)
    plt.savefig('plot {}({}): {}.png'.format(ordinate_key, abscissa_key, data_filter))
    plt.show()


def main(file_name):
    data_str = open_file(file_name)
    data = create_list_of_dicts(data_str)
    data = prepare_data(data, sys.argv[4])
    make_plot(data, sys.argv[2], sys.argv[3])


# To run program you should write '....txt' 'ordinate_key' 'abscissa_key' 'data_filter'
# Format of data_filter is key1=value1,key2=value2,...
if __name__ == '__main__':
    main(sys.argv[1])
