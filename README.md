## Balert :loudspeaker:

Balert is for all the lazy people (like me :bowtie: ) who don't bother to check desktop notifications. Balert 
will say it clear and loud whenever your battery status goes below a default critical level or the level decided by you! 

| Build Status |
| ------------ |
| [![Build Status](https://travis-ci.org/tushar-rishav/balert.svg?branch=master)](https://travis-ci.org/tushar-rishav/balert)|


### [Demo](https://cloud.githubusercontent.com/assets/7397433/9386259/47f4991a-4778-11e5-9aaa-54873acf3d31.gif)
![balert](https://cloud.githubusercontent.com/assets/7397433/9386259/47f4991a-4778-11e5-9aaa-54873acf3d31.gif)


### Installation

```sh
	python setup.py install
```
After installation is done successfully, run any combinations of below command in your terminal once for initial setup and then we are done! If you want to use the default setup then just run  ``` balert ``` in terminal. 

#####Default config:
	language: English
	rate    : 150
	charge  : 20 (in percentage)
    msg     : ""
    vol     : 1.0

### Usage

##### Set language
To set the language eg. hindi, english , tamil. Default one is english
```sh

balert -l hindi

```

##### Set rate of speaking
```sh
balert -r 100

```

##### Set your custom alert message
```sh

balert -m "Delta is the state of mind"

```

##### Set custom charge level. 
If the battery level is below this critical level then it will give voice alert

```sh
balert -c 30

```
##### Get help
```sh
balert -h
```
##### Example
```sh
balert -m "Hey,Lazy dog " -c 25
```
When you run the above code, you've set "Hey,Lazy dog" as your custom message and 25 as your critical charge level.

### Contributions
Have an idea to make it better? Go ahead! I will be happy to see a pull request from you! :blush:

### License
![gpl](https://cloud.githubusercontent.com/assets/7397433/9025904/67008062-3936-11e5-8803-e5b164a0dfc0.png)
