👗 AI Fashion Assistant (Work in Progress)

An AI-powered fashion assistant that helps users generate outfit suggestions based on their personal wardrobe, occasion, and context (e.g., weather, mood).

Status: Work in Progress
This project is actively being developed and features are continuously being improved and expanded.

Features
1- Image-Based Clothing Description
Upload an image of a clothing item
AI extracts structured attributes:
Type
Color
Style
Season
Occasion

2- Store clothing item attributes in a local SQLite database

3- Virtual Wardrobe Management

AI Outfit Generation
Uses OpenAI models to generate outfit combinations
Selects:
1 top
1 bottom
1 outerwear (if appropriate)
1 pair of shoes
Based only on available wardrobe items

Setup
1. Clone the repository
2. Create a virtual environment
3. Install dependencies
```pip install -r requirements.txt```
4. Create .env file and pass your API key
```OPENAI_API_KEY=your_api_key```