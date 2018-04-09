# Progressive Equity Calculator App
A simple program written in Python to help companies project pay-outs from a progressive equity arrangement. Under "progressive equity", once an equity holder reaches the pre-set financial independence number during an exit, 50% of their additional equity will be re-distributed to other equity holders on a pro-rata basis.

This concept was popularized by one of the co-founders of Groupon, who reasoned that after a certain amount of money or the "financial independence threshold", a portion of the earnings from a large exit should be shared with the many employees who made huge contributions, but owned far less equity. 

Check out this blog post: <a href=https://medium.com/detour-dot-com/introducing-progressive-equity-f424a51ee3a4>Introducing Progressive Equity</a> and this <a href=https://medium.com/detour-dot-com/introducing-progressive-equity-f424a51ee3a4>Hacker News Thread</a> for more information. 

You can also play with the <a href=http://pe-calculator.us-west-2.elasticbeanstalk.com/
>Progressive Equity Calculator</a> online.  
### Technlogies Used
I used Python, Flask, and Pandas to build the app and some simple HTML and CSS to render it. 




<h3>Tech Summary</h3>
This app was built with Python, Flask and Pandas. I created my own Docker image
using Ubuntu 

<h3>Use Docker to Run the Program</h3>

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


If you want to edit the files and run them on Docker container, you can mount the folder in which you saved the files when you run the Docker container.

```

docker run -p [file path to the project files on your computer]:/app nadaataiyab/pe-calculator

```
