FROM prefecthq/prefect:2-python3.10

# Install additional dependencies
RUN pip install yfinance pandas

# Copy your flow code into the image
COPY ./prefect_data /opt/prefect/flows

# Set the working directory
WORKDIR /opt/prefect/flows