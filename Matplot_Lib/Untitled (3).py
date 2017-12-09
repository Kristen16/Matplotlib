
# coding: utf-8

# In[40]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[41]:


city_data = "Untitled Folder/city_data.csv"
ride_data = "Untitled Folder/ride_data.csv"

city_data_df = pd.read_csv(city_data)
ride_data_df = pd.read_csv(ride_data)



# In[42]:


combined_data_df = pd.merge(city_data_df, ride_data_df, how='outer', on='city')
del combined_data_df['date']
combined_data_df


# In[43]:


Urban = combined_data_df[combined_data_df['type'] == "Urban"]
print(avg_fare)


# In[44]:


Suburban = combined_data_df[combined_data_df['type'] == "Suburban"]
print(Suburban)


# In[45]:


Rural = combined_data_df[combined_data_df['type'] == "Rural"]
print(Rural)


# In[47]:


urban_count = Urban.groupby(["city"]).count()["ride_id"]
urban_count


# In[49]:


urban_fare = Urban.groupby(["city"]).mean()["fare"]
print(urban_fare)


# In[50]:


urban_driver = Urban.groupby(["city"]).mean()["driver_count"]
print(urban_driver)


# In[52]:


suburban_count = Suburban.groupby(["city"]).count()["ride_id"]
suburban_count


# In[53]:


suburban_driver = Suburban.groupby(["city"]).mean()["driver_count"]
print(suburban_driver)


# In[54]:


suburban_fare = Suburban.groupby(["city"]).mean()["fare"]
print(suburban_fare)


# In[55]:


rural_count = Rural.groupby(["city"]).count()["ride_id"]
rural_count


# In[56]:


rural_driver = Rural.groupby(["city"]).mean()["driver_count"]
print(rural_driver)


# In[57]:


rural_fare = Rural.groupby(["city"]).mean()["fare"]
print(rural_fare)


# In[62]:


plt.scatter(urban_count, urban_fare, marker="o", c="red", edgecolors="black", alpha=0.75)

plt.title("Ride Data Urban")
plt.ylabel("Average Fare")
plt.xlabel("Total Number of Rides")
plt.xlim((0,50))
plt.grid(True)

plt.show()


# In[63]:


plt.scatter(suburban_count, suburban_fare, marker="o", c ="blue", edgecolors="black", alpha=0.75)

plt.title("Ride Data Suburban")
plt.ylabel("Average Fare")
plt.xlabel("Total Number of Rides")
plt.xlim((0,50))
plt.grid(True)

plt.show()


# In[64]:


plt.scatter(rural_count, rural_fare, marker="o", c ="yellow", edgecolors="black", alpha=0.75)

plt.title("Ride Data Rural")
plt.ylabel("Average Fare")
plt.xlabel("Total Number of Rides")
plt.xlim((0,50))
plt.grid(True)

plt.show()


# In[74]:


urban_fares = Urban.groupby(["type"]).sum()["fare"]
urban_fares


# In[75]:


suburban_fares = Suburban.groupby(["type"]).sum()["fare"]
suburban_fares


# In[77]:


rural_fares = Rural.groupby(["type"]).sum()["fare"]
rural_fares


# In[78]:


Total = combined_data_df['fare'].sum()
print (Total)


# In[86]:


city = ["Urban", "Suburban", "Rural"]
Fares = [urban_fares, suburban_fares, rural_fares]
colors = ["red","lightblue","yellow"]
explode = (0.1,0,0)


# In[87]:


plt.pie(Fares, explode=explode, labels=city, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=140)


# In[88]:


plt.axis("equal")


# In[89]:


plt.savefig("Pyfares.png")
plt.show()


# In[90]:


urban_rides = Urban.groupby(["type"]).count()["ride_id"]
urban_rides


# In[92]:


suburban_rides = Suburban.groupby(["type"]).count()["ride_id"]
suburban_rides


# In[94]:


rural_rides = Rural.groupby(["type"]).count()["ride_id"]
rural_rides


# In[96]:


Total2 = combined_data_df['ride_id'].count()
print (Total2)


# In[97]:


city = ["Urban", "Suburban", "Rural"]
rides = [urban_rides, suburban_rides, rural_rides]
colors = ["red","lightblue","yellow"]
explode = (0.1,0,0)


# In[98]:


plt.pie(rides, explode=explode, labels=city, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=140)


# In[99]:


plt.axis("equal")


# In[100]:


plt.savefig("Pyrides.png")
plt.show()


# In[103]:


urban_drivers = Urban.groupby(["type"]).sum()["driver_count"]
urban_drivers


# In[104]:


suburban_drivers = Suburban.groupby(["type"]).sum()["driver_count"]
suburban_drivers


# In[105]:


rural_drivers = Rural.groupby(["type"]).sum()["driver_count"]
rural_drivers


# In[106]:


Total3 = combined_data_df['driver_count'].sum()
print (Total3)


# In[108]:


city = ["Urban", "Suburban", "Rural"]
drivers = [urban_drivers, suburban_drivers, rural_drivers]
colors = ["red","lightblue","yellow"]
explode = (0.1,0,0)


# In[109]:


plt.pie(drivers, explode=explode, labels=city, colors=colors,
        autopct="%1.1f%%", shadow=True, startangle=140)


# In[110]:


plt.axis("equal")


# In[111]:


plt.savefig("Pydrivers.png")
plt.show()

