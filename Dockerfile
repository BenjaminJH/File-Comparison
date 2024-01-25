# set base image (host OS)
FROM python:3.9.18 as build

# Set working directory to project to have changes compartmentalised
WORKDIR project/

# Set environment variable path
ENV VIRTUAL_ENV=/project/opt/venv
# Create venv at that path
RUN python -m venv $VIRTUAL_ENV
# Enable venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# copy the dependencies file to the working directory
COPY requirements.txt .
# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local file_comparison directory to the working directory
COPY file_comparison/ file_comparison/
COPY test/ test/

# Set the pythonpath to the root of the project
ENV PYTHONPATH .

# command to run on container start
ENTRYPOINT ["python", "./file_comparison/cli/cli.py"]
