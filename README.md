# Data Security and Privacy in Data Engineering

Here are some notebooks that will guide us in learning data privacy and security topics in relation to data engineering. These are included as a starting point to help you along your journey in learning Data Engineering as part of the Data Derp exercises!

## Motivation

When do we need to worry about privacy as we move data across an organization? How can we enable private-by-design pipelines? When should we get in touch with security peers and teammembers to better advise on the data we are moving and storing? 

This notebook / video aims to start approaching these questions as you learn data engineering basics. Unfortunately, there is no cookie-cutter answer, and many of these questions you will ask again and again as you deepen your knowledge and experience with data work. Let this section of your training be an open invitation to think on these principles and get to know them better via your work!

## Quickstart

```
git clone git@github.com:data-derp/exercise-data-security.git
docker run  -p 8888:8888 -v $(pwd):/app -it ghcr.io/data-derp/dev-container:master bash
```

In the Docker container
```
cd /app
pip install -r requirements.txt
jupyter notebook --ip 0.0.0.0 --no-browser --allow-root
```
Then navigate to the `localhost` address (don't forget the token) that the juypter console spins up.

Click on `Security and Privacy in Data Engineering - Spark Version.ipynb`


## Installation
Please utilize the included `requirements.txt` to install your requirements using `pip` (you can also do so in `conda`. The notebooks have *only* been tested with Python 3. 🙌🏻

We recommend using [virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/) or [conda environments](https://conda.io/docs/user-guide/tasks/manage-environments.html). 

## Outline

Agenda
--------
- Data Security and Privacy in Data Engineering (open this and follow along with the video)
- Try the Python solutions on your own
- Switch to Databricks Community Edition or a locally installed Spark instance
- Try to recreate the same steps in Spark, how would you do it?
- Peek at hints or take a look at one approach in the Spark version of the notebook

Extra Materials
- Generating Example Data notebook (this should not be required to use and has additional software dependencies)


## Questions?

Questions about getting set up or the content covered in the notebooks or book? Feel free to reach out via email at: katharine (at) kjamistan (dot) com
