# Import the dependencies.
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc

import pandas as pd
import datetime as dt

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

# reflect an existing database into a new model
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    """List all available api routes"""
    return(f"Welcome to my Hawaii Weather Station API<br/>"
           f"Available Routes:<br/>"
           f"/api/v1.0/precipitation<br/>"
           f"/api/v1.0/stations<br/>"
           f"/api/v1.0/tobs<br/>")

@app.route("/api/v1.0/precipitation")
# """JSONify results of precipitation analysis"""
def prcp():
    most_recent_date = session.query(Measurement.date).order_by(desc(Measurement.date)).first()
    most_recent_date_str = most_recent_date[0]
    most_recent_date_obj = dt.datetime.strptime(most_recent_date_str, "%Y-%m-%d").date()
    one_year_ago = (most_recent_date_obj - dt.timedelta(days=365))
    prcp_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()

    # Convert the SQLAlchemy Row objects to a list of dictionaries
    prcp_data_dict = []
    for row in prcp_data:
        prcp_data_dict.append({
            "date": row.date,
            "prcp": row.prcp
        })

    return(jsonify(prcp_data_dict))
    

@app.route("/api/v1.0/stations")
# """JSONify stations"""
def station():
    all_stations = session.query(Station.station).distinct().all()

    #create dictionary for all stations
    all_stations_dict = []
    for row in all_stations:
        all_stations_dict.append({
            "station": row.station
        })
    
    return(jsonify(all_stations_dict))


@app.route("/api/v1.0/tobs")
# """JSONify results of most active stations analysis"""
def tobs():
    most_recent_date = session.query(Measurement.date).order_by(desc(Measurement.date)).first()
    most_recent_date_str = most_recent_date[0]
    most_recent_date_obj = dt.datetime.strptime(most_recent_date_str, "%Y-%m-%d").date()
    one_year_ago = (most_recent_date_obj - dt.timedelta(days=365))
    results = session.query(Measurement.station, Measurement.date, Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= one_year_ago).all()
    active_station_temps_df = pd.DataFrame(results, columns=['station','date','tobs'])

    #create dictionary for most active station analysis
    most_active_dict = []
    for index, row in active_station_temps_df.iterrows():
        most_active_dict.append({
            "station": row['station'],
            "date": row['date'],
            "tobs": row['tobs']
        })

    return(jsonify(most_active_dict))

@app.route("/api/v1.0/<start>")
def start_date (date):
    # provide code for min, max, and avg of tobs for each date


    # code for if given that date
    canonicalized = date.replace(" ", "").lower()
    for each in justice_league_members:
        search_term = character["superhero"].replace(" ", "").lower()

        if search_term == canonicalized:
            return jsonify(character)

    return jsonify({"error": f"Character with superhero {superhero} not found."}), 404


# @app.route("/api/v1.0/<start>/<end>")


if __name__ == '__main__':
    app.run(debug=True)