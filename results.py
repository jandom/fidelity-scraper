#!/usr/bin/env python

import urllib2
import json
import pandas as pd

def read_contents(url):
    request = urllib2.urlopen(url)
    contents = request.read()
    return contents



url_template = "https://lt.morningstar.com/api/rest.svc/9vehuxllxs/security/screener?page={}&pageSize=50&sortOrder=LegalName%20asc&outputType=json&version=1&languageId=en-GB&currencyId=GBP&universeIds=ETEXG%24XLON_3518%7CETALL%24%24ALL_3518&securityDataPoints=SecId%7CName%7CTenforeId%7CholdingTypeId%7Cisin%7Csedol%7CQR_MonthDate%7CLegalName%7CYield_M12%7COngoingCostEstimated%7CStarRatingM255%7CCustomCategoryId3Name%7CCollectedSRRI%7CQR_GBRReturnM12_5%7CQR_GBRReturnM12_4%7CQR_GBRReturnM12_3%7CQR_GBRReturnM12_2%7CQR_GBRReturnM12_1%7CCustomMinimumPurchaseAmount%7CTransactionFeeEstimated%7CPerformanceFee%7CGBRReturnM0%7CGBRReturnM12%7CGBRReturnM36%7CGBRReturnM60%7CGBRReturnM120%7CTrackRecordExtension&filters=&term=&subUniverseId=ETFEI"

urls = [url_template.format(i) for i in range(1,7)]

contents = [ read_contents(url) for url in urls ]

jsons = [ json.loads(content) for content in contents ]

pages = [json['rows'] for json in jsons]

rows = [row for page in pages for row in page]

print(len(rows) )

df.to_json("results.json")
