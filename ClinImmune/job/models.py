from mongoengine import *
from datetime import datetime

connect('jobdb')

EPITOPE_ANALYSIS = '1'
    
JOB_TYPE_CHOICES = (
    (EPITOPE_ANALYSIS, 'Epitope Analysis')
)

GROUP_COUNT = (
    1,
    2,
    3,
    4
)

RACE_CHOICS = (
    ('Un','Unknown')
)

class Job(Document):
    """
    Defines a job schema for mongoengine defined as follows
    {
        "user": "/users/1",

        "university": "UC Denver",
        "Job Type": "1",
        "created": "05-04-2013",
        "finished": "True",
        "patients": [
            {
                "subject_id": 332245,
                "control": True,
                "Race": "IT",
                "alleles": [
                    "DPB1*01:01",
                    "DPB1*02:01",
                    "DRB1*02:03",
                    ...
                ]
            },
            {
            ...
            }
        ],
        "return_data": [
            {
                "module": "ARQL",
                "positions": [
                    "57",
                    "70",
                    "84",
                    "85"
                ],
                "affected": "1000",
                "control": "900",
                "p-value": "1.625e-64",
                "p-adjusted": "2.948e-57"
            },
        ],
    }
    """
    
    user = URLField(required=False) # Hyperlink to user
    university = StringField(required=True)
    job_type = StringField(max_length=2, choices=JOB_TYPE_CHOICES)
    created = DateTimeField(default=datetime.now)
    finished = BooleanField(default=False)
    patients = ListField(EmbeddedDocumentField(Patient))
    return_data = ListField(EmbeddedDocumentField(AnalysisData))
    
class Patient(EmbeddedDocument):
    subject_id = IntField(required=True)
    control = BooleanField(required=True)
    race = StringField(required=True)
    alleles = ListField(StringField())

class AnalysisData(EmbeddedDocument):
    module = StringField()
    positions = ListField(IntField())
    affected = IntField()
    control = IntField()
    p-value = FloatField()
    p-adjusted = FloatField()
    
