# sqlalchemy_challenge
Challenge 10

## Challenge Outputs
This activity uses SQLAlchemy and Flask to analysis weather conditions before leaving for a trip to Honolulu, Hawaii.

### Analysis:
In Honolulu, Hawaii, the precipitation varies from 0 to 6.7 inches of rain per day between 2016-08-23 and 2017-08-23. The precipitation averages 0.18 inches of rain per day. The temperature ranges between 54-85 degrees with an average temperature of 71.66.

In conclusion, Hawaii is a lovely place to visit for their typical temperature in the 70's and mild rain chances.

### API:
The API provides the data retrieved for the analysis. Below are the available routes: 
- /api/v1.0/precipitation : precipitation analysis of the last 12 months of data
- /api/v1.0/stations : stations names
- /api/v1.0/tobs : the dates and temperature observations of the most-active station for the previous year of data
- /api/v1.0/start : returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start date
- /api/v1.0/start/end : returns a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start and end date range

## Resources
- Referenced lesson acitivies from Module 10 Advanced SQL.
- Xpert Learning Assistant was used to assist in debugging errors in coding.
