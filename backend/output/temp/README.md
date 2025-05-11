# Food Delivery App

## Overview
This is a food delivery application built with a FastAPI backend and a React frontend. The app utilizes Firebase for user authentication and Stripe for payment processing.

## Features
- User authentication with Firebase
- Browse restaurants and menus
- Add items to cart
- Secure payment processing with Stripe
- Order tracking
- Responsive design

## Tech Stack
- **Backend**: FastAPI
- **Frontend**: React
- **Authentication**: Firebase
- **Payment Processing**: Stripe
- **Database**: PostgreSQL (or any preferred database)

## Installation

### Prerequisites
- Python 3.7+
- Node.js 14+
- PostgreSQL (or preferred database)

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/food-delivery-app.git
   cd food-delivery-app/backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file and add your Firebase and Stripe credentials.

5. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd ../frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Set up environment variables:
   Create a `.env` file and add your Firebase configuration.

4. Run the React app:
   ```bash
   npm start
   ```

## Usage
- Register and log in using Firebase authentication.
- Browse available restaurants and their menus.
- Add items to your cart and proceed to checkout.
- Complete your order using Stripe for secure payments.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.