# coding=utf-8
import subprocess
servers = {
    'Moscow': 'ya.ru',
    'San-Francisco': 'google.com',
}



def get_stats_from_ping_data(stats):
    """
    >>> get_stats_from_ping_data(['1', 'd', '2'])
    [2.0, 1.0]
    """
    out = []
    for i, x in enumerate(reversed(stats[:])):
        data = x.split('/')
        for d in data:
            try:
                out.append(float(d))
            except ValueError:
                continue

    return out


def ping(website="google.com"):
    """
    >>> a = ping()
    >>> type(a) == float
    True
    """
    try:
        packets_count = 5
        _ping = subprocess.Popen(
            ["ping", "-n", "-c 5", website],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        out, error = _ping.communicate()
        if out:
            statistics = get_stats_from_ping_data(
                out[out.index('statistics ---'):].split(' ')
            )

            try:
                resived_packets = statistics.pop()
                minimum = statistics.pop()
                average = statistics.pop()
                maximum = statistics.pop()
                stddev = statistics.pop()
                percent = (resived_packets / packets_count) * 100
                return average
            except IndexError:
                return 10 ** 5
                # print "no data for one of minimum,maximum,average,packet"
        else:
            return 10 ** 5
            # print 'No ping'

    except subprocess.CalledProcessError:
        return 10 ** 5
        # print "Couldn't get a ping"


def find_best_server():
    pings = [(city, ping(server)) for city, server in servers.items()]
    print(sorted(pings, key=lambda p: p[1]))


find_best_server()