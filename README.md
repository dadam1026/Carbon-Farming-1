# Carbon Farming: A Farm-to-Table Strategy for Food & Energy Security
![image](https://user-images.githubusercontent.com/78511177/171748204-f95510ec-fe34-4cd7-bf20-9ce432bc7d79.png)

Motivation
"Control oil and you control nations; control food and you control people." - Henry Kissinger
        As the population grows, so will the demand for food
        Food and nature emit 14 out of 59 Gigatons of carbon, so sustainable food systems and agricultural practices are needed to ajust what we eat, how we grow our food, and even waste it, and protect nature nature
        To curate a tailored, sustainable agricultural practice youe must measure your carbon footprint, analyze your emissions, and execute on meaninful reductions
        
        
This project aims to take time-lapsed, satellite imagery from areas undergoing deforestation across the globe to measure its carbon footprint. First we meaure the % of green land at each timestamp, 1985, 1995, 2005, 2015, and 2020 to conduct cover crop analysis. Next we measure surface roughness at each timestamp to perform conservation tillage verififcation. This monitors soil disturbance which causes the soil's carbon to be released into the atmosphere. Lastly, for the geopgraphic region being analyzed, we use images of the vegetation and livestock unique to the input area to further study crop yield, quality, and plant resistance to abiotic and biotic stresses. 

A compounding problem
Investing in the now and the new
Green discount instead of green premium
the right outcome must be the profitable outcome to be the probable outcome
"We don't inherit the world from our ancestors. We are borrowing it from our children."
don't fall in either/or (the tyanny of or). need the harmony of "and"
take movements to create action
4 levers to pull on:
1) innovation 2) policy 3)activist 4)investing



Getting Started
We created a protoype for users to upload a zipped folder with an image to measure its carbon footprint. The output will be a dashboard reporting the emissions statistics and further analysis. You can run the demo app with:
$ streamlit run app.py

Here is a demonstration of the app:

Data Sourcing & Processing
To prototype our idea, we took timelapsed deforestation images from Google Earth Engine of Rondonia, Brazil, Nuflo de Chavez, Brazil, Toliara annd Saint Augustin, Madagascar, and Olam Farm in Nigeria. We strived for geographic diveristy and looked for changes in sustainable practices over time. 

we then used a pre-trained ResNNet-50 modelto generate numerical values for measuring cover crop analysis, conservation tillage verififcation, and an analysis on vegetaton & livestock indigenous to the area of the inputted image. 


Further Improvements
Use more sophisticated and nuanced datasets for training and testing, such as those from NASA
Further expand geographic reach and types of veegatation and livestock being analyzed
Further refine our methodoology for quantitfying carbon footprint
 



