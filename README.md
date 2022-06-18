# Analyzing the Effects of Agriculture on Deforestation for a Better Farm-to-Table Strategy
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
* To curate a tailored, sustainable agricultural practice you must measure your carbon footprint, analyze your emissions, and execute on meaninful reductions
<img width="718" alt="Screen Shot 2022-06-15 at 8 37 06 AM" src="https://user-images.githubusercontent.com/78511177/173828466-599e40a6-20a0-4cc5-9f31-ad59d3a96ea0.png">
Source: Climate Tech VC

Problem Statement
-----------------
* The objective of the project is to detect deforestation risk by labeling satellite images with atmospheric conditions and various classes of land cover/land use. The project specifically addresses Kaggle competition - Planet: Understanding the Amazon from Space. 

* Generally, stakeholders are unaware to what degree their organization is contributing to greenhouse gases. By providing data, stakeholders can better choose amongst the 4 levers they can pull on to reduce one's own carbon footprint: 
<br> 1) innovation
<br> 2) policy 
<br> 3) activism 
<br> 4) investing 

Getting Started
---------------
<br>**Deep Learning Approach 1 ResNet-18**:
* This project requires runs on Google Colab, and a Kaggle account
* Prior to running main.ipynb, set up the Kaggle API and download kaggle.json follwing these instructions: https://github.com/Kaggle/kaggle-api

* Run main.ipynb on Colab, using GPU

* Upload kaggle.json to the notebook when prompted

<br>**Deep Learning Approach 2 ResNet-50**:
<br> 
* Source: FSDL Deforestation Detection
[here](https://github.com/karthikraja95/fsdl_deforestation_detection)
                

1) Run the program:


        $ python run scripts/main.py

Project Structure
-----------------
<br>**Deep Learning Approaches 1 & 2**:
* Since the training dataset is large, >40,000 images, in lieu of downloading the entire dataset onto the project directory, we downloaded them at runtime to Colab 

<br>**Deep Learning Approach 1 ResNet-18**:
* Setup occurs in the main.ipynb notebook instead of a setup python script

* We use a deep learning approach: ResNet18 model with PyTorch DataLoaders
* We use a pretrained ResNet-18 model, and add our deforestation labels in the fully connected layer.
* Our project is structured as follows:
* **Main.ipynb** - Main notebook file to be run on colab. Requires GPU.
* **Data (colab)** - Since our training dataset is large, we create the data directory in Colab at runtime. This contains our training and validation sets.
* **Test-data** - Contains the screenshots as test data 
* **models/resnet18.pt**  - we saved the full trained model.
* Since we decided to use Colab Pro to access GPU for our model, our project can be run entirely from the main.ibynb without the use of any scripts.


Data Sourcing & Processing
--------------------------
#### Training Dataset
* Our training dataset is taken from Kaggle's Understanding the Amazon from Space. It is a multilabel dataset to guage human impact in the Amazon. The 17 general labels are: agriculture, artisinal_mine, bare_ground, blooming, blow_down, clear, cloudy, conventional_mine, cultivation, habitation, haze, partly_cloudy, primary, road, selective_logging, slash_burn, and water.
* The following steps were done to process and prepare the data for modeling:

<br>  1) Select the 7 labels most indicative of deforestation - agriculture, slash-burn, habitation, selective-logging, artisinal_mine, conventional_mine, cultivation <br>
<br>  2) Create two classes - 'deforested' and 'conserved'. An image is classified as 'deforested' when any of the 7 deforestation labels are present. Otherwise it is classified as conserved <br>
<br>  3) Split the dataset into an 80-20 training-validation split <br>
<br>  4) Place the images in their appropriate class directories 


#### Test Dataset
* Satellite images collected from Google Earth Engine of three naturally deforested areas were used - Nuflo de Chavez, Brazil, Rondonia, Brazil, and Toliara and Saint Augustin, Madagascar
* Timelapsed images of these locations were taken from 1985, 1990, 1995, 2000, 2005, 2010, 2015, and 2020 to see how the area has deforested over time

        
Modeling Details
----------------
* Used a **ResNet-18** pretrained model to train the training data, batch size = 128, over 9 epochs
* Used a Cross Entropy Loss function and stochastic gradient descent
* Transfer learning on the ResNet-18 model to train our data and validate on the validation set achieved a training accuracy of 0.8905 and a validation     accuracy of 0.8797

Non-DL Discussion
---------------
* Non-DL Methods, such as, Logistic Regression assume linearity between the dependent variable and the independent variables
* Linearly separable data is rarely found in real-world scenarios
* Non-deep learning is not applicable for this project because satellite images are very pixelated and hard to fully capture 
* Neural networks are more capable of capturing finer details needed for analyzing carbon emissions for example


