#! /usr/bin/python3

banner = r'''
#EXTINF:-1 group-title="Entertainment" tvg-logo="https://www.indiantvinfo.com/media/2022/10/Sony-Entertainment-Television-HD-New-Logo.png",SET HD
https://pubads.g.doubleclick.net/ssai/event/HgaB-u6rSpGx3mo4Xu3sLw/master.m3u8

#EXTINF:-1 group-title="Entertainment" tvg-logo="https://www.indiantvinfo.com/media/2022/10/Sony-SAB-HD-New-Logo.png",SONY SAB HD
https://pubads.g.doubleclick.net/ssai/event/UI4QFJ_uRk6aLxIcADqa_A/master.m3u8

#EXTINF:-1 group-title="Entertainment" tvg-logo="https://www.indiantvinfo.com/media/2022/10/Sony-PAL-New-Logo.png",SONY PAL
https://pubads.g.doubleclick.net/ssai/event/rPzF28qORbKZkhci_04fdQ/master.m3u8

#EXTINF:-1 group-title="Entertainment" tvg-logo="https://www.indiantvinfo.com/media/2022/10/Sony-WAH-New-Logo.png",SONY WAH
https://pubads.g.doubleclick.net/ssai/event/H_ZvXWqHRGKpHcdDE5RcDA/master.m3u8

#EXTINF:-1 tvg-logo="https://jiotv.catchup.cdn.jio.com/dare_images/images/Colors_HD.png" group-title="Entertainment",Colors HD
https://prod-sports-north-gm.jiocinema.com/bpk-tv/Colors_HD_voot_MOB/Fallback/index.m3u8

#EXTINF:-1 tvg-logo="https://jiotv.catchup.cdn.jio.com/dare_images/images/Rishtey.png" group-title="Entertainment",Colors Rishtey
https://prod-sports-north-gm.jiocinema.com/bpk-tv/Colors_Rishtey_voot_MOB/Fallback/index.m3u8

#EXTINF:-1 group-title="Movies" tvg-logo="https://www.indiantvinfo.com/media/2022/10/Sony-MAX-HD-New-Logo.png",SONY MAX HD
https://pubads.g.doubleclick.net/ssai/event/Qyqz40bSQriqSuAC7R8_Fw/master.m3u8

#EXTINF:-1 group-title="Movies" tvg-logo="https://www.indiantvinfo.com/media/2022/10/Sony-MAX2-New-Logo.png",SONY MAX 2
https://pubads.g.doubleclick.net/ssai/event/4Jcu195QTpCNBXGnpw2I6g/master.m3u8

#EXTINF:-1 tvg-logo="https://jiotv.catchup.cdn.jio.com/dare_images/images/Color_Cineplex_HD.png" group-title="Movies",Colors Cineplex HD
https://prod-sports-north-gm.jiocinema.com/bpk-tv/Colors_Cineplex_voot_MOB/Fallback/index.m3u8

#EXTINF:-1 tvg-logo="https://jiotv.catchup.cdn.jio.com/dare_images/images/Colors_Cineplex_Bollywood.png" group-title="Movies",Colors Cineplex Bollywood
https://prod-sports-north-gm.jiocinema.com/bpk-tv/Colors_Cineplex_Bollywood_voot_MOB/Fallback/index.m3u8

#EXTINF:-1 group-title="Movies" tvg-logo="https://www.indiantvinfo.com/media/2022/10/Sony-PIX-HD-New-Logo.png",SONY PIX HD
https://pubads.g.doubleclick.net/ssai/event/8FR5Q-WfRWCkbMq_GxZ77w/master.m3u8

#EXTINF:-1 tvg-logo="https://jiotv.catchup.cdn.jio.com/dare_images/images/Colors_Infinity_HD.png" group-title="Entertainment",Colors Infinity HD
https://prod-sports-north-gm.jiocinema.com/bpk-tv/Colors_Infinity_HD_voot_MOB/Fallback/index.m3u8

#EXTINF:-1 tvg-logo="https://jiotv.catchup.cdn.jio.com/dare_images/images/Comedy_Central_HD.png" group-title="Entertainment",Comedy Central HD
https://prod-sports-north-gm.jiocinema.com/bpk-tv/Comedy_Central_HD_voot_MOB/Fallback/index.m3u8

#EXTINF:-1 group-title="Kids" tvg-logo="https://www.indiantvinfo.com/media/2022/10/Sony-YAY-New-Logo.png",SONY YAY!
https://pubads.g.doubleclick.net/ssai/event/40H5HfwWTZadFGYkBTqagg/master.m3u8

#EXTINF:-1 tvg-logo="https://jiotv.catchup.cdn.jio.com/dare_images/images/Sonic_Nickelodeon.png" group-title="Kids",Sonic Nickelodeon
https://prod-sports-north-gm.jiocinema.com/bpk-tv/Sonic_Nickelodeon_voot_MOB/Fallback/index.m3u8

#EXTINF:-1 tvg-logo="https://jiotv.catchup.cdn.jio.com/dare_images/images/Nick_Junior.png" group-title="Kids",Nick Jr
https://prod-sports-north-gm.jiocinema.com/bpk-tv/Nick_Junior_voot_MOB/Fallback/index.m3u8

#EXTINF:-1 tvg-logo="https://logodix.com/logo/900709.png" group-title="Kids",Nick HD+
https://prod-sports-north-gm.jiocinema.com/bpk-tv/Nick_HD_Plus_voot_MOB/Fallback/index.m3u8

#EXTINF:-1 tvg-logo="https://jiotv.catchup.cdn.jio.com/dare_images/images/Sports18_1_HD.png" group-title="Sports",Sports18 1 HD
https://prod-sports-north-gm.jiocinema.com/bpk-tv/Sports18_1_HD_voot_MOB/Fallback/index.m3u8

#EXTINF:-1 group-title="Sports" tvg-logo="https://www.indiantvinfo.com/media/2022/10/Sony-Sports-Ten1-HD-New-Logo.png",SONY SPORTS TEN 1 HD
https://pubads.g.doubleclick.net:443/ssai/event/yeYP86THQ4yl7US8Zx5eug/master.m3u8

#EXTINF:-1 group-title="Sports" tvg-logo="https://www.indiantvinfo.com/media/2022/10/Sony-Sports-Ten2-HD-New-Logo.png",SONY SPORTS TEN 2 HD
https://pubads.g.doubleclick.net:443/ssai/event/Syu8F41-R1y_JmQ7x0oNxQ/master.m3u8

#EXTINF:-1 group-title="Sports" tvg-logo="https://www.indiantvinfo.com/media/2022/10/Sony-Sports-Ten3-HD.png",SONY SPORTS TEN 3 HD
https://pubads.g.doubleclick.net:443/ssai/event/nmQFuHURTYGQBNdUG-2Qdw/master.m3u8

#EXTINF:-1 group-title="Sports" tvg-logo="https://www.indiantvinfo.com/media/2022/10/Sony-Sports-Ten4-HD.png",SONY SPORTS TEN 4 HD
https://pubads.g.doubleclick.net/ssai/event/x4LxWUcVSIiDaq1VCM7DSA/master.m3u8

#EXTINF:-1 group-title="Sports" tvg-logo="https://www.indiantvinfo.com/media/2022/10/Sony-Sports-Ten5-HD-New-Logo.png",SONY SPORTS TEN 5 HD
https://pubads.g.doubleclick.net:443/ssai/event/DD7fA-HgSUaLyZp9AjRYxQ/master.m3u8

#EXTINF:-1 group-title="Discovery-PLUS" tvg-logo="https://www.indiantvinfo.com/media/2022/10/Sony-BBC-Earth-HD-New-Logo.png",BBC EARTH HD
https://pubads.g.doubleclick.net/ssai/event/V73ovbgASP-xGvQQOukwTQ/master.m3u8

#EXTINF:-1 group-title="Discovery-PLUS" tvg-logo="https://raw.githubusercontent.com/fraudiay79/logos/master/us/discovery.png",Discovery
https://sabbirhasan.pythonanywhere.com/dplus/discovery-eng
#EXTINF:-1 group-title="Discovery-PLUS" tvg-logo="https://raw.githubusercontent.com/fraudiay79/logos/master/us/discovery.png",Discovery
https://sabbirhasan.pythonanywhere.com/dplus/discovery-hin

#EXTINF:-1 group-title="Discovery-PLUS" tvg-logo="https://raw.githubusercontent.com/fraudiay79/logos/master/us/discoveryscience.png",Discovery Science
https://sabbirhasan.pythonanywhere.com/dplus/discoverysci-eng
#EXTINF:-1 group-title="Discovery-PLUS" tvg-logo="https://raw.githubusercontent.com/fraudiay79/logos/master/us/discoveryscience.png",Discovery Science
https://sabbirhasan.pythonanywhere.com/dplus/discoverysci-hin

#EXTINF:-1 group-title="Discovery-PLUS" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Investigation_Discovery_Logo_2018.svg/1200px-Investigation_Discovery_Logo_2018.svg.png",Discovery Investigation [English]
https://sabbirhasan.pythonanywhere.com/dplus/discoveryid-eng
#EXTINF:-1 group-title="Discovery-PLUS" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/2/27/Investigation_Discovery_Logo_2018.svg/1200px-Investigation_Discovery_Logo_2018.svg.png",Discovery Investigation [HINDI]
https://sabbirhasan.pythonanywhere.com/dplus/discoveryid-hin

#EXTINF:-1 group-title="Discovery-PLUS" tvg-logo="https://raw.githubusercontent.com/fraudiay79/logos/master/us/discoveryturbo.png",Discovery Turbo
https://sabbirhasan.pythonanywhere.com/dplus/discoveryturbo

#EXTINF:-1 group-title="Discovery-PLUS" tvg-logo="https://raw.githubusercontent.com/fraudiay79/logos/master/us/animalplanet.png",Animal Planet [ENGLISH]
https://sabbirhasan.pythonanywhere.com/dplus/animalplanet-eng
#EXTINF:-1 group-title="Discovery-PLUS" tvg-logo="https://raw.githubusercontent.com/fraudiay79/logos/master/us/animalplanet.png",Animal Planet [HINDI]
https://sabbirhasan.pythonanywhere.com/dplus/animalplanet-hin

#EXTINF:-1 group-title="Discovery-PLUS" tvg-logo="https://raw.githubusercontent.com/fraudiay79/logos/master/us/tlc.png",TLC HD
https://sabbirhasan.pythonanywhere.com/dplus/tlc-eng
#EXTINF:-1 group-title="Discovery-PLUS" tvg-logo="https://raw.githubusercontent.com/fraudiay79/logos/master/us/tlc.png",TLC HD
https://sabbirhasan.pythonanywhere.com/dplus/tlc-hin
'''

import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/confident-hate/YouTube_to_m3u/main/assets/moose_na.m3u')
                return
            #os.system(f'wget {url} -O temp.txt')
            os.system(f'curl "{url}" > temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/confident-hate/YouTube_to_m3u/main/assets/moose_na.m3u')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print('#EXTM3U x-tvg-url="https://www.tsepg.cf/epg.xml.gz"')
print(banner)
#s = requests.Session()
with open('../youtube_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
