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

def serchQuery(queryName):
    return DDGS().text(
    query=queryName,
    region = "wt-wt",
    safesearch='off',
    timeLimit='7d',
    max_results=50
    )