from random import randint
HEADERS_LIST = ['date', 'resource', 'staff_id', 'count']
NUMBER_OF_COLUMNS = 4
N = 100


class GenerateDataByColumns:

    def generate_date(self):
        self.is_not_used()
        return '{}-{}'.format(randint(2020, 2021), randint(1, 12))

    def generate_resource(self):
        self.is_not_used()
        return '{}'.format(randint(118, 142))

    def generate_staff_id(self):
        self.is_not_used()
        return '{}'.format(randint(1, 42))

    def generate_count(self):
        self.is_not_used()
        return '{}'.format(randint(0, 100))

    def is_not_used(self):
        pass

    def __str__(self):
        return '{},{},{},{}'.format(self.generate_date(), self.generate_resource(),
                                    self.generate_staff_id(), self.generate_count())


def main():
    headers = ''
    for i in range(NUMBER_OF_COLUMNS):
        headers += HEADERS_LIST[i]
    data = headers + '\n'
    for _ in range(N):
        data_row = str(GenerateDataByColumns()) + '\n'
        data += data_row

    f = open('input.txt', 'w')
    f.write(data)
    f.close()


if __name__ == '__main__':
    main()
