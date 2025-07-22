import asyncio
import aiohttp


async def fetch_url(session, url):
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.text()


def read_list(content):
    return [
        line.strip()
        for line in content.split("\n")
        if line.strip() and line.startswith("0")
    ]


async def merge_ads(urls):
    all = set()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        for content in results:
            all.update(read_list(content))
    return all


# this was on top of pi-holes default list
def save_list(filename, data):
    with open(filename, "w") as f:
        f.write(
            """
127.0.0.1 localhost
127.0.0.1 localhost.localdomain
127.0.0.1 local
255.255.255.255 broadcasthost
::1 localhost
::1 ip6-localhost
::1 ip6-loopback
fe80::1%lo0 localhost
ff00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
ff02::3 ip6-allhosts
0.0.0.0 0.0.0.0

"""
        )
        for line in data:
            f.write(line + "\n")


if __name__ == "__main__":
    urls = [
        "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
        "https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt",
        "https://blocklistproject.github.io/Lists/phishing.txt",
        "https://www.github.developerdan.com/hosts/lists/amp-hosts-extended.txt",
        "https://blocklistproject.github.io/Lists/tracking.txt",
        "https://blocklistproject.github.io/Lists/abuse.txt",
        "https://blocklistproject.github.io/Lists/ransomware.txt",
        "https://blocklistproject.github.io/Lists/scam.txt",
        "https://raw.githubusercontent.com/PolishFiltersTeam/KADhosts/master/KADhosts.txt",
        "https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Spam/hosts",
        "https://v.firebog.net/hosts/static/w3kbl.txt",
        "https://raw.githubusercontent.com/matomo-org/referrer-spam-blacklist/master/spammers.txt",
        "https://someonewhocares.org/hosts/zero/hosts",
        "https://raw.githubusercontent.com/VeleSila/yhosts/master/hosts",
        "https://adaway.org/hosts.txt",
        "https://v.firebog.net/hosts/AdguardDNS.txt",
        "https://v.firebog.net/hosts/Admiral.txt",
        "https://raw.githubusercontent.com/anudeepND/blacklist/master/adservers.txt",
        "https://v.firebog.net/hosts/Easylist.txt",
        "https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=0&mimetype=plaintext",
        "https://raw.githubusercontent.com/FadeMind/hosts.extras/master/UncheckyAds/hosts",
        "https://raw.githubusercontent.com/bigdargon/hostsVN/master/hosts",

        "https://v.firebog.net/hosts/Easyprivacy.txt",
        "https://v.firebog.net/hosts/Prigent-Ads.txt",
        "https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.2o7Net/hosts",
        "https://raw.githubusercontent.com/crazy-max/WindowsSpyBlocker/master/data/hosts/spy.txt",
        "https://hostfiles.frogeye.fr/firstparty-trackers-hosts.txt",
        "https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/android-tracking.txt",
        "https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/SmartTV.txt",
        "https://raw.githubusercontent.com/Perflyst/PiHoleBlocklist/master/AmazonFireTV.txt",

        "https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/AntiMalwareHosts.txt",
        "https://v.firebog.net/hosts/Prigent-Crypto.txt",
        "https://raw.githubusercontent.com/FadeMind/hosts.extras/master/add.Risk/hosts",
        "https://bitbucket.org/ethanr/dns-blacklists/raw/8575c9f96e5b4a1308f2f12394abd86d0927a4a0/bad_lists/Mandiant_APT1_Report_Appendix_D.txt",
        "https://phishing.army/download/phishing_army_blocklist_extended.txt",
        "https://gitlab.com/quidsup/notrack-blocklists/raw/master/notrack-malware.txt",
        "https://v.firebog.net/hosts/RPiList-Malware.txt",
        "https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt",
        "https://raw.githubusercontent.com/AssoEchap/stalkerware-indicators/master/generated/hosts",
        "https://urlhaus.abuse.ch/downloads/hostfile/"
    ]
    ads = asyncio.run(merge_ads(urls))
    save_list("ad_list.txt", ads)
