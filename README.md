# Carbon Farming: A Farm-to-Table Strategy for Food & Energy Security
![image](https://user-images.githubusercontent.com/78511177/171748204-f95510ec-fe34-4cd7-bf20-9ce432bc7d79.png)

AIPI 540 Deep Learning Applications
Computer Vision Module Project by: Diarra Bell, Sakura Anning Yoshihara, and Derrick Adam

# Motivation
"Control oil and you control nations; control food and you control people." - Henry Kissinger
* As the population grows, so will the demand for food
* Food and nature emit 14 out of 59 Gigatons of carbon, so sustainable food systems and agricultural practices are needed to adjust what we eat, how we grow our food, and even waste it, and protect nature 
* To curate a tailored, sustainable agricultural practice youe must measure your carbon footprint, analyze your emissions, and execute on meaninful reductions

Here are two examples of a dashboard displaying carbon analytics to help organizations create more sustainable solutions 

The first example is from Watershed. Waterhsed is a company that provides a dashboard for corporate customers' emission analytics to measure, reduce, remove, and report its own carbon footprint:

The second example is from ClimateTrace. ClimateTrace, like Watershed, aims to provide radical transaprency for global emissions by helping to detect where carbon pollution is coming from by country and by industry using satellite images. The purpose is to create a a global inventory of emissions to help policymakers, industry operators and consumers unknowingly investing in high-polluting organizations:


        
        







# Getting Started




Here is a demonstration of the app:

Data Sourcing & Processing
To prototype our idea, we took timelapsed deforestation images from Google Earth Engine of Rondonia, Brazil, Nuflo de Chavez, Brazil, Toliara annd Saint Augustin, Madagascar, Olam Farm in Nigeria . We strived for geographic diveristy and looked for changes in sustainable practices over time. 

*Fishery Pollution

we then used a pre-trained ResNet-50 model to generate numerical values for measuring cover crop analysis, conservation tillage verififcation, and an analysis on vegetaton & livestock indigenous to the area of the inputted image. 

# Problem Statement
* The objective of the project is to address the following Kaggle competition - Planet: Understanding the Amazon from Space by labeling satellite images with atmospheric conditions and various classes of land cover/land use. Stakeholders, especially farmers and those who work outdoors, are unaware of how and to what degree their organization is contributing to greehouse gases. By providing data, stakeholders can better choose amongst the 4 levers they can pull on to reduce and be more aware of one's carbon footprint 1) innovation 2) policy 3)activist 4)investing 

# Project Structure

# Modeling Details

# Model Evaluation & Results

# Further Improvements
* Given that access to satellite imagery is very limited to train and test a model, with access to a robust database, the project can go one step further by creating a data flywheel by taking imagery from areas undergoing deforestation and water pollution across the globe to measure its carbon footprint. From a given image you can 
        1) extract cover crop analysis 
        2) perform conservation tillage verififcation which monitors soil disturbance causing the soil's carbon to              be released into the atmosphere. 
        3) from the geopgraphic region, you can analyze the vegetation, livestock (red meat), poultry (white meat),            and seafood unique to the area to study crop yield, quality, and plant resistance to abiotic and biotic              stresses. 
* Use more sophisticated and nuanced datasets for training and testing, such as those from NASA
* Further expand geographic reach and types of veegatation and livestock being analyzed
* Further refine our methodoology for quantitfying carbon footprint
* Collobarate with larger compaines, like Watershed, FarmBeats, John Deere, Bayer which acquired Mosanto (the world's largest seed company & major producer of pesticides and genetically modified crops), Syngenta (a subsidiary of China National Chemical), FarmShots (acquired by Syngenta), Corteva Argiscience (the agricultural unit of DowDuPont), satellite imagery providers, synthetic meat producers, like Beyond Meat & Impossible Foods, ClimateTrace, Wattime, and universities pioneering research in agricultural biotechnology.

# Conclusion:
Helping farmers adapt to climate change is way to combat poverty. No matter how small or large our contribution is to the cleantech revolution, we all must strive to stop mititgate climate's deleterious effects. Work done by CGIAR Climate-smart agriculture research helps smallholder farmers in the developing world. About two-thirds of those living in poverty work in agriculture, often relying on the food they grow to feed their families. A warmer world will be problematic for relatively well-off farmers in America and Europe, but potentially deadly for low-income farmers in Africa and Asia. (Gates Notes)

# Notebooks
1. ResNet-50 Deep Learning Model: [here](https://colab.research.google.com/drive/1M9Y7eJZacFHujo8vmwYcCdr3JKlE4G1Q#scrollTo=M2r5Wun4lHXv)
2. Logistic Regression Non-Deep Learning Model:


# Citations
@article{
  title={Detecting Deforestation from Satellite Images},
  author={Ferreira, Andre and Bhaskar, Bhaskar},
  journal={Towards Data Science},
  year={2021}
}



