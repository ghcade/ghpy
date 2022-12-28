import sys
import getopt


def check_input(argv):
    check_list = ['http://', 'https://']
    error_flag = 0
    file_type = 'xlsx'
    try:
        opts, args = getopt.getopt(argv, "h:u:t:", ["url=", "type="])
        # print(opts)
        # print(args)
    except getopt.GetoptError:
        print('Use : ghpy.py -u <target url> [-t <file type>]')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Use : ghpy.py -u <target url> [-t <file type>]')
            print('-u, --url : Scan target url.')
            print('-t, --type : output file type, default xlsx. Optional csv, xlsx')
            print('EX: ghpy.py -u example.com')
            print('EX: ghpy.py -u example.com -t xlsx')
            sys.exit()
        elif opt in ("-u", "--url"):
            url = arg
            # 如果目標加上http(s)將url移除http(s)
            for check_url in check_list:
                if url.find(check_url) != -1:
                    url = url.split(check_url)[1]
                    break
            if url == '-t' or url == '--type':
                print('Url cannot be empty!')
                error_flag += 1
        elif opt in ("-t", "--type"):
            file_type = arg
            if file_type == 'csv':
                pass
            elif file_type == 'xlsx':
                pass
            else:
                print('File type not supput! Supput type: csv, xlsx')
                error_flag += 1

    if error_flag == 0:
        return url, file_type


'''
if __name__ == "__main__":
    try:
        target_url, file_type = check_input(sys.argv[1:5])
        print(target_url, file_type)
    except:
        print('Use : ghpd.py -u <target url> [-t <file type>]')
'''
