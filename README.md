# Carbon Farming: A Farm-to-Table Strategy for Food & Energy Security
![image](https://user-images.githubusercontent.com/78511177/173726171-2d866975-a9d4-4fa9-8b8b-2bbc7cb1c632.png)


AIPI 540 Deep Learning Applications
<br> Computer Vision Module 
<br> Project by: Diarra Bell, Sakura Anning Yoshihara, and Derrick Adam

Motivation
----------
"Control oil and you control nations; control food and you control people." - Henry Kissinger
<br>
<br> About two-thirds of those living in poverty work in agriculture. (Gates Notes) The rich and middle-income countries are the biggest contributors to climate climage, yet the poorest are the most adversely affected. The project aims to make equipping the poorest farmers with modern technology a global humanitarian effort since increasing temperatures affects these groups more than others. 
<br>
* As the population grows, so will the demand for food
* Food and nature emit 14 out of 59 Gigatons of carbon, so sustainable food systems and agricultural practices are needed to adjust what we eat, how we grow our food, and even waste it, and protect nature 
* To curate a tailored, sustainable agricultural practice youe must measure your carbon footprint, analyze your emissions, and execute on meaninful reductions
<img width="718" alt="Screen Shot 2022-06-15 at 8 37 06 AM" src="https://user-images.githubusercontent.com/78511177/173828466-599e40a6-20a0-4cc5-9f31-ad59d3a96ea0.png">



Here are two examples of a dashboard displaying carbon analytics to help organizations create more sustainable solutions:

- Watershed: a company that provides a dashboard for corporate customers' emission analytics to measure, reduce, remove, and report its own carbon footprint:


https://user-images.githubusercontent.com/78511177/173738976-b33bac38-8989-45a0-a12c-450516b2a8e3.mov



- ClimateTrace: like Watershed, aims to provide radical transaprency for global emissions by helping to detect where carbon pollution is coming from by country and by industry using satellite images. The purpose is to create a a global inventory of emissions to help policymakers, industry operators and consumers unknowingly investing in high-polluting organizations:



https://user-images.githubusercontent.com/78511177/173741059-b3f26f63-37fd-4fab-ad88-16a7ea6f8aed.mov


        
        














Problem Statement
-----------------
* The objective of the project is to detect deforestation risk by labeling satellite images with atmospheric conditions and various classes of land cover/land use. The porject specifically addresses Kaggle competition - Planet: Understanding the Amazon from Space. Generally, stakeholders are unaware to what degree their organization is contributing to greehouse gases. By providing data, stakeholders can better choose amongst the 4 levers they can pull on to reduce one's own carbon footprint: 
<br> 1) innovation 
<br> 2) policy 
<br> 3) activism 
<br> 4) investing 

Getting Started
---------------
1) Install the requirements to run the python files:
        
        $ pip install -r requirements.txt
        
2) Run the program:


        $ python3 scripts/carbon_farming.py

3) Run the demo app:

        $ streamlit run app.py
        
A demo of how the app works:


Project Structure
-----------------

Data Sourcing & Processing
--------------------------
Finding datasets with binary classification of deforestation and non-deforestation is very difficult, so the closest dataset to what we aimed to achieve is Kaggle's Understanding the Amazon from Space. It is a multilabel dataset to guage human impact in the Amazon. The 17 general labels are: agriculture, artisinal_mine, bare_ground, blooming, blow_down, clear, cloudy, conventional_mine, cultivation, habitation, haze, partly_cloudy, primary, road, selective_logging, slash_burn, and water.
        

Modeling Details
----------------

Model Evaluation & Results
----------------------------
<img width="610" alt="Screen Shot 2022-06-15 at 12 13 05 AM" src="https://user-images.githubusercontent.com/78511177/173735335-35c3d51d-39fe-421e-9553-15c47cf6d1fe.png">


Further Improvements
--------------------
* Given that access to labeled satellite imagery is very limited to train and test a model, with access to a robust database, the project can go one step further by creating a data flywheel by taking imagery from areas undergoing deforestation and water pollution across the globe to measure its carbon footprint. From a given image you can 
        <br> 1) extract cover crop analysis 
        <br> 2) perform conservation tillage verififcation which monitors soil disturbance causing the soil's carbon to              be released into the atmosphere. 
        <br> 3) from the geopgraphic region, you can analyze the vegetation, livestock (red meat), poultry (white meat),            and seafood unique to the area to study crop yield, quality, and plant resistance to abiotic and biotic              stresses. 
* Use more sophisticated and nuanced datasets for training and testing, such as those from NASA
* Further expand geographic reach and types of veegatation and livestock being analyzed
* Further refine our methodoology for quantitfying carbon footprint
* Collobarate with industry & academia. Examples include:
<img width="711" alt="Screen Shot 2022-06-15 at 11 53 59 AM" src="https://user-images.githubusercontent.com/78511177/173871680-f3b0c7bf-c93f-47f5-b75d-6345a699a789.png">
 <br> Watershed: Software platform for running a climate program
 <br> ClimateTrace: Database to collect and share greenhouse gas emissions from anthropogenic activities to facilitate climate action
 <br> FarmBeats: Deliver internet connectivity to create precision farming to local farmers at affordale costs
 <br> John Deere: Manufactures agircultural machinery
 <br> Monsanto (acquired by Bayer): World's largest seed company & major producer of pesticides and genetically modified crops
 <br> Syngenta (subsidiary of China National Chemical): Provider of agricultural science and technology, in particular seeds and pesticides
 <br> FarmShots (acquired by Syngenta): Uses satellite imagery analysis to help detect diseases, pests, and poor plant nutrition 
 <br> Corteva Argiscience (the agricultural unit of DowDuPont): Provides argonomic support and services to help increase farmer productivity and profitabilty
 <br> Satellite Imagery Providers: Sentinel-2 Europe's Earth observation satellite
 <br> Beyond Meat & Impossible Foods: plant-based meat producers
 <br> WattTime: Environmental tech nonprofit that empowers all people, companies, policymakers, and countries to slash emissions and choose cleaner energy. 
 <br> Universities pioneering research in agricultural biotechnology: Duke, Clemson, Cornell, etc. 

Conclusion
----------
Helping farmers adapt to climate change is a way to combat poverty. No matter how small or large our contribution is to the cleantech revolution, we all must strive to mititgate climate's deleterious effects. About two-thirds of those living in poverty work in agriculture, often relying on the food they grow to feed their families. A warmer world will be problematic for relatively well-off farmers in America and Europe, but potentially deadly for low-income farmers in Africa and Asia. (Gates Notes)

Notebooks
---------
1. ResNet-50 Deep Learning Model: [here](https://colab.research.google.com/drive/1M9Y7eJZacFHujo8vmwYcCdr3JKlE4G1Q#scrollTo=M2r5Wun4lHXv)
2. Logistic Regression Non-Deep Learning Model:

Additional Notes
----------------

License
-------
This project is licensed under the terms of the MIT license. See [LICENSE](https://github.com/diarrabell/Carbon-Farming/blob/main/LICENSE) 
for more details.


Citation
--------
@misc{fsdl_deforestation_detection,
  author = {Karthik Bhaskar, Andre Ferreira},
  title = {Predicting deforestation from Satellite Images},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/karthikraja95/fsdl_deforestation_detection}}
}



