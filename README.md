# adlist

Contains an adlist for use with Pi-hole. Merged this from:

- https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts
- https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt
- https://blocklistproject.github.io/Lists/phishing.txt
- https://www.github.developerdan.com/hosts/lists/amp-hosts-extended.txt
- https://blocklistproject.github.io/Lists/tracking.txt
- https://blocklistproject.github.io/Lists/abuse.txt
- https://blocklistproject.github.io/Lists/ransomware.txt
- https://blocklistproject.github.io/Lists/scam.txt

Thanks to the maintainers of the original lists.

Every Saturday night, the `check_upstram.yaml` will check Stephen Black's repository for changes and update `ad_list.txt` accordingly. I didn't spend much time checking the other lists' update schedule but checking one of the better maintained ones once a week will probably do fine.
