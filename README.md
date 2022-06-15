# Carbon Farming: A Farm-to-Table Strategy for Food & Energy Security
![image](https://user-images.githubusercontent.com/78511177/171748204-f95510ec-fe34-4cd7-bf20-9ce432bc7d79.png)

# Motivation
"Control oil and you control nations; control food and you control people." - Henry Kissinger
* As the population grows, so will the demand for food
* Food and nature emit 14 out of 59 Gigatons of carbon, so sustainable food systems and agricultural practices are needed to adjust what we eat, how we grow our food, and even waste it, and protect nature 
* To curate a tailored, sustainable agricultural practice youe must measure your carbon footprint, analyze your emissions, and execute on meaninful reductions

Here are two examples of a dashboard displaying carbon analytics from stakeholders to create more sustainable solution for their organization. 

The first example is from Watershed. Waterhsed is a company that provides a dashboard  for corporate customers' emission analytics to measure, reduce, remove, and report its own carbbon footprint:

The second example is from ClimateTrace. ClimateTrace, like Watershed, aims to provide radical transaprency for global emissions by helping to detect where carbon pollution is coming from by country and by industry using satellite images and machine learning. Down the line it plans to publish wjere pollution arises from a particular facory, coal plant, an agricultural field, an animal farm and more. The purpose is to create a a global inventory of emissions to help policymakers, industry operators and consumers unknowingly investing in high-polluting organizations


        
        
This project aims to take imagery from areas undergoing deforestation and water pollution across the globe to measure its carbon footprint. First wemeaure the % of green land at each timestamp, 1985, 1995, 2005, 2015, and 2020 to conduct cover crop analysis. Next we measure surface roughness at each timestamp to perform conservation tillage verififcation. This monitors soil disturbance causing the soil's carbon to be released into the atmosphere. Lastly, for the geopgraphic region being analyzed, we use images of the vegetation, livestock (red meat), poultry (white meat), and seafood unique to the input area to further study crop yield, quality, and plant resistance to abiotic and biotic stresses. 

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
To prototype our idea, we took timelapsed deforestation images from Google Earth Engine of Rondonia, Brazil, Nuflo de Chavez, Brazil, Toliara annd Saint Augustin, Madagascar, Olam Farm in Nigeria . We strived for geographic diveristy and looked for changes in sustainable practices over time. 

*Fishery Pollution

we then used a pre-trained ResNet-50 model to generate numerical values for measuring cover crop analysis, conservation tillage verififcation, and an analysis on vegetaton & livestock indigenous to the area of the inputted image. 


Further Improvements
Use more sophisticated and nuanced datasets for training and testing, such as those from NASA
Further expand geographic reach and types of veegatation and livestock being analyzed
Further refine our methodoology for quantitfying carbon footprint
Can callobarate with larger compaines, like Watershed, FarmBeats, John Deere, Bayer which acquired Mosanto (the world's largest seed company & major producer of pesticides and genetically modified crops), Syngeta (a subsidiary of China National Chemical), Corteva Argiscience (the agricultural uit of DowDuPont), satellite imagery providers, synthetic meat producers, like Beyond Meat & Impossible Foods, ClimateTrace, Wattime, and universities pioneering research in agricultural biotechnology.

*Heme Analysis
*
 
 
Conclusion:
Helping farmers adapt to climate change is way to combat poverty. No matter how small or large our contribution is to the cleantech revolution, we all must strive to stop mititgate climate's deleterious effects. Work done by CGIAR Climate-smart agriculture research helps smallholder farmers in the developing world. About two-thirds of those living in poverty work in agriculture, often relying on the food they grow to feed their families. A warmer world will be problematic for relatively well-off farmers in America and Europe, but potentially deadly for low-income farmers in Africa and Asia. (Gates Notes)

Additional Resources & Further Study
Curretly, much of the world's agircultural output is dependent on weather. Having a platform that ennables access to data 24/7 can help untether agriculture output to the weather, similar to how the internent enables us to do online shopping, search, communicate with friends & family, and entertain ourselves at annytime of the day. Similarly, solar roofs and storage battery systems are slowly untethering the world's dependece on the grid.

A perfect solution for efficiently providing the energy for electricity is to install photovoltaic (PV) solar panels on the roof or next to the house. The house can get energy from the grid when there is no sun or inclement weather and feed energy back to the grid where this is allowed. 
![image](https://user-images.githubusercontent.com/78511177/172438992-2bd6b716-a21a-453e-8c10-79079c606df9.png)
Some houses are totally off the grid because connecting to the grid would be too expensive or unavailable in that area. These houses require photo voltaic (PV) panels to provide energy and batteries to store the energy for periods when there is no solar energy and/or inclement weather. When a household stores solar energy produced on site and uses that energy when solar production is less than than the energy requirements in the house, it is called “self consumption.”

The house may also be connected to the grid and return excess energy to the grid when the battery is full or during peak periods of the day when the grid is overloaded. (Forbes)

Currently, the energy grid is centralized ad beginning to become a an interconnected, yet decentralized system. When the power plat knows the demand for energy will be high at a certai day and time, "the system" can sed a signal to the inverters to start discharging energy to the grid. Curretly, the U.S. has a solar subsidy called net metering which is when the cost of the electric energy consumed from the grid is offset by the electric energy consumed by the renewable source. Inceitves like this could be implemented to help pivot towards clean agricultural practices. Grid parity and gird independence. 


"Agriculture is all about weather. It’s far less connected to the overall economy. That makes its asset returns in agriculture uncorrelated with other stock prices. Investors love that for a variety of reasons we won’t go into here.

But the reason for the uncorrelation is that food demand is very stable and we grow most of what we eat each year. Agriculture is a supply-driven business. Total soybean consumption, for instance, barely budged during the financial crisis, while U.S. auto sales plummeted. People have to eat." (Barron's)

# Notebooks
ResNet-50 Deep Learning Model: [here](https://colab.research.google.com/drive/1M9Y7eJZacFHujo8vmwYcCdr3JKlE4G1Q#scrollTo=M2r5Wun4lHXv)

# Further Improvements

# Citations
@article{


