#!/usr/bin/python
#encoding=utf-8

import sys, time, random, string
reload(sys)
sys.setdefaultencoding('utf-8')

import logging
import logmodule.logHelper
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

import httplib, urllib

# 生成指定位数的随机字符串，字符为字母或数字
def getRandomString(idLength):
    charSeq = string.ascii_letters + string.digits
    randString = 'owzeBj'
    for i in range(idLength):
        randString += random.choice(charSeq)
    return randString

# 对指定的作品（zpid）投一张票
def voteOnce(zpid):
    conn = httplib.HTTPConnection("www.4006880288.com")
    opid = getRandomString(22)
    logger.debug('opid = %s', opid)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    postParams = urllib.urlencode({'zpid': zpid, 'opid': opid, 'md_id': 70, 'act': 'zuopin_toupiao'})
    conn.request("POST", "/wtg1/mobile/user.php", postParams, headers)
    response = conn.getresponse()
    logger.debug('response.status=%s, response.reason=%s', response.status, response.reason)
    respData = response.read()
    logger.debug('response.data=%s', respData)
    conn.close()

# 投票控制器：指定作品（zpid）和投票张数（voteNum），并随机出投票间隔时间
def voteController(zpid, voteNum):
    logger.info('Start Voting to zpid(%s), Total votes: %s', zpid, voteNum)
    for i in range(voteNum):
        voteOnce(zpid)
        randomSleepTime = random.randint(1, 60)
        logger.info('%s tickets has been voted, the next ticket will be voted after %s seconds.', i+1, randomSleepTime)
        time.sleep(randomSleepTime)
    logger.info('Voting Ended!')

if __name__ == '__main__':
    #voteOnce(38)
    voteController(38, 3)
