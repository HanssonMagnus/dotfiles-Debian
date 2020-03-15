test = [file for files in glob.glob(test_path + "/*.pdf")]
test
import glob
test_path = os.path.join(wd_in, 'bank of guatemala')
test = [file for files in glob.glob(test_path + "**/*.pdf")]
test
test_path
import glob
test_path = os.path.join(wd_in, 'bank of guatemala')
test = [file for files in glob.glob(test_path + "*.pdf")]
test
import glob
test_path = os.path.join(wd_in, 'bank of guatemala')
test = [file for files in glob.glob(test_path + "/*.pdf")]
test
import glob
test_path = os.path.join(wd_in, 'bank of guatemala')
test = [file for file in glob.glob(test_path + "/*.pdf")]
test
import glob
test_path = os.path.join(wd_in, 'bank of algeria')
test = [file for file in glob.glob(test_path + "/*.pdf")]
test
test[0]
os.path.split(test[0])
os.path.split(test[0])[-1]
os.path.basename(test[0])
import glob
test_path = os.path.join(wd_in, 'bank of algeria')
test = [file for file in glob.glob(test_path + "/*.pdf")]
test
import glob
test_path = os.path.join(wd_in, 'bank of algeria')
test = [file for file in glob.glob(test_path + "*.pdf")]
test
import glob
test_path = os.path.join(wd_in, 'bank of algeria')
test = [file for file in glob.glob(test_path + "/*.pdf")]
os.path.basename(test[0])
test = os.path.basename(test[0])
test
test.replace(".pdf", "")
os.path.join(wd_out, "folder", test, ".csv")
os.path.join(wd_out, "folder", test + ".csv")
runfile('/home/magnus/Documents/Python/Research/Scrape_BIS/FINAL_ALL_MULTIPLE_2020_01_10/pdf_to_txt.py', wdir='/home/magnus/Documents/Python/Research/Scrape_BIS/FINAL_ALL_MULTIPLE_2020_01_10')
folders
runfile('/home/magnus/Documents/Python/Research/Scrape_BIS/FINAL_ALL_MULTIPLE_2020_01_10/pdf_to_txt.py', wdir='/home/magnus/Documents/Python/Research/Scrape_BIS/FINAL_ALL_MULTIPLE_2020_01_10')

## ---(Fri Jan 31 07:44:18 2020)---
import logging
import os
import glob
import textract
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
wd_in = '/home/magnus/Documents/Python/Research/Scrape_BIS/FINAL_ALL_MULTIPLE_2020_01_10/2_speeches_all_multiple_ADDED'

# Working directory to save files
wd_out = '/home/magnus/Documents/Python/Research/Scrape_BIS/FINAL_ALL_MULTIPLE_2020_01_10/2_speeches_all_multiple_ADDED_token'
wd_in = '/home/magnus/Documents/Python/Research/Scrape_BIS/FINAL_ALL_MULTIPLE_2020_01_10/'
file_1 = 'r190821a.pdf'
text = textract.process(os.path.join(wd, file_1)) # type bytes
text = text.decode('utf-8')
text = textract.process(os.path.join(wd_in, file_1)) # type bytes
text = text.decode('utf-8')
text
files = [file for file in glob.glob(wd_in + "/*.pdf")]
files
os.path.basename(files[0])
file_name = os.path.basename(files[0])
file_name = file_name.replace(".pdf", "")
file_name
file_name = os.path.basename(files[0])
file_name
file_name = file_name.replace("_speech.pdf", "")
file_name
file_name[0]
file_name[1:]
order = file_name[0]
import datetime as dt
date = file_namne[1:]
date = file_name[1:]
date
dt.strftime(date, '%Y-%m-%d')
strftime
dt
dt.strftime()
date
date.strft('%Y-%m-%d')
dt.Parse(date)
dt.strptime()
dt.datetime.strptime()
dt.datetime.strptime(date, "%Y-%m-%d")
dt.datetime.strptime(date, "%y%m%d")
date = dt.datetime.strptime(date, "%y%m%d")
date
date = dt.datetime.strftime(date, "%Y-%m-%d")
date
text
runfile('/home/magnus/Documents/Python/Research/Scrape_BIS/2020_01_30/pdf_to_txt_v2.py', wdir='/home/magnus/Documents/Python/Research/Scrape_BIS/2020_01_30')

