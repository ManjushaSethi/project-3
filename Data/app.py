from pymongo import MongoClient

from typing import Union

from fastapi import FastAPI

from fastapi.responses import HTMLResponse

from datetime import datetime

mongostring = 'mongodb+srv://DanielleDanis:Cheeseman82!@bootcampproject3.3roprpe.mongodb.net/?retryWrites=true&w=majority'

mongo = MongoClient(mongostring)

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>COVID-19 Vaccine Database</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    padding: 20px;
                }
                h1 {
                    color: blue;
                }
                p {
                    color: #555;
                }
                img {
                    max-width: 25%;
                    height: auto;
                    float: right;
                    margin-left: 20px;
                }
            </style>
        </head>
        <body>
            <h1>Hello, welcome to our Covid-19 Vaccine Database!</h1>
            <img src="https://team.georgia.gov/wp-content/uploads/2021/02/COVID-Vaccine-2048x1365.jpg" alt="Vaccine Image">
            <p>Please use the following routes for more information:</p>
            <ul>
                <li><strong>/vaccines</strong> - General COVID-19 Vaccine Data</li>
                <li><strong>/vaccines/[Your State Here]</strong> - Data for a specific U.S. state</li>
                <li><strong>/vaccines?start_date=[YYYY-MM-DD]</strong> - Data after a specified date</li>
                <li><strong>/vaccines?end_date=[YYYY-MM-DD]</strong> - Data before a specified date</li>
                <li><strong>/vaccines?start_date=[YYYY-MM-DD]&end_date=[YYYY-MM-DD]</strong> - Data between two specified dates</li>
            </ul>
            <h3>Be sure to capitalize the first letter of the state you are searching for</h3>
            <p> To search for Covid-19 data in Alabama, for example, use <strong> /vaccines/Alabama</strong></p>
            <p> If you want to search between two dates in Alabama, for example, use <strong> /vaccines/Alabama?start_date=2021-01-12&end_date=2021-02-12</strong></p>
            
        
        </body>
    </html>
    """
    # return ('Hello, welcome to our Covid-19 Vaccine Database!',
            
    #         'Please use route /vaccines for more information about COVID-19 Data',
            
    #         'To search for data in a specific US state, use /vaccines/[Your State Here]',

    #         'To search for a range of data after a specified date, use /vaccines?start_date=[YYYY-MM-DD]',
            
    #         'To search for a range of data before a specified date, use /vaccines?end_date=[YYYY-MM-DD]',

    #         'To search for a range of data between two specified dates, use /vaccines?start_date=[YYYY-MM-DD]&end_date=[YYYY-MM-DD]',
            
    #         'To search for a range of data after a specified date in any particular US State, use /vaccines/[Your State Here]?start_date=[YYYY-MM-DD]',
            
    #         'To search for a range of data before a specified date, use /vaccines/[Your State Here]?end_date=[YYYY-MM-DD]',

    #         'To search for a range of data between two specified dates, use /vaccines/[Your State Here]?start_date=[YYYY-MM-DD]&end_date=[YYYY-MM-DD]',

    #         "Be sure to capitalize the first letter of the state you are searching for",
            
    #         "For example: /vaccines/Alabama or /vaccines/New York State"


    #         )


@app.get("/vaccines")
def read_item(start_date: Union[str, None] = '2019-01-01', end_date: Union[str, None] = '2024-01-01' ):
    db = mongo.COVID19_DB
    s_date = datetime.strptime(start_date,'%Y-%m-%d')
    e_date = datetime.strptime(end_date,'%Y-%m-%d')
    query = {}
    fields = {'state':1, '_id':0,'date':1, 'total_vaccinations':1, 'total_distributed':1,'people_vaccinated':1,'total_vaccinations_per_hundred':1,'people_vaccinated_per_hundred':1,'distributed_per_hundred':1,'inpatient_beds_used_covid':1, 'total_adult_patients_hospitalizated_confirmed_covid':1,'total_pediatric_patients_hospitalized_confirmed_covid':1,'previous_day_admission_adult_covid_confirmed_20-29':1,
'previous_day_admission_adult_covid_confirmed_30-39':1, 'previous_day_admission_adult_covid_confirmed_40-49':1,'previous_day_admission_adult_covid_confirmed_50-59':1,'previous_day_admission_adult_covid_confirmed_60-69':1, 'previous_day_admission_adult_covid_confirmed_70-79':1, 'previous_day_admission_adult_covid_confirmed_80+':1, 'deaths_covid':1,  }
    return list(db.Vaccine_Data.find(query,fields))

@app.get("/vaccines/{state}")
def read_item(state: str, start_date: Union[str, None] = '2019-01-01', end_date: Union[str, None] = '2024-01-01' ):
    db = mongo.COVID19_DB
    s_date = datetime.strptime(start_date,'%Y-%m-%d')
    e_date = datetime.strptime(end_date,'%Y-%m-%d')
    query = {'state':state, 'date':{'$gte':s_date, '$lte': e_date}}
    fields = {'state':1, '_id':0,'date':1, 'total_vaccinations':1, 'total_distributed':1,'people_vaccinated':1,'total_vaccinations_per_hundred':1,'people_vaccinated_per_hundred':1,'distributed_per_hundred':1,'inpatient_beds_used_covid':1, 'total_adult_patients_hospitalizated_confirmed_covid':1,'total_pediatric_patients_hospitalized_confirmed_covid':1,'previous_day_admission_adult_covid_confirmed_20-29':1,
'previous_day_admission_adult_covid_confirmed_30-39':1, 'previous_day_admission_adult_covid_confirmed_40-49':1,'previous_day_admission_adult_covid_confirmed_50-59':1,'previous_day_admission_adult_covid_confirmed_60-69':1, 'previous_day_admission_adult_covid_confirmed_70-79':1, 'previous_day_admission_adult_covid_confirmed_80+':1, 'deaths_covid':1,  }
    return list(db.Vaccine_Data.find(query,fields))