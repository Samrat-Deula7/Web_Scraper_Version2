import pandas as pd
from ddgs import DDGS
import requests
import re
from bs4 import BeautifulSoup
from rapidfuzz import fuzz
import os
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd

def genURL(results):
    count = 0
    dotIndex = 0
    slashIndex = 0
    best_href = None
    best_score = -1
    FBURL = ""
    HrefArr = []
    FilteredHref = []


    for i in range(8):
        HrefArr.insert(i,results[i]["href"])

    for i in range(8):
        if "facebook" in HrefArr[i]:
            FBURL = HrefArr[i]
            print("\n")
            print("This is the Facebook LINK ***************")
            print(HrefArr[i])

    FilteredHref = [x for x in HrefArr if not any(k in x for k in ["facebook", "linkedin", "youtube","school","maps","worldwide","tiktok","wikipedia","instagram"])]

    print("\n")
    print("ORIGINAL LIST OF LINKS ********************")
    print(HrefArr)

    print("\n")
    print("FILTERED LIST OF LINKS ********************")
    print(FilteredHref)

    for i , c in enumerate(FBURL):
        if c == "/":
            count +=1
            if count == 3:
                slashIndex = i+1
                break

    siteURLName = "https://"+FBURL[slashIndex:-1]

    if "." in siteURLName:
        for i , s in enumerate(siteURLName):
            if s == ".":
                dotIndex = i
                break

    filteredSiteURLName = "https://"+siteURLName[0:dotIndex]

    if "edu" in FilteredHref:
        print("\n")
        print("##### adding edu #########")
        filteredSiteURLName +="edu"


    print("\n")
    print("ORIGINAL SITE NAME ********************")
    print(siteURLName)

    print("\n")
    print("FILTERED SITE NAME ********************")
    print(filteredSiteURLName)


    if (filteredSiteURLName == "https://"):
        for href in FilteredHref:
            clean_href = href.lower().replace("-", "").replace(" ", "")
            score=fuzz.partial_ratio(siteURLName.lower(),clean_href.lower())
            ScoreBoard.append(score)

            if score > best_score:
                best_score = score
                best_href = href

            webURLName = best_href
    else:
        for href in FilteredHref:
            clean_href = href.lower().replace("-", "").replace(" ", "")
            score=fuzz.partial_ratio(filteredSiteURLName.lower(),clean_href.lower())
            ScoreBoard.append(score)

            if score > best_score:
                best_score = score
                best_href = href

            webURLName = best_href

    HrefArr = []
    FilteredHref = []

    print("\n")
    print("WEBSITE URL ********************")
    print(webURLName)


    return webURLName