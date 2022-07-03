
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

We recommend using [virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/) or [conda environments](https://conda.io/docs/user-guide/tasks/manage-environments.html). 
