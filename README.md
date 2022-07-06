# Data Security and Privacy in Data Engineering

Here are some notebooks that will guide us in learning data privacy and security topics in relation to data engineering. These are included as a starting point to help you along your journey in learning Data Engineering as part of the Data Derp exercises!


## Motivation

When do we need to worry about privacy as we move data across an organization? How can we enable private-by-design pipelines? When should we get in touch with security peers and teammembers to better advise on the data we are moving, transforming and storing? 

This notebook / video aims to start approaching these questions as you learn data engineering basics. Unfortunately, there is no cookie-cutter answer, and many of these questions you will ask again and again as you deepen your knowledge and experience in data work. Let this section of your training be an open invitation to think on these principles and get to know them better via your work!

## Quickstart

1. Set up a [Databricks Account](https://github.com/data-derp/documentation/blob/master/databricks/README.md) if you don't already have one
2. [Create a cluster](https://github.com/data-derp/documentation/blob/master/databricks/setup-cluster.md) if you don't already have one

3. In your User's workspace, click import

   ![databricks-import](https://github.com/data-derp/documentation/blob/master/databricks/assets/databricks-import.png?raw=true)

4. Import the `Security and Privacy in Data Engineering Databricks.dbc` notebook using the URL method: `https://github.com/data-derp/exercise-data-security/blob/master/Security%20and%20Privacy%20in%20Data%20Engineering%20Databricks.dbc?raw=true`

5. Select your cluster
 ![databricks-select-cluster.png](https://github.com/data-derp/documentation/blob/master/databricks/assets/databricks-select-cluster.png?raw=true)
 
6. Follow along with the video.

7. Use a new notebook and convert the steps to Spark!


### Local Docker Container

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

Click on `Security and Privacy in Data Engineering.ipynb` to follow along


### Local Machine

Please utilize the included `requirements.txt` to install your requirements using `pip` (you can also do so in `conda`. The notebooks have *only* been tested with Python 3. 🙌🏻

```bash
pip install -r requirements.txt
```
It is recommended that you use [virtualenv](https://virtualenv.pypa.io/en/latest/) or [conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) when running and installing Python packages on your machine!


### Databricks

Open [Security and Privacy in Data Engineering Databricks.dbc](./Security%20and%20Privacy%20in%20Data%20Engineering%20Databricks.dbc) in [Databricks Community Edition](https://community.cloud.databricks.com/)
      ![databricks-import](./images/databricks-import.png)


## Outline


Agenda
--------

- Security and Privacy in Data Engineering (open this Notebook and follow along with the video)
- Switch to Databricks Community Edition, paid Databricks if you have one or a locally installed Spark instance
- Use the example Databricks notebook to get started, try to recreate the same steps in Spark, how would you do it?
- If you get stuck or want to compare notes, please look at the hints in the solutions folder. There is a notebook with one way to solve the same steps (see: Security and Privacy in Data Engineering - Spark Version).


Extra Materials
- Generating Example Data notebook (this should not be required to use and has additional software dependencies)


## Questions?

Questions about getting set up or the content covered in the notebooks or book? Feel free to reach out via email at: katharine (at) kjamistan (dot) com
