#!/usr/bin/env python
# coding: utf-8

# This notebook has code for calculating how you should pre-culture the fission yeast *Schizosaccharomyces pombe* in order to get a well-defined density of cells in your flask at a given time.

# In[1]:


# I want to create a variable to store the name of the strain I am using

strain_name = input("What is the name of your yeast strain? ")


# In[3]:


# I want to store the current optical density (OD) of my culture.
# If the OD is higher than 5, I want to print a message saying that this is too high for reliable calculations.

initial_OD = input("What is the current OD of the culture? ")
initial_OD=int(initial_OD)

if initial_OD > 5:
    print("OD is too high! Results will be unreliable!")


# In[5]:


# I want to create a variable to store the doubling time of S. pombe in hours.
# The doubling time of S. pombe is 2 hours and 5 minutes.
# I need to convert this into just hours.

doubling_time = 2 + 5/60


# In[6]:


# Culturing yeast is a time-sensitive process.
# I need to be able to do maths involving dates and times in order to calculate my optical density.
# To do this, I will import a package called datetime

import datetime


# In[9]:


# I want to use the datetime package to define a date and time in the future when I will harvest my cells.
# I can do this by using datetime.datetime(year, month, day, hour, minute)

harvest_datetime = datetime.datetime(2023, 3, 8, 19,1)
print("Cells should be harvested at", harvest_datetime)


# In[10]:


# I am assuming I am going to do my culturing right now - so I need to get a datetime for this instant
# I can do this using the now() method of datetime.datetime

inoculation_time = datetime.datetime.now()
print("Current date and time is: ", inoculation_time)


# In[11]:


# I want to calculate how many hours there are between my inoculation time and my harvesting time.
# Subtracting datetimes from each other gives me a 'timedelta'

time_difference = harvest_datetime - inoculation_time

# I'm using an inbuilt method to get my timedelta in seconds
time_difference_in_seconds = time_difference.total_seconds()

# I now want to convert my time difference in seconds into hours.
# I'll do this by converting into minutes, then into hours

time_difference_in_minutes = time_difference_in_seconds/60
time_difference_in_hours = time_difference_in_minutes/60

# The number of doublings the cells will do during the time difference is
# the time difference in hours divided by the doubling time in hours.
# We subtract 1 because there is a lag time of approximately one doubling time.

n_doublings = time_difference_in_hours/doubling_time - 1


# In[60]:


# I want to make a list of different ODs that I want my final culture to have.
# These should range from 0.1 to 1.0 in steps of 0.1

final_ODs = []
for i in range(0,10,1):
    OD = (i+1)/10
    final_ODs.append(OD)  
print(final_ODs)


# In[61]:


# The last piece of information I need to do the calculation is the volume I want to inoculate in mL.
# I only have flasks in my lab that can handle volumes between 10 and 100 mL, so I need to check that
# my target volume can be used

culture_volume = 50
if culture_volume < 10:
    print("I don't have a flask small enough.")
elif culture_volume > 100:
    print("I don't have a flask big enough.")
else:
    print("Appropriate flask is available!")


# In[ ]:


# Now I need to calculate how much of my original culture I need to inoculate into my fresh media
# for each of my desired final ODs.
# The formula for this is


# $$ \text{Volume}_\text{inoculation} = \frac{\text{Volume}_\text{culture} \times OD_\text{final}}{2^{n_\text{doublings}} \times OD_\text{initial}} $$

# In[64]:


inoculation_volumes = []
lenfin=len(final_ODs)


# loop through each of the ODs I want to achieve
for i in range(lenfin):
    final_OD = final_ODs[i]
    inoculation_volume = (culture_volume*final_OD)/((2**n_doublings)*initial_OD)
    
    # multiply the volumes in mL to get volumes in uL
    inoculation_volumes.append(inoculation_volume*1000)


# In[63]:


# display information to proceed with culturing
print('Strain name:' , strain_name)
print('Total culture volume: ', culture_volume, 'mL')
print(inoculation_volumes)
for i in range(len(final_ODs)):
    print('For OD', final_ODs[i], ':')
    print('inoculate ', inoculation_volumes[i], 'uL of initial culture')


# In[ ]:




