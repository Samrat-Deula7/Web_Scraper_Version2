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

def gen(path):
    with open(path,"r", encoding="utf-8") as f:
        html_content = f.read()

        soupData = BeautifulSoup(html_content,"html.parser")
        return soupData