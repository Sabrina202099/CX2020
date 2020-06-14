import re

def get_address(port):
    fr = open('exc.txt', 'r')
    while True:
        data = ''
        for line in fr:
            if line == '\n':
                break
            data += line
        if not data:
            break

        obj = re.match(port, data)
        if obj:
            # pattern = r"([0-9]{1,3}\.){3}[0-9]{1,3}/\d+|Unknow"
            pattern=r'(\d+\.){3}\d+/\d+|Unknown'
            address = re.search(pattern, data).group()
            return address

if __name__=="__main__":
    port=input("请输入端口号：")
    print(get_address(port))


