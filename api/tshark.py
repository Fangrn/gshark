#!/usr/bin/env python3

def make_filter(display_filter):
    filter_list = []
    # Network
    if display_filter.get('network'):
        if display_filter['network'] == 'icmp':
            filter_list.append('icmp')
        elif display_filter['network'] == 'ipv4':
            filter_list.append('ip')
        elif display_filter['network'] == 'ipv6':
            filter_list.append('ipv6')
    # Src IP
    if display_filter.get('src_ip'):
        filter_list.append('ip.src == %s' % display_filter['src_ip'])
    # Dst IP
    if display_filter.get('dst_ip'):
        filter_list.append('ip.dst == %s' % display_filter['dst_ip'])

    # Src port
    if display_filter.get('src_port'):
        filter_list.append('(tcp.srcport == {port} or udp.srcport == {port})' \
            .format(port=display_filter['src_port']))
    # Dst port
    if display_filter.get('dst_port'):
        filter_list.append('(tcp.dstport == {port} or udp.dstport == {port})' \
            .format(port=display_filter['dst_port']))

    # Transport
    if display_filter.get('transport'):
        filter_list.append(display_filter['transport'].lower())
    # Application
    if display_filter.get('application'):
        filter_list.append(display_filter['application'].lower())

    # Period Start
    if display_filter.get('period_start'):
        filter_list.append('frame.time_epoch >= %s' % display_filter['period_start'])
    # Period End
    if display_filter.get('period_end'):
        filter_list.append('frame.time_epoch <= %s' % display_filter['period_end'])

    filter = ' and '.join(filter_list)

    return filter