Model Evaluation & Results
----------------------------
After training the model, we ran the test dataset through our trained model, and we get two outputs for each image:
* probs: the probability that the image is deforested or conserved
* preds: binary classification - 0 for no deforestation detected

Results on Training Data:
<br> 
* Using transfer learning on the Resnet-18 model to train our data and validate on the validation set, we achieved a training accuracy of 0.8905 and a validation accuracy of 0.8797

<img width="629" alt="Screen Shot 2022-06-17 at 8 17 15 PM" src="https://user-images.githubusercontent.com/78511177/174414612-cffb8d76-5d2c-410a-8b63-b9dbdcb5748b.png">

Results on Test Data:
<img width="946" alt="Screen Shot 2022-06-17 at 8 19 23 PM" src="https://user-images.githubusercontent.com/78511177/174414700-9b87963c-514a-429e-84df-74fd6eb93cb7.png">

Future Work
--------------------


* Given that access to labeled satellite imagery is very limited to train and test a model, with access to a more robust database, the project can go one step further by creating a data flywheel that takes imagery from areas undergoing deforestation and water pollution across the globe as input into a Streamlit app. The output is a dashboard of emissions analytics for any user, especially farmers and fisherman, with low-cost internet access to quanitfy their own carbon footprint. Current products are only for corporate or government agenices. Some examples of data the could be collected from a given image are: 
        <br>
        <br> 1) cover crop analysis - utilization of satellite imagery to determine how many months a field remains green throughout the year
        <br>
        <br> 2) conservation tillage verification - monitor soil disturbance causing the soil's carbon to              be released into the atmosphere
        <br>
        <br> 3) from the geopgraphic region, you can analyze the vegetation, livestock (red meat), poultry (white meat),            and seafood unique to the area to study crop yield, quality, and plant resistance to abiotic and biotic              stresses. 
      
* Here are two examples of a dashboard displaying carbon analytics to help organizations create more sustainable solutions:
        <br>
        <br> 1) Watershed: a company that provides a dashboard for corporate customers' emission analytics to measure, reduce, remove, and report its own carbon footprint:


https://user-images.githubusercontent.com/78511177/173738976-b33bac38-8989-45a0-a12c-450516b2a8e3.mov

      
   <br> 2) ClimateTrace: like Watershed, aims to provide radical transaprency for global emissions by helping to detect where carbon pollution is coming from by country and by industry using satellite images. The purpose is to create a a global inventory of emissions to help policymakers, industry operators and consumers unknowingly investing in high-polluting organizations:
   
   
   
https://user-images.githubusercontent.com/78511177/173741059-b3f26f63-37fd-4fab-ad88-16a7ea6f8aed.mov


* Use more sophisticated and nuanced datasets for training and testing, such as those from NASA
* Further expand geographic reach and types of vegatation and livestock being analyzed
* Further refine our methodology for quantitfying carbon footprint
* Collobarate with industry & academia. Examples include:
<img width="711" alt="Screen Shot 2022-06-15 at 11 53 59 AM" src="https://user-images.githubusercontent.com/78511177/173871680-f3b0c7bf-c93f-47f5-b75d-6345a699a789.png">


Conclusion
----------
* Helping farmers adapt to climate change is a way to combat poverty. No matter how small or large our contribution is to the cleantech revolution, we all must strive to mitigate climate's deleterious effects
* About two-thirds of those living in poverty work in agriculture, often relying on the food they grow to feed their families
* A warmer world will be problematic for relatively well-off farmers in America and Europe, but potentially deadly for low-income farmers in Africa and Asia. 
* It is our duty to provide technology and analytics to better serve the most vulnerable populations
Source: Gates Notes

Additional Resources
--------------------
* Gates Notes
* How to Avoid a Climate Disaster by Bill Gates
* Speed and Scale by John Doerr & Ryan Panchadsaram
* Climate TRACE/Google/Sentinel-2 Geo-Spatial Classification Model: [here](https://colab.research.google.com/github/GoogleCloudPlatform/python-docs-samples/blob/main/people-and-planet-ai/geospatial-classification/README.ipynb#scrollTo=3547aec6)

Notebooks
---------
1. ResNet-18 Deep Learning Model: [here](https://colab.research.google.com/drive/1RKdO2bWmNe9sy4iH8REQjJfXCrdrxcrr#scrollTo=bRppvh0FRklm)
2. ResNet-50 Deep Learning Model: [here](https://colab.research.google.com/drive/1M9Y7eJZacFHujo8vmwYcCdr3JKlE4G1Q#scrollTo=M2r5Wun4lHXv)


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



