
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

Click on `Security and Privacy in Data Engineering.ipynb` or `Security and Privacy in Data Engineering - Spark Version.ipynb`


### Local Machine
Please utilize the included `requirements.txt` to install your requirements using `pip` (you can also do so in `conda`. The notebooks have *only* been tested with Python 3. 🙌🏻
```bash
pip install -r requirements.txt
```

It is recommended that you use [virtualenv](https://virtualenv.pypa.io/en/latest/) or [conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) when running and installing Python packages on your machine!