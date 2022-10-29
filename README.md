# Rozetka.com.ua active promotions parser
The project uses Python and Scrapy library
## Installation tutorial
1. Download and install the latest Python version from the official [Python website](https://www.python.org/).
2. Install scrapy library using pip.
    1) Open Command Prompt using administrator access on your computer.
    2) Enter the next command to install Scrapy library: `pip3 install scrapy`.
    3) Wait until the library is installed.
3. Download and extract the repository on your computer.
    An extracted folder structure should look like this:
```
rozetka-promotions-parser-master
│   .gitignore
│   scrapy.cfg
│
└───rozetka_discounts
│   items.py
│   middlewares.py
│   pipelines.py
│   settings.py
│   __init__.py
│
└───spiders
        rozetka.py
        __init__.py
```
## Usage tutorial
1. Run the Command Prompt inside the extracted folder.
2. Execute the next command to start parsing `scrapy crawl rozetka -o <filename>.<extension>`. 
Where `<filename>` is the name of a file to which you want to save scraped data and `<extension>` is the format of the file (available formats: `json`,`jsonlines`,`xml`,`csv`)
3. Wait until the application scrapes the data. The file should appear in the current folder.
4. Done!
