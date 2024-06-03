[![progress-banner](https://backend.codecrafters.io/progress/http-server/fbcae4da-2b0b-4937-a75c-6ed8b1ae8e72)](https://app.codecrafters.io/users/notlelouch?r=2qF)


# Py-Ser

Py-Ser is a lightweight and simple HTTP server implemented in Python. It provides functionalities for handling HTTP requests, including serving static files, echoing content, and capturing user-agent information.

## Features

- **File Serving:** Serve static files from a specified directory.
- **Echo Endpoint:** Echo the content specified in the URL.
- **User-Agent Endpoint:** Mine blocks with proof-of-work and validate transactions for added security.
- **State Tracking:** Retrieve and display the User-Agent information from the HTTP headers.

## Getting Started

### Prerequisites

Python 3.x
No additional dependencies

### Installation

Clone the repository:

1. Clone the repository:

   ```bash
    git clone https://github.com/your-username/Py-Ser.git
    cd Py-Ser
   ```
   
2. Run the server:

  ```bash
    python main.py --directory /path/to/serve
   ```
Replace /path/to/serve with the directory you want to serve.

### Usage

Once the server is running, you can access different endpoints:

**Hello World:** 
  
  ```bash
    http://localhost:4221/
   ```

**Echo Endpoints:** 
  
  ```bash
    http://localhost:4221/](http://localhost:4221/echo/your_content_here
   ```

**User-Agent Endpoint:** 
  
  ```bash
    http://localhost:4221/user-agent
   ```

**File Serving:** 
  
  ```bash
    http://localhost:4221/your_file_name
   ```



## Contributing

Contributions are welcome! If you have ideas for improvements, new features, or bug fixes, please open an issue or submit a pull request.

