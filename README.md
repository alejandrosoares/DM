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
* [dm-recommendations](https://github.com/alejandrosoares/dm-recommendations)

