# API 


## locathost:8000/patient/John 
    
todo: see if we can return just the object and not a list 
    [
        {
            "id": 6,
            "username": "John",
            "email": "John@theYoohoo.com",
            "bp_measurements": []
        }
    ]
## localhost:8000/patient/all get 

todo: this will only available to administrators 


    [
        {
            "id": 2,
            "username": "max",
            "email": "max3323l@gmail.com",
            "bp_measurements": [
            "BP: 123/142 Pulse:83   2024-08-09 16:14",
            "BP: 123/141 Pulse:83   2024-08-10 16:14"
            ]
        },
        {
            "id": 3,
            "username": "amdrew",
            "email": "andrewkorell@gmail.com",
            "bp_measurements": [
            "BP: 123/141 Pulse:83   2024-08-10 16:14",
            "BP: 123/141 Pulse:83   2024-08-10 16:14"
            ]
        },
        {
            "id": 4,
            "username": "mark",
            "email": "mark@thefall.com",
            "bp_measurements": []
        },
        {
            "id": 5,
            "username": "mike",
            "email": "mike@thefall.com",
            "bp_measurements": []
        }
    ]

## localhost:8000/patient/John post 

the '/John can be any string 

body = { "username": "John, "email": "John@theYoohoo.com" }
{
  "id": 6,
  "username": "John",
  "email": "John@theYoohoo.com",
  "bp_measurements": []
}

## localhost:80000/bpdata get 


todo: this needs to be filtered by patient username

    [
        {
            "systolic": 124,
            "diastolic": 145,
            "pulse": 81,
            "patient": 1,
            "measDateTime": "2024-08-09T16:13:49.993000Z",
            "note": "test"
        },
        {
            "systolic": 123,
            "diastolic": 142,
            "pulse": 83,
            "patient": 1,
            "measDateTime": "2024-08-09T16:14:49.993000Z",
            "note": "test"
        }
    ]