## ---(Fri Jan 31 08:21:59 2020)---
runfile('/home/magnus/Documents/Python/Research/Scrape_BIS/2020_01_30/pdf_to_txt_v2.py', wdir='/home/magnus/Documents/Python/Research/Scrape_BIS/2020_01_30')
hej = "1991-11-30_d.txt"
hej[0:10]
runfile('/home/magnus/Documents/Python/Research/Scrape_BIS/2020_01_30/meta_analysis.py', wdir='/home/magnus/Documents/Python/Research/Scrape_BIS/2020_01_30')
wd
runfile('/home/magnus/Documents/Python/Research/Scrape_BIS/2020_01_30/meta_analysis.py', wdir='/home/magnus/Documents/Python/Research/Scrape_BIS/2020_01_30')
all_files
len(all_files)
sort(all_files)
type(all_files)
all_files.sort()
all_files
all_files[0]
all_files[-1]
years = ['1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', 
         '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', 
         '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
len(years)
years[24]
years[23]
years = ['1997': 0, '1998': 0, '1999': 0, '2000': 0, '2001': 0, '2002': 0, '2003': 0, '2004': 0, 
         '2005': 0, '2006': 0, '2007': 0, '2008': 0, '2009': 0, '2010': 0, '2011': 0, '2012': 0, 
         '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0] #24
years = {'1997': 0, '1998': 0, '1999': 0, '2000': 0, '2001': 0, '2002': 0, '2003': 0, '2004': 0, 
         '2005': 0, '2006': 0, '2007': 0, '2008': 0, '2009': 0, '2010': 0, '2011': 0, '2012': 0, 
         '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}
years
years.name
years.names
years.names()
names.year
name.year
year.items()
years.items()
years.values()
years.keys()
years.keys()[0]
for i in years.keys(): print(i)
for i in years.keys(): type(i)
for i in years.keys(): print(type(i))
re.findall('1997*', all_files)
import re
re.findall('1997*', all_files)
all_files[0]
1997 in all_files[0]
"1997" in all_files[0]
years = {'1997': 0, '1998': 0, '1999': 0, '2000': 0, '2001': 0, '2002': 0, '2003': 0, '2004': 0, 
         '2005': 0, '2006': 0, '2007': 0, '2008': 0, '2009': 0, '2010': 0, '2011': 0, '2012': 0, 
         '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0} #24

for year in years.keys():
    for file in all_files:
        if year in file:
            years[year] +=1
years
import pandas as pd
df = pd.DataFrame()
df
df = pd.DataFrame(columns=years)
df
folders
df = pd.DataFrame(columns=years, rows=folders)
df
years
df
pd.DataFrame(years)
pd.DataFrame(data=years)
pd.DataFrame(columsn=years)
pd.DataFrame(columns=years)
pd.DataFrame(years)
df = pd.DataFrame(columns=years, index=folders)
df
df = pd.DataFrame(columns=years, index=folders.sort())
df
folders
folders.sort()
df = pd.DataFrame(columns=years, index=folders)
df
file_name
file_name[0:4]
df = pd.DataFrame(0, columns=years, index=folders)
df
df["1997"]
df["1997"]["sveriges riksbank"]
df["1997"]["sveriges riksbank"] = 3
df
df["1997"]["sveriges riksbank"] += 1
df
runfile('/home/magnus/Documents/Python/Research/Scrape_BIS/2020_01_30/meta_analysis.py', wdir='/home/magnus/Documents/Python/Research/Scrape_BIS/2020_01_30')
df
print(df)
df.to_string()
runfile('/home/magnus/Documents/Python/Research/Scrape_BIS/2020_01_30/meta_analysis.py', wdir='/home/magnus/Documents/Python/Research/Scrape_BIS/2020_01_30')
folders