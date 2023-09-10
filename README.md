
# ETL Pipeline for a Sales Dataset

ETL stands for “extract, transform, load,” the three interdependent processes of data integration used to pull data from one database and move it to another.








## Documentation

[Documentation of ETL Pipeline](https://docs.google.com/document/d/1q94Zltj_6kgSY3eGlf13L-RufXt7xP45CDBbU-9BvBw/edit?usp=sharing)


## Installation

Install the Requirements.txt file
```bash 
  pip install -r requirements.txt
```

Dependency-related issues and package installation, I have used Docker containers to manage the PostgreSQL database and Apache Airflow environment.

## For PostgreSQL Database Setup

Pull the image of Postgres from the DockerHub.
```bash 
  docker pull postgres
```

Create and run postgres Container.
```bash 
  docker run -d --name postgresdb -p 5432:5432 -e POSTGRES_PASSWORD=password postgres
```

To interact with the Container in Shell.
```bash 
  docker exec -it postgresdb bash
```
To connect the PostgreSQL Database in Shell.
```bash 
  psql -h localhost -U postgres
```

To check if the data is loaded in the PostgreSQL DB
```bash 
  SELECT * FROM table_name;
```

## For Apache- Airflow Setup:

Download the docker-compose.yaml of Apache-Airflow.
```bash 
  CURL 'https://airflow.apache.org/docs/apache-airflow/2.0.1/docker-compose.yaml’ -o ‘docker-compose.yaml’ 

```

Copy or Add all the scripts in the dags folder

Docker Compose command to start.
```bash 
  docker compose up  airflow-init
```

Docker Command to start the service.
```bash 
  docker compose up
```

To login the Airflow Portal
```bash 
  Open this url in http://localhost:8080 browser.
```

Login for Airflow Portal
```bash 
  By default, the username and password is airflow.
```

Docker Command to stop the service.
```bash 
  docker compose down
```


## STEPS
```bash 
  1. Download the scripts.
  2. Add all the scripts in the dags folder.
  3. Login on the Apache Airflow portal.
  4. Monitor DAG execution and review logs through the Airflow Portal.

```
## When you login on Portal on Portal, you will see all the DAGs  


## If you want to manually run the scripts.
```bash 
  python extract.py 
  python transform.py
  python load.py
```













    
