#encoding=utf-8

import sys
import time
import random
import string

import httplib
import urllib


# 生成指定位数的随机字符串，字符为字母或数字
def getRandomString(id_length):
    charSeq = string.ascii_letters + string.digits
    randString = 'owzeBj'
    for i in range(id_length):
        randString += random.choice(charSeq)
    return randString

# 对指定的作品（zpid）投一张票
def voteOnce(zpid):
    conn = httplib.HTTPConnection("www.4006880288.com")
    opid = getRandomString(22)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    postParams = urllib.urlencode({'zpid': zpid, 'opid': opid, 'md_id': 70, 'act': 'zuopin_toupiao'})
    conn.request("POST", "/wtg1/mobile/user.php", postParams, headers)
    conn.close()

# 投票控制器：指定作品（zpid）和投票张数（voteNum），并随机出投票间隔时间
def voteController(zpid, voteNum):
    print '======== Start to vote zpid({0}), Total votes: {1}'.format(zpid, voteNum)
    for i in range(voteNum):
        voteOnce(zpid)
        randomSleepTime = random.randint(1, 4)
        print '{0} tickets has been voted, the next ticket will be voted after {1} seconds.'.format(i+1, randomSleepTime)
        time.sleep(randomSleepTime)
    print '======== Voting Ended!'


if __name__ == '__main__':
    # voteOnce(38)
    voteController(38, 3)
