## balert

balert is for all the lazy people like me who don't bother to check desktop notifications. balert 
will say it clear and loud whenever your battery status goes below critical level or the level decided by you! 

Makes life simple! :wink:

### Installation

```sh
	python setup.py install
```
After installation is done successfully, run any combinations of below command in your terminal once for initial setup and then we are done! If you want to use the default setup then just run  ```sh balert ``` in terminal. 

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

##### Set custom alert message
```sh

balert -m "Delta is the state of mind"

```

##### Set custom charge level. 
If the battery level is below this critical level then it will give voice alert

```sh
balert -c 30

```
### TO DO
- Add the script as startup application


### License
![gpl](https://cloud.githubusercontent.com/assets/7397433/9025904/67008062-3936-11e5-8803-e5b164a0dfc0.png)
