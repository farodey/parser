import re


def print_line(filename):
    with open(filename, 'r') as file:
        with open('log.csv', 'w') as csvfile:
            for line in file:
                csvfile.write(line[0:15] + ';')
                csvfile.write(line[16:31] + ';')
                csvfile.write(line[32:63] + ';')
                csvfile.write(line[64:90] + ';')

                # IP
                csvfile.write(re.search(r'\+0400 (.*?) - ', line).group(1) + ';')

                # Тип запроса
                try:
                    csvfile.write(re.search(r' - (.*?) /', line).group(1) + ';')
                except Exception:
                    csvfile.write('none;')

                # ссылка
                try:
                    csvfile.write(re.search(r'(GET|POST|HEAD) (.*?) HTTP', line).group(2) + ';')
                except Exception:
                    csvfile.write('none;')

                # код ответа
                try:
                    csvfile.write(re.search(r'"(\d\d\d)"', line).group(1) + ';')
                except Exception:
                    csvfile.write('none;')

                csvfile.write('\n')


def main():
    print_line('log')


if __name__ == '__main__':
    main()
