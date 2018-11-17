
# script follows link for each drink in 'drinks' table, scrapes
# instructions, placing them in column 'instructions'.

from bs4 import BeautifulSoup
import urllib2
import re
import psycopg2

DATABASE_URL = 'postgres://fftbsmtlkjrdda:1f1ea62929ba0acbcbc74d4cd2267c04b70b1a2dfc1106c87aa440ec2ba70ee8@ec2-54-243-46-32.compute-1.amazonaws.com:5432/d7ncm4tt5a8edo'

# connect to postgers db
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

cur.execute("SELECT did, link FROM drinks")
row = cur.fetchone()

while row is not None:
    cur2 = conn.cursor()

    # open page, get BeautifulSoup
    page = urllib2.urlopen(row[1])
    soup = BeautifulSoup(page, 'html.parser')

    # get divs containing an instruction
    divs = soup.findAll("div", {"class": "comp mntl-sc-block mntl-sc-block-html"}, id=re.compile("mntl-sc-block_2.*"))

    # put instruction text into array
    instructions = []
    for div in divs:
        p = div.find('p')
        if p is not None:
            instructions.append(div.find('p').text)

    # update table instruction with instructions array
    cur2.execute("UPDATE drinks SET instructions = %s WHERE did = %s", (instructions, row[0]))

    print row[0]    # debug
    # get next row
    row = cur.fetchone()

# done, commit changes
conn.commit()
