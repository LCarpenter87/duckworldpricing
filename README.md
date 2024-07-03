# duckworldpricing

## Introduction 

DuckWorld is a fictional duck sanctuary that sells duck feed on a dynamic pricing scale, depending on the current demand. They do this to ensure that the ducks of duck world do not become too large by being overfed. By raising prices during seasons of high demand, they reduce the number of people willing to pay. 

This project tracks the prices at DuckWorld, by calling their API. It then stores this in a SQL database, to create a history of the DuckWorld Pricing. Before displaying the DuckWorld pricing on an interactive graph in a streamlit app.


### Part One 

obtaindata.py requests the current pricing from the duckworld API, as well as requesting the current date and time from the server running the python script. It then stores this in the main.duckworld table.

obtaindata.py sits on the job server, running on a CRON schedule that executes it every 15 minutes. 

### Part Two 

The Streamlit application reads from the database and displays the latest duckworld data.
