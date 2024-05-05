# Vendor Management System

The Vendor Management System is a web application built using Django and Django REST Framework. It provides functionalities for managing vendors, tracking purchase orders, and evaluating vendor performance metrics.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Admin Interface](#admin-interface)
  - [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Contributing](#contributing)

## Features

- **Vendor Profile Management**: Create, view, update, and delete vendor profiles including name, contact details, address, and unique vendor code.
- **Purchase Order Tracking**: Create, view, update, and delete purchase orders with details such as order number, order date, delivery date, items ordered, quantity, and status.
- **Vendor Performance Evaluation**: Calculate performance metrics for vendors including on-time delivery rate, quality rating average, average response time, and fulfillment rate.
- **RESTful API**: Access data through RESTful API endpoints for integration with external systems or applications.
- **Token-based Authentication**: Secure API endpoints with token-based authentication for user authentication.

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/prajwalk-1/vendor-management-system.git](https://github.com/prajwalk-1/Vendor-Management-System-with-Performance-Metrics.git)
   cd vendor-management-system
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

### Admin Interface

1. Navigate to `http://127.0.0.1:8000/admin/` in your web browser.
2. Log in with the superuser credentials created earlier.
3. Manage vendors, purchase orders, and historical performance records through the admin interface.

### API Endpoints

## Vendor Endpoints

- **POST /api/vendors/**
  - Create a new vendor.
  - Request body should contain vendor details (name, contact_details, address, vendor_code).
  
- **GET /api/vendors/**
  - List all vendors.

- **GET /api/vendors/{vendor_id}/**
  - Retrieve details of a specific vendor.

- **PUT /api/vendors/{vendor_id}/**
  - Update details of a specific vendor.

- **DELETE /api/vendors/{vendor_id}/**
  - Delete a vendor.

## Purchase Order Endpoints

- **POST /api/purchase_orders/**
  - Create a new purchase order.
  - Request body should contain purchase order details (po_number, vendor, order_date, delivery_date, items, quantity, status, quality_rating).

- **GET /api/purchase_orders/**
  - List all purchase orders.
  - Optional query parameters: vendor (filter by vendor).

- **GET /api/purchase_orders/{po_id}/**
  - Retrieve details of a specific purchase order.

- **PUT /api/purchase_orders/{po_id}/**
  - Update details of a specific purchase order.

- **DELETE /api/purchase_orders/{po_id}/**
  - Delete a purchase order.

## Vendor Performance Endpoint

- **GET /api/vendors/{vendor_id}/performance/**
  - Retrieve the calculated performance metrics for a specific vendor.
  - Metrics include on_time_delivery_rate, quality_rating_avg, average_response_time, and fulfillment_rate.

### Authentication

- API endpoints are secured with token-based authentication.
- To obtain an authentication token:
  - Send a POST request to `/api/token/` with the superuser credentials.
  - Include the token in the Authorization header of subsequent requests: `Authorization: Token <token>`.
    
### Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests for any improvements or features you'd like to see.
