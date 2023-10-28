# DM - Product Catalog

Introducing our cutting-edge Product Catalog, a seamless blend of technology and customer-centric innovation. Elevate your business with features that go beyond the ordinary


## Features

### Product Recommendation Microservice
* Uses an own microservice [dm-recommendations](https://github.com/alejandrosoares/dm-recommendations) to obtain recommended products and improve the user experience

### Optimization
* Converts images to WEBP
* Resizes images according to screen size
* Applies some frontend techniques to improve performance
* Applies cache with redis
* Has a product search and pagination

### Chat
* Has implements real-time chat with Django channels
* Has ChatGPT implemented to answer some frequently asked questions

### Opening hours
* Has an endpoint to show the user if the business is opening now or closed, with the custom messages:
- Open now
- Closed now
- Open, closing soon
- Closed, opening soon

## CI
* Uses GitActions to run linters and tests automatically



## Installation

1. Set the next environment variables inside of .env file in ***src/*** dir:
```
    DJANGO_SECRET_KEY
    OPENAI_API_KEY
    REDIS_USER
    REDIS_PASSWORD
```

Set the next variables to use DM Recommendation Microservice:
```
    DMREC_HOST
    DMREC_CLIENT_ID
    DMREC_CLIENT_SECRET
    DMREC_USERNAME
    DMREC_PASSWORD
```

2. Inside your virtual environment:
```
    pip install requirements/dev.txt
```

3. Go to ***src/*** dir and run:
```
    python manage.py runserver
```



## Microservices
Make sure to run the next microservices before:
* [dm-recommendations](https://user-images.githubusercontent.com/48335948/277250835-24b43490-1e7f-4e86-9a75-459f5edfbac7.png)



## Screenshots
![Search](https://user-images.githubusercontent.com/48335948/277250835-24b43490-1e7f-4e86-9a75-459f5edfbac7.png)
![Opening Hours](https://user-images.githubusercontent.com/48335948/277250843-23c8b6f3-3bf6-4804-a09c-4991903d6636.png)
![Product Detail and recommendations](https://user-images.githubusercontent.com/48335948/277250845-adb42a65-2b78-4cda-923e-408c3e3f05d4.png)
