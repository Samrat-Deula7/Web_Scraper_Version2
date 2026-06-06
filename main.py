# Importing components

import searchQuery as search
import genSoup
import fetchWebUrl as siteURl
import SaveToFile as save

# Importing modules
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


df = pd.read_excel("C:\\Users\\hp\\Downloads\\consultancy data.xlsx")
search_query = df["Name of Company"].tolist()

name = []
logo = []
ConsultancyDesc = []
url = []

AboutConsultancy = ""

for i, query in enumerate(search_query[0:3]):
    
    try:
        defaultpath = "data"

        path = os.path.join("html",defaultpath+str(i)+".html")

        result = search.serchQuery(query)

        # JSON name

        name.insert(i,query)


        webUrl = siteURl.genURL(result)

        # JSON url

        url.insert(i,webUrl)

        isDone = save.saveData(result,webUrl,path)

        if isDone == "Done":
            soup = genSoup.gen(path)

        print("\n")
        print("WEBSITE IMAGE ********************")
        img = soup.find_all("img", alt=re.compile(r"logo|home", re.I)) or soup.find_all("img", class_=re.compile(r"logo|home", re.I)) or soup.find_all("img",src=re.compile(r"logo",re.I))



        if img == []:
            icon = soup.find_all("link", rel="icon") or soup.find_all("link", class_=re.compile(r"logo|home", re.I))

            if icon:
                print(icon[0]["href"])
                ImgLOGO = icon[0]["href"]

                # JSON LOGO

                logo.insert(i,ImgLOGO if ImgLOGO else "")

            else:
                logo.insert(i,"")

        else:
            if img:
                print(img[0]["src"])
                IconLOGO = img[0]["src"]

                # JSON LOGO

                logo.insert(i,IconLOGO if IconLOGO else "")
            else:
                logo.insert(i,"")

        description = soup.find_all("p", text = re.compile(r"consultancy|education", re.I))

        print("\n")
        print("WEBSITE DESCRIPTION ********************")


        print("\n")
        print("][*/[]*[[]/[*]]] This is the description block []*[/][*]/[*]/")
        print(description)

        if description:
            # JSON DESC

            ConsultancyDesc.insert(i,str(description))
        else:
            ConsultancyDesc.insert(i,"")


            print("\n")
            print("Ending of DESCRIPTION ********************")
        max_len = max(len(name),len(logo),len(ConsultancyDesc),len(url))


        if (max_len-len(name))>0:
            name += [""]
        if (max_len-len(logo))>0:
            logo += [""]
        if (max_len-len(ConsultancyDesc))>0:
            ConsultancyDesc += [""]
        if (max_len-len(url))>0:
            url += [""]

    except Exception as e:
        print("Couldn't scrape Data",e)
        pass

data = {
    "Name":name,
    "Url":url,
    "Logo":logo,
    "Desc":ConsultancyDesc
}

print("\n")
print("############### This is the data to export to json ###############")
print(name)
print("\n")
print("############### This is the data to export to json ###############")
print(url)
print("\n")
print("############### This is the data to export to json ###############")
print(logo)
print("\n")
print("############### This is the data to export to json ###############")
print(ConsultancyDesc)

df = pd.DataFrame(data)

# Export to JSON
df.to_json("HopeData.json", orient="records", indent=4)
