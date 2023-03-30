Project Description:

The project is to create an ecommerce API using Django Rest Framework (DRF) that allows users to browse and buy products online. The API should be secure and allow users to authenticate using tokens, and manage categories and products.

Key Features:

	1-User authentication using tokens
	2-Category management system
	3-Product catalog with search and filter functionality
	4-User management system
	5-Checkout functionality
	
Requirements:

	1-The project should be built using Django Rest Framework (DRF) and use PostgreSQL database.
	2 User authentication should be implemented using token-based authentication, and the tokens should expire after an hour.
	3-Users should be able to browse products by categories and search for specific products using keywords.
	4- Categories should be managed through DRF's API endpoints.
	5- Products should be able to be added, edited and deleted through DRF's API endpoints.
	6- Users should be able to create an account, update their profile, and view their order history through DRF's API endpoints.
	7 -The checkout system should collect user information, shipping details, and payment information through DRF's API endpoints.



Deliverables:

	Source code and project documentation.
	A working demo of the API hosted on a live server OR (video on local environment in case you have not a host)
	User manual and technical documentation.
	Presentation of the project to the evaluation committee. (not required based on the need)

---------------------------------------------------------------------------------------------------------

This is a high-level overview of how i created  ecommerce API using:
Django Rest Framework (DRF), PostgreSQL database, and token-based authentication.
We'll go through the main steps involved in creating this project. 

### Step 1: Set up the project environment

1. Install Django, DRF, PostgreSQL, and Simple JWT:
2. Create a new Django project:
3. Navigate to the project folder and create a new app:
4. Configure the PostgreSQL database and DRF in `ecommerce/settings.py`:
5. Migrate the database:

### Step 2: Implement User Authentication

1. Create a custom user model in `api/models.py` with the required fields.
2. Configure JWT authentication in `ecommerce/settings.py`:
3. Create serializers, views, and URLs for user registration and authentication in `api` app.

### Step 3: Implement Category Management

1. Create a Category model in `api/models.py`.
2. Create a Category serializer in `api/serializers.py`.
3. Create Category viewsets in `api/views.py`.
4. Add Category URLs in `api/urls.py`.

### Step 4: Implement Product Catalog

1. Create a Product model in `api/models.py`.
2. Create a Product serializer in `api/serializers.py`.
3. Create Product viewsets in `api/views.py` with search and filter functionality.
4. Add Product URLs in `api/urls.py`.

### Step 5: Implement User Management

1. Create serializers and viewsets for user profiles and order history in `api` app.
2. Add necessary URLs in `api/urls.py`.

### Step 6: Implement Checkout Functionality

1. Create models for Orders, OrderItems, and ShippingInfo in `api/models.py`.
2. Create serializers for Orders, OrderItems, and ShippingInfo in `api/serializers.py`.
3. Create viewsets for Orders, OrderItems, and ShippingInfo in `api/views.py`.
4. Add necessary URLs in `api/urls.py`.

### Step 7: Testing and Deployment

1. Test your API endpoints using tools like Postman or by writing test cases.
2. Deploy your application to a server (e.g., Heroku, AWS, or Digital Ocean).