import requests
import time

# URL of the webpage you want to measure
url = "https://byenna.github.io/ProjectX-website/"

# Function to measure page load time and server response time
def measure_load_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    
    page_load_time = end_time - start_time
    server_response_time = response.elapsed.total_seconds()
    
    return page_load_time, server_response_time

# Measure and print the load times
page_load_time, server_response_time = measure_load_time(url)
print(f"Page Load Time: {page_load_time:.2f} seconds")
print(f"Server Response Time: {server_response_time:.2f} seconds")