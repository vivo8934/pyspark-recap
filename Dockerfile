FROM openjdk:17-jdk-slim

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Install PySpark
RUN pip3 install pyspark

# Copy your PySpark script
COPY spark_day1.py /app/spark_day1.py
COPY data/sample_text.txt /app/data/sample_text.txt

# Set working directory
WORKDIR /app

# Run the script
CMD ["python3", "spark_day1.py"]
