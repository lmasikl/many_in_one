# coding=utf-8
import subprocess
servers = {
    'Buenos': 'bn-ar.boxpnservers.com',
    'Sydney': 'sy-au.boxpnservers.com',
    'Montreal': 'mr-ca.boxpnservers.com',
    'Toronto': 'tr-ca.boxpnservers.com',
    'Vancouver': 'vn-ca.boxpnservers.com',
    'Paris': 'pr-fr.boxpnservers.com',
    'Frankfurt': 'ff-de.boxpnservers.com',
    'Reykjavik': 'ry-is.boxpnservers.com',
    'Milan': 'ml-it.boxpnservers.com',
    'Steinsel': 'st-lx.boxpnservers.com',
    'Amsterdam': 'am-nl.boxpnservers.com',
    'Panama': 'pn.boxpnservers.com',
    'Debica': 'db-pl.boxpnservers.com',
    'Moscow': 'ms-ru.boxpnservers.com',
    'Singapore': 'sg.boxpnservers.com',
    'Madrid': 'mr-es.boxpnservers.com',
    'Stockholm': 'se.boxpnservers.com',
    'Zurich': 'zr-ch.boxpnservers.com',
    'Istanbul': 'is-tr.boxpnservers.com',
    'Coventry': 'cv-uk.boxpnservers.com',
    'Hampshire': 'hs-uk.boxpnservers.com',
    'London': 'ln-uk.boxpnservers.com',
    'Maidenhead': 'md-uk.boxpnservers.com',
    'Manchester': 'mh-uk.boxpnservers.com',
    'Atlanta': 'al-us.boxpnservers.com',
    'Chicago': 'ch-us.boxpnservers.com',
    'Dallas': 'dl-us.boxpnservers.com',
    'A': 'la-us.boxpnservers.com',
    'B': 'lab-us.boxpnservers.com',
    'Miami': 'mi-us.boxpnservers.com',
    'York': 'ny-us.boxpnservers.com',
    'Jersey': 'nyb-us.boxpnservers.com',
    'Phoenix': 'ph-us.boxpnservers.com',
    'Jose': 'sj-us.boxpnservers.com',
    'St': 'sl-us.boxpnservers.com',
    'Washington': 'dc-us.boxpnservers.com',
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
    print('\n\r'.join(['{0}\t{1}'.format(i, s) for i, s in enumerate(sorted([(city, ping(server), server)for city, server in servers.items()], key=lambda p: -1 * p[1]))]))


find_best_server()