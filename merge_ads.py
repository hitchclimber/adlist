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
    ]
    ads = asyncio.run(merge_ads(urls))
    save_list("ad_list.txt", ads)
