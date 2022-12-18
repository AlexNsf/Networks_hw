import subprocess
import platform
import re


class MTUScript:
    ICMP_IP_HEADERS = 28

    def __init__(self, host_name):
        self.host_name = host_name
        self.is_win = platform.system() == 'Windows'

    def ping(self, packet_size=1):
        if self.is_win:
            cmd = f'ping {self.host_name} -f -l {packet_size}'
        else:
            cmd = f'ping -M do -c 1 -s {packet_size} {self.host_name}'
        proc = subprocess.run(cmd, capture_output=True, shell=True, encoding='utf8')
        if proc.returncode != 0:
            return False
        res = proc.stdout + proc.stderr
        print(res)
        for err_msg in ['message too long', '100.0% packet loss', 'packet size too large']:
            if err_msg in res:
                return False
        return True

    def find_mtu(self):
        left, right = 0, 10000
        while left + 1 < right:
            mid = (left + right) // 2
            if self.ping(mid):
                left = mid
            else:
                right = mid
        return left + self.ICMP_IP_HEADERS


if __name__ == '__main__':
    valid_ip = '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
    valid_host = '^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$'
    try:
        host = input('Enter host name: ')
        while not (re.match(valid_ip, host) or re.match(valid_host, host)):
            print('Host name might be not valid. Process with given host name?')
            ans = input('[y/n]')
            if ans == 'y':
                break
            else:
                host = input('Enter host name: ')
        script = MTUScript(host)

        if not script.ping(1):
            print('Icmp is not available or host is not responding')
        else:
            print('MTU:', script.find_mtu())
    except Exception as e:
        print(f"Error occurred: {e}")
