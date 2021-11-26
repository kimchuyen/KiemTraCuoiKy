import sys
import re

re_apache_log = r"(?P<ip>.*?) (?P<remote_log_name>.*?) (?P<userid>.*?) \[(?P<date>.*?)(?= ) (?P<timezone>.*?)\] \"(" \
                r"?P<request_method>.*?) (?P<path>.*?)(?P<request_version> HTTP/.*)?\" (?P<status>.*?) (" \
                r"?P<length>.*?) \"(?P<referrer>.*?)\" \"(?P<user_agent>.*?)\""


def read_logs(filename):
    data = list()
    with open(filename, 'r') as file:
        # reading each line
        for line in file:
            m = re.search(re_apache_log, line)
            if m and 'path' in m.groupdict():
                path = m.groupdict()['path']
                if path.endswith('.jpg'):
                    full_path = f'https://{filename}{path}'
                    if full_path not in data:
                        data.append(full_path)
    return data


def main():
    if len(sys.argv) != 3:
        print('usage: ./main.py {--filename} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--filename':
        logs = read_logs(filename)
        print("\n".join(logs))
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
