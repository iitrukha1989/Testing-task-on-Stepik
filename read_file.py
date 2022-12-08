# Тестовые/экзаменационные задачи по работе с файлами из курса Python на платформе Stepik
# Файлы с данными по условию находяться в той же репозитории что и скрипт
# Разработчик: Ilya Trukhanovich


def exam_file_1(file_name):
    res_value = ''
    with open('forbidden_words.txt', 'rt', encoding='utf-8') as forb_file, open(file_name, 'rt', encoding='utf-8') as parse_file:
        forb_list = forb_file.read().split()
        for parse_value in parse_file:
            res_option = parse_value
            for forb_value in forb_list:
                if forb_value in parse_value.lower():
                    for _ in range(parse_value.lower().count(forb_value)):
                        res_option = res_option.replace(res_option[res_option.lower().find(
                            forb_value):res_option.lower().find(forb_value) + len(forb_value)], '*' * len(forb_value))
            res_value += res_option
    return res_value


def exam_file_2():
    dict_value = {'а':	'a', 'к': 'k',	'х': 'h',
                  'б':	'b',	'л':	'l',	'ц':	'c',
                  'в':	'v',	'м':	'm',	'ч':	'ch',
                  'г':	'g',	'н':	'n',	'ш':	'sh',
                  'д':	'd',	'о':	'o',	'щ':	'shh',
                  'е':	'e',	'п':	'p',	'ъ':	'*',
                  'ё':	'jo',	'р':	'r',	'ы':	'y',
                  'ж':	'zh',	'с':	's',	'ь':	"'",
                  'з':	'z',	'т':	't',	'э':	'je',
                  'и':	'i',	'у':	'u',	'ю':	'ju',
                  'й':	'j',	'ф':	'f',	'я':	'ya',
                  }
    with open('cyrillic.txt', 'rt', encoding='utf-8') as input_file, open('transliteration.txt', 'wt', encoding='utf-8') as output_file:
        for row_value in input_file:
            for tmp_value in row_value:
                if tmp_value.lower() in dict_value:
                    if tmp_value.islower():
                        output_file.write(dict_value[tmp_value.lower()])
                    if tmp_value.isupper():
                        output_file.write(
                            dict_value[tmp_value.lower()].title())
                else:
                    output_file.write(tmp_value)


def main():
    print(*exam_file_1('data.txt'), sep='\n')
    print(*exam_file_1('stepik.txt'), sep='\n')
    print(*exam_file_1('beegreek.txt'), sep='\n')
    print(*exam_file_2(), sep='\n')


if __name__ == '__main__':
    main()
