# progressive-equity-calculator
A simple program written in Python to help companies project pay-outs from a progressive equity arrangement. Under "progressive equity", once an equity holder reaches the pre-set financial independence number during an exit, 50% of their additional equity will be re-distributed to other equity holders on a pro-rata basis.

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
