# Progressive Equity Calculator App
A simple program written in Python to explore pay-out scenarios from a progressive equity arrangement. Under "progressive equity", once an equity holder reaches the pre-set financial independence number from the earnings received from an exit, 50% of their additional equity will be re-distributed to other equity holders on a pro-rata basis.

This concept was popularized by one of the co-founders of Groupon, who reasoned that after a certain amount of money or the "financial independence threshold", a portion of the earnings from a large exit should be shared with the many employees who made huge contributions, but owned far less equity. 

The <a href=http://pe-calculator.us-west-2.elasticbeanstalk.com/>progressive equity calculator</a> is available online and explains the genesis of the project.  

### Learn More about Progressive Equity
Check out this blog post: <a href=https://medium.com/detour-dot-com/introducing-progressive-equity-f424a51ee3a4>Introducing Progressive Equity</a> and this <a href=https://medium.com/detour-dot-com/introducing-progressive-equity-f424a51ee3a4>Hacker News Thread</a> for more information on progressive equity.  

### Technlogies Used
* Python
* Flask
* Pandas
* Docker

The app was deployed on AWS Elastic Beanstalk. Blog post with the details coming soon!

### Use Docker to Run the Program

To run this program using Docker, using two simple commands:

1. Pull the image from DockerHub:

```
docker pull nadaataiyab/pe-calculator:latest
```

2. Run the app locally in the Docker container:
-p specifies the ports used on your computer and the Docker container

```
docker run -p 5000:5000 nadaataiyab/pe-calculator:latest
```


To edit the files locally and have the changes update in real time on the Docker container, mount the folder in which you saved the files when you run the Docker container using this command:

```
docker run -p [file path to the project files on your computer]:/app nadaataiyab/pe-calculator
```

### Run the program in your local environment
1. Ensure that you have installed python, flask, and pandas
2. Go to the root director of the app
3. Use the following command:
```python
python application.py
```
### Contribute!
This is an open source project. Please feel free to fork the repo and make a pull request and/or provide feedback on how to improve the app. 

