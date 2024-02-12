import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

URL = 'https://careers.redacted.com/us/en/search-results?keywords='
JOB_TITLE = 'Product%20Manager'
LOCATION = 'location=India'
SENDER_ADDRESS = ‘redacted@example.com’
RECEIVER_ADDRESS = 'redacted@example.com’

def check_for_new_jobs():
    # URL of Microsoft Careers job search with filters for Product Manager jobs in India
    url = URL + JOB_TITLE + '&' + LOCATION
    
    # Send a request to the website
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find job listings. This requires inspecting the webpage to determine the correct selector
    job_listings = soup.find_all('div', class_='job-listing specific class name')  # Example class name

    # Filter jobs by title and geography, already filtered by URL but double-check if needed
    new_jobs = []
    for job in job_listings:
        title = job.find('h2').text  # Assuming title is in <h2> tag
        # Add further processing if necessary
        new_jobs.append(title)

    return new_jobs

def send_email(job_titles):
    
    # Email setup
    msg = MIMEMultipart()
    msg['From'] = SENDER_ADDRESS
    msg['To'] = RECEIVER_ADDRESS
    msg['Subject'] = 'New Job Openings'

    body = 'New jobs found:\n' + '\n'.join(job_titles)
    msg.attach(MIMEText(body, 'plain'))
    
    # Setup the SMTP server
    server = smtplib.SMTP('smtp.example.com', 587)  # Use your SMTP server
    server.starttls()
    server.login(from_addr, "your_password")
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()

def main():
    while True:
        new_jobs = check_for_new_jobs()
        if new_jobs:
            send_email(new_jobs)
        time.sleep(86400)  # Check once every day

if __name__ == "__main__":
    main()
