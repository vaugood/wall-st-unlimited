from urllib.parse import quote
import requests
import json

def algolia(ticker):

    url = "https://17iqhzwxzw-1.algolianet.com/1/indexes/companies/query?x-algolia-api-key=be7c37718f927d0137a88a11b69ae419&x-algolia-application-id=17IQHZWXZW"

    payload = json.dumps({
    "query": f"{ticker}",
    "highlightPostTag": " ",
    "highlightPreTag": " ",
    "restrictHighlightAndSnippetArrays": True
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    data = response.json()

    return data['hits'][0]['url']

def statement(canonicalUrl):

    url = f"https://statements.simplywall.st/statements/{canonicalUrl}?include=statements.question"

    payload = {}
    headers = {
    'Cookie': '__cf_bm=ZY4c9Txiu5K.JmxNbk5P.s2MtaV6g0PgzS2.Jwizhr4-1692470485-0-Ad64bF8ifcjJa1g7znfXPmCul2UxB1k14JMw9Esz1aLZWqSm6k+n06uxPRuxd5AeI9Yk9nm66JgLwcXifv/+3Q4=; _sws_uid=43d35601505669d490bbd04cd179f6f0; ab.storage.deviceId.e32ab9b0-7a06-40f3-919b-6c08c1447e63=%7B%22g%22%3A%22842b4f00-6e1e-4315-bce8-d4add5b52a0e%22%2C%22c%22%3A1680060396071%2C%22l%22%3A1690006327683%7D; ab.storage.sessionId.e32ab9b0-7a06-40f3-919b-6c08c1447e63=%7B%22g%22%3A%22de6c5e1e-03ac-9a88-8568-02b188dbd61c%22%2C%22e%22%3A1690009397840%2C%22c%22%3A1690006327681%2C%22l%22%3A1690007597840%7D; ab.storage.userId.e32ab9b0-7a06-40f3-919b-6c08c1447e63=%7B%22g%22%3A%2243d35601505669d490bbd04cd179f6f0%22%2C%22c%22%3A1680060396066%2C%22l%22%3A1690006327683%7D; cf_clearance=NEPnsD2P9NX6Ow01Hzwh._AqZ1Yi_NNtg2sfwPvfCmw-1689998418-0-0.2.1689998418'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    report = response.json()
    return report['data']

def main(ticker):
    canonicalUrl = algolia(ticker)
    canonicalUrl = quote(canonicalUrl[1:], safe='')
    report = statement(canonicalUrl)

    symbol = report['symbol']
    name = report['name']
    data = report['statements']['data']

    return symbol, name, data