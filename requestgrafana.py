# -*- coding:utf-8 -*-
# author:f0ngf0ng

import requests

def read():
    a = []
    with open("grafana.txt", "r+") as f:
        for j in f.readlines():
            j = j.strip('\n')
            a.append(j)
    return a


if __name__ == '__main__':
    a = read()
    for url in a:
        try:
            requests.packages.urllib3.disable_warnings()
            a = requests.get( url , timeout=3)
            if a.status_code == 200:
                with open("finsh0602.txt","a+") as f:
                    f.writelines(url+'\n')

        except requests.exceptions.ConnectTimeout:
            # NETWORK_STATUS = False
            continue

        except requests.exceptions.Timeout:
            # REQUEST_TIMEOUT = True
            continue

        except requests.exceptions.ConnectionError:
            continue

        finally:
            print("OK")