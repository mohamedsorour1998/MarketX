# MarketX: Cloud Full Stack Ecommerce Project

This project is an ecommerce API and web application built using Django, Django Rest Framework (DRF), and Angular. Users can browse and buy products online through a user-friendly interface. The API supports secure user authentication using JWT tokens stored in local storage, with custom token handling and decoding for user identification. Cross-Origin Resource Sharing (CORS) is also supported for cross-domain requests. The application is deployed on Google Cloud Platform (GCP) using Google Kubernetes Engine (GKE), and GitHub Actions is utilized for CI/CD.
SEE IT LIVE => https://www.linkedin.com/feed/update/urn:li:activity:7063481349159948289/
![Screenshot 2023-08-29 221233](https://github.com/mohamedsorour1998/MarketX/assets/110028481/bbc39a4f-6401-409b-9930-5eecade4fb0b)
![Screenshot 2023-08-29 221246](https://github.com/mohamedsorour1998/MarketX/assets/110028481/423b6ba7-9cce-4ef7-b131-62b34aac505b)
![Screenshot 2023-08-29 221328](https://github.com/mohamedsorour1998/MarketX/assets/110028481/85d16145-e422-42d5-b419-2fc7364a68a8)

## Key Features

1. User authentication using JWT tokens
   - JWT tokens are stored in local storage
   - Custom token handling and decoding for user identification
2. CORS support for cross-domain requests
3. Category management system
4. Product catalog with search and filter functionality
5. User management system
6. Checkout functionality
7. Angular-based web application for a responsive user experience
8. Deployment on GCP using GKE
9. Continuous Integration and Continuous Deployment (CI/CD) using GitHub Actions

## Requirements

1. Django
2. Django Rest Framework (DRF)
3. PostgreSQL database
4. django-cors-headers
5. Angular
6. Node.js and npm

Refer to the `README.md` files inside the backend and frontend directories for the installation and setup instructions for each part.

## API Endpoints

### Users

* List and create users: `GET, POST /users/`
* Retrieve, update, and delete a specific user: `GET, PUT, DELETE /users/<int:pk>/`
* List and create orders for a specific user: `GET, POST /users/<int:pk>/orders/`
* Retrieve, update, and delete a specific order: `GET, PUT, DELETE /users/<int:pk>/orders/<int:pk2>/`
* List and create checkouts for a specific user: `GET, POST /users/<int:pk>/orders/checkout/`

### Categories

* List and create categories: `GET, POST /categories/`
* Retrieve, update, and delete a specific category: `GET, PUT, DELETE /categories/<int:pk>/`

### Products

* List and create products, also filter them by category: `GET, POST /products/`
* Search for products by keyword: `GET /products/search/`
* Retrieve, update, and delete a specific product: `GET, PUT, DELETE /products/<int:pk>/`

### Authentication

* Obtain a JWT token pair: `POST /token/`
* Refresh a token: `POST /token/refresh/`

## Deployment on GCP using GKE

The application is deployed on Google Cloud Platform using Google Kubernetes Engine. Refer to the [official GCP documentation](https://cloud.google.com/kubernetes-engine/docs) for information on deploying applications with GKE.

## CI/CD using GitHub Actions

This project uses GitHub Actions for Continuous Integration and Continuous Deployment. The actions are defined in the `.github/workflows/` directory. Please consult the [official GitHub Actions documentation](https://docs.github.com/en/actions) for guidance on setting up and configuring GitHub Actions for your project.

## Documentation

This README serves as a user manual and technical documentation for the project. Please refer to the `README.md` files inside the backend and frontend directories for the installation and setup instructions for each part.

For further information on working with Django and DRF, consult the [Django documentation](https://docs.djangoproject.com/en/stable/) and the [Django Rest Framework documentation](https://www.django-rest-framework.org/), respectively.

For the frontend, refer to the [Angular documentation](https://angular.io/docs) for guidance on working with Angular, and the [Node.js documentation](https://nodejs.org/en/docs/) for guidance on Node.js.

For implementing JWT authentication, refer to the [Django Rest Framework SimpleJWT documentation](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/index.html) for information on working with token-based authentication.

For the `django-cors-headers` library, consult the [official documentation](https://github.com/adamchainz/django-cors-headers#setup) for guidance on setting up CORS support.

## Contributing

If you have any suggestions, improvements, or bugs to report, please open an issue or submit a pull request. All contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
