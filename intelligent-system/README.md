# Intelligent System for Extracting and Analyzing Information from PDFs and the Internet

## Overview
This project aims to develop an intelligent system that efficiently extracts and analyzes information from PDF documents and the internet. The system integrates advanced natural language processing (NLP) capabilities to provide insights through sentiment analysis and question answering.

## Objectives
- Extract text from PDF documents.
- Fetch and parse data from the internet.
- Perform sentiment analysis and question answering using NLP models.
- Provide a user-friendly interface for interaction.

## Project Structure
The project is divided into two main components: **backend** and **frontend**.

### Backend
- **app.py**: Main entry point for the backend service, initializing the Flask application and setting up routes.
- **requirements.txt**: Lists dependencies required for the backend service.
- **services/**: Contains modules for PDF extraction, web scraping, and NLP tasks.
  - **pdf_extraction.py**: Functions for extracting text from PDFs.
  - **web_scraping.py**: Functions for fetching and parsing web data.
  - **nlp_tasks.py**: Functions for sentiment analysis and question answering.
- **tests/**: Contains unit tests for the services.
  - **test_pdf_extraction.py**: Tests for PDF extraction functions.
  - **test_web_scraping.py**: Tests for web scraping functions.
  - **test_nlp_tasks.py**: Tests for NLP tasks.

### Frontend
- **public/index.html**: Main HTML file for the frontend application.
- **src/**: Contains the React application components.
  - **App.js**: Main component for setting up routing.
  - **components/**: Individual components for PDF upload, web scraping, and displaying NLP results.
  - **styles/App.css**: CSS styles for the frontend application.
- **package.json**: Configuration file for npm.

## Setup Instructions
1. **Backend Setup**:
   - Navigate to the `backend` directory.
   - Install dependencies using `pip install -r requirements.txt`.
   - Run the backend service using `python app.py`.

2. **Frontend Setup**:
   - Navigate to the `frontend` directory.
   - Install dependencies using `npm install`.
   - Start the frontend application using `npm start`.

## Usage
- Users can upload PDF documents for text extraction.
- Users can input URLs for web scraping.
- Users can perform sentiment analysis and ask questions based on the extracted data.

## Conclusion
This intelligent system provides a comprehensive solution for extracting and analyzing information from diverse sources, enhancing the accuracy and context-awareness of NLP tasks.