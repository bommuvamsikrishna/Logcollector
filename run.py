
def get_error_logs_from_pods():
    fpod = open('readfile.txt', "r")
    lines = fpod.readlines()
    for i in range(1, len(lines)):
        if lines[i].__contains__('terminated'):
            with open('terminated', 'a') as f:
                f.write(lines[i])

if __name__ == '__main__':
    get_error_logs_from_pods()


