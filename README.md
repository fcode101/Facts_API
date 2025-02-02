# Random Facts API

The Random Facts API is a simple FastAPI-based web service that provides random interesting facts on request. This API is designed for developers, educators, and curious individuals who want to access a wide range of facts programmatically.

## Features:

- **Random Fact Generation:** Returns a random fact on each request.  
- **FastAPI Framework:** Built using FastAPI for high performance and ease of use.  
- **Lightweight & Fast:** Minimal dependencies, optimized for quick responses.  
- **Simple Integration:** Easy to use in web applications, chatbots, and more.  

## API Endpoint

### Get a Random Fact

- **Endpoint:** `/random`  
- **Method:** `GET`  
- **Response:**  

```json
{
  "fact": "Bananas are berries, but strawberries are not."
}
```

## Tech Stack
 - **Backend Framework: FastAPI**
- **Programming Language: Python**
- **Server: Uvicorn (for running the FastAPI app)**
- **Data Storage: Text file or JSON (for storing facts)**



Your updated README.md file in proper Markdown format:

md
Copy
Edit
# Random Facts API

The Random Facts API is a simple FastAPI-based web service that provides random interesting facts on request. This API is designed for developers, educators, and curious individuals who want to access a wide range of facts programmatically.

## Features:

- **Random Fact Generation:** Returns a random fact on each request.  
- **FastAPI Framework:** Built using FastAPI for high performance and ease of use.  
- **Lightweight & Fast:** Minimal dependencies, optimized for quick responses.  
- **Simple Integration:** Easy to use in web applications, chatbots, and more.  

## API Endpoint

### Get a Random Fact

- **Endpoint:** `/random`  
- **Method:** `GET`  
- **Response:**  

```json
{
  "fact": "Bananas are berries, but strawberries are not."
}
```
## Tech Stack
 - **Backend Framework: FastAPI**
- **Programming Language: Python**
- **Server: Uvicorn (for running the FastAPI app)**
- **Data Storage: Text file or JSON (for storing facts)**

## Installation & Setup
```

git clone https://github.com/your-username/random-facts-api.git
```
- **Folder**
```

cd random-facts-api
```
- **Install dependencies:**
```

pip install -r requirements.txt
```
- **Run the API:**
```

uvicorn main:app --reload
```

- **Access the API at:**
```

http://127.0.0.1:8000/random
```

- **Access the Docs:**
- **Swaggy Docs:**
  ```
  
  http://127.0.0.1:8000/docs
  ```
-**Redocs Docs:**
  ```

  http://127.0.0.1:8000/redocs
  ```

  
## Deployment:
You can deploy this API using services like Render, Vercel, or AWS Lambda.

## Social Media:
- **YouTube:** **https://www.youtube.com/@F-Code101**



