# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 08:42:33 2023

@author: penpo
"""

import pandas as pd
from pandas_profiling import ProfileReport

data = pd.read_csv('Police_Department_Incident_Reports__2018_to_Present.csv')
profile= ProfileReport(data, title="profile")
profile.to_file("summary_SFPD.html")

