# Uses data available at http://data.worldbank.org/indicator
# on Forest area (sq. km) and Agricultural land area (sq. km).
# Prompts the user for two distinct years between 1990 and 2004
# as well as for a strictly positive integer N,
# and outputs the top N countries where:
# - agricultural land area has increased from oldest input year to most recent input year;
# - forest area has increased from oldest input year to most recent input year;
# - the ratio of increase in agricultural land area to increase in forest area determines
#   output order.
# Countries are output from those whose ratio is largest to those whose ratio is smallest.
# In the unlikely case where many countries share the same ratio, countries are output in
# lexicographic order.
# In case fewer than N countries are found, only that number of countries is output.


# Written by *** and Eric Martin for COMP9021


import sys
import os
import csv
from collections import defaultdict
agricultural_land_filename = 'API_AG.LND.AGRI.K2_DS2_en_csv_v2.csv'
if not os.path.exists(agricultural_land_filename):
    print(f'No file named {agricultural_land_filename} in working directory, giving up...')
    sys.exit()
forest_filename = 'API_AG.LND.FRST.K2_DS2_en_csv_v2.csv'
if not os.path.exists(forest_filename):
    print(f'No file named {forest_filename} in working directory, giving up...')
    sys.exit()
try:
    years = {int(year) for year in
                           input('Input two distinct years in the range 1990 -- 2014: ').split('--')
            }
    if len(years) != 2 or any(year < 1990 or year > 2014 for year in years):
        raise ValueError
except ValueError:
    print('Not a valid range of years, giving up...')
    sys.exit()
try:
    top_n = int(input('Input a strictly positive integer: '))
    if top_n < 0:
        raise ValueError
except ValueError:
    print('Not a valid number, giving up...')
    sys.exit()


countries = []
year_1, year_2 = None, None
# Insert your code here
year = []
for i in years:
    year.append(i)
if year[0] > year[1]:
    year_1 = year[1]
    year_2 = year[0]
else:
    year_1 = year[0]
    year_2 = year[1]

agricultural_land_library = defaultdict(list)
forest_library = defaultdict(list)
agr_after_calculate = defaultdict(float)
forest_after_calculate = defaultdict(float)
temp_countries =[]

with open (agricultural_land_filename,encoding = 'utf-8') as agricultural_land,\
                open(forest_filename,encoding = 'utf-8') as forest:
                agricultural_land_2 = agricultural_land.readlines()
                forest_2 = forest.readlines()
                for line in agricultural_land_2[5:]:
                    country_name,country_code,indicator_name,indicator_code,year = line.split('\",\"',4)
                    country_name = country_name.replace('\"','')
                    agricultural_land_library[country_name].append(year.split('\",\"'))
                    for splited_year in range(len(agricultural_land_library[country_name][0])):
                        agricultural_land_library[country_name][0][splited_year] = \
                                                            agricultural_land_library[country_name][0][splited_year].replace('\"','')
                for line in forest_2[5:]:
                    country_name,country_code,indicator_name,indicator_code,year = line.split('\",\"',4)
                    country_name = country_name.replace('\"','')
                    forest_library[country_name].append(year.split('\",\"'))
                    for splited_year in range(len(forest_library[country_name][0])):
                        forest_library[country_name][0][splited_year] = \
                                                            forest_library[country_name][0][splited_year].replace('\"','')
        

for country_name in agricultural_land_library:
        try:
             if float(agricultural_land_library[country_name][0][year_2-1960]) \
            - float(agricultural_land_library[country_name][0][year_1-1960]) > 0:
                 agr_after_calculate[country_name] = float(agricultural_land_library[country_name][0][year_2-1960])\
                                                                  -float(agricultural_land_library[country_name][0][year_1-1960])
        except ValueError:
            continue

for country_name in forest_library:
    try:
        if float(forest_library[country_name][0][year_2-1960]) \
            - float(forest_library[country_name][0][year_1-1960]) > 0:
            forest_after_calculate[country_name] = (float(forest_library[country_name][0][year_2-1960])\
                                                   -float(forest_library[country_name][0][year_1-1960]))
    except ValueError:
        continue

for country_name in agr_after_calculate:
    temp_agr_value = agr_after_calculate[country_name]
    temp_forest_value = forest_after_calculate[country_name]
    try:
        temp_value = round(temp_agr_value/temp_forest_value,2)

        temp_countries.append((country_name,temp_value))
    except ZeroDivisionError:
        continue

temp_countries.sort(key = lambda d: d[1])
temp_countries.reverse()
i = 0
while i < top_n:
    temp = ""
    temp += str(temp_countries[i][0])
    temp += " (" + str(temp_countries[i][1]) + ")"

    temp2 = "{} ({:.2f})".format(temp_countries[i][0], temp_countries[i][1])
    countries.append(temp2)
    i = i+1

print(f'Here are the top {top_n} countries or categories where, between {year_1} and {year_2},\n'
      '  agricultural land and forest land areas have both strictly increased,\n'
      '  listed from the countries where the ratio of agricultural land area increase\n'
      '  to forest area increase is largest, to those where that ratio is smallest:')
print('\n'.join(country for country in countries))
    
