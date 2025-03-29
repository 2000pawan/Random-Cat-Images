# Random Cat Images Gallery

This is a simple **Streamlit** application that fetches and displays random cat images from **The Cat API**. It allows users to filter cats by breed and load more images dynamically.

## Features
- Fetches random cat images from **The Cat API**.
- Displays images in a **grid layout**.
- Provides a **dropdown filter** to select cat breeds.
- Includes a **Load Cats** button to refresh images.

## Installation
### Prerequisites
Ensure you have **Python 3.7+** installed on your system.

### Install Dependencies
```bash
pip install streamlit requests
```

## Usage
1. **Get an API Key** from [The Cat API](https://thecatapi.com/).
2. **Replace** `your-api-key-here` in the `app.py` file with your actual API key.
3. **Run the application:**
```bash
streamlit run app.py
```
4. Open the displayed **local URL** in your browser.

## Project Structure
```
|-- app.py  # Main Streamlit app
|-- README.md  # Documentation
```

## Screenshot
![Cat Gallery](https://via.placeholder.com/600x300?text=Cat+Gallery+Preview)

## Future Enhancements
- Add **pagination** for loading more images.
- Include a **favorite/save** feature.
- Improve UI with **better styling**.

## License
This project is licensed under the **MIT License**.

## Author
Developed by **Pawan Yadav**.

