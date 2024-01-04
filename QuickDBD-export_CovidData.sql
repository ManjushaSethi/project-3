-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Vaccine_DF" (
    "_id" VAR   NOT NULL,
    "date" DATE   NOT NULL,
    "state" VAR   NOT NULL,
    "total_vaccinations" INT   NOT NULL,
    "total_distributed" INT   NOT NULL,
    "people_vaccinated" INT   NOT NULL,
    "total_vaccinations_per_hundred" INT   NOT NULL,
    "people_vaccinated_per_hundred" INT   NOT NULL,
    "distributed_per_hundred" INT   NOT NULL,
    CONSTRAINT "pk_Vaccine_DF" PRIMARY KEY (
        "state"
     )
);

CREATE TABLE "Age_DF" (
    "_id" VAR   NOT NULL,
    "state" VAR   NOT NULL,
    "date" DATE   NOT NULL,
    "inpatient_beds_used_covid" INT   NOT NULL,
    "total_adult_patients_hospitalized_confirmed_covid" INT   NOT NULL,
    "total_pediatric_patients_hospitalized_confirmed_covid" INT   NOT NULL,
    "previous_day_admission_adult_covid_confirmed_20-29" INT   NOT NULL,
    "previous_day_admission_adult_covid_confirmed_30-39" INT   NOT NULL,
    "previous_day_admission_adult_covid_confirmed_40-49" INT   NOT NULL,
    "previous_day_admission_adult_covid_confirmed_50-59" INT   NOT NULL,
    "previous_day_admission_adult_covid_confirmed_60-69" INT   NOT NULL,
    "previous_day_admission_adult_covid_confirmed_70-79" INT   NOT NULL,
    "previous_day_admission_adult_covid_confirmed_80+" INT   NOT NULL,
    "deaths_covid" INT   NOT NULL,
    CONSTRAINT "pk_Age_DF" PRIMARY KEY (
        "state"
     )
);

ALTER TABLE "Age_DF" ADD CONSTRAINT "fk_Age_DF_state_date" FOREIGN KEY("state", "date")
REFERENCES "Vaccine_DF" ("state", "date");

