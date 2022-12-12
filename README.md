># Bachelor Thesis Project

This project was made for my Bachelor thesis.

**Name**: 

**Description**:



The project simulates the creation of IoT devices. 
X devices send data to an api endpoint. The data that is gathered in json format will be used by a main model and they will be preproccessed before the trainning.
An addition endpoint will store addition entries that can be used 
for model testing purposes.




## Libraries

| [Django API](https://github.com/johnt1838/bachelor-thesis/tree/main/API/dataApi) | Command | Description |
| ----------- | ----------- | ----------- |
| Django | ```pip install django``` | Django is a high-level Python web framework that enables rapid development of secure and maintainable websites |
| Django Rest Framework | ```pip install djangorestframework``` |


| [Device Module](https://github.com/johnt1838/bachelor-thesis/tree/main/IOT_DEVICESTOAPI_SIM) | Command | Description |
| ----------- | ----------- |----------- |
| Pandas  | ```pip install pandas``` | pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.|
| Threading | ```pip install thread6``` | A thread is a separate flow of execution. This is used for the simultaneous device execution|
| Requests | ```pip install requests``` | The requests library is the de facto standard for making HTTP requests in Python|
| Logging | ```pip install logging``` | |



| [Server Module](https://github.com/johnt1838/bachelor-thesis/tree/main/SERVER_MODEL_ML) | Command | Description |
| ----------- | ----------- |-----------|
| Pandas  | ```pip install pandas``` | pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the Python programming language.|
| Sklearn  | ```pip install sklearn``` | Scikit-learn is probably the most useful library for machine learning in Python. The sklearn library contains a lot of efficient tools for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction| 
| Requests | ```pip install requests``` |The requests library is the de facto standard for making HTTP requests in Python | 

# Architecture (Greek)
## 1. General Architecture 
![General Architecture Image](/architecture/general_architecure_diagram_thesis.drawio.png)

## 2. IoT devices Architecture 
![IoT devices Architecture ](/architecture/IOTtier_pp.drawio.png)

## 3. Server Architecture 
![Server Architecture](/architecture/eksipiretitisServerPP.drawio.png)

## 4. Machine Learning Model Architecture
![Machine Learning Model Architecture](/architecture/ML%20MODELS.drawio.png)


