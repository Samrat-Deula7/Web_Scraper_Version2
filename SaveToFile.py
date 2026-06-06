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

def saveData(results,url,path):
    try:
        response = requests.get(url, timeout=60)
        with open(path,"w", encoding="utf-8") as f:
            f.write(response.text)
        return "Done"
    except requests.exceptions.RequestException as e:
        print(f"Couldn't scrape {url}: {e}")
        return None