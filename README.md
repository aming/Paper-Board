# Paper-Board

Display board for E-paper display

## Installation

You have to install following dependencies

### BCM2835 library

```bash
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.60.tar.gz
tar zxvf bcm2835-1.60.tar.gz 
cd bcm2835-1.60/
sudo ./configure
sudo make
sudo make check
sudo make install
```

### Other dependencies

```bash
sudo apt-get install libopenjp2-7 libatlas-base-dev
```

Now we can install the package locally (for use on our system), with:

```bash
pip install .
```

We can also install the package with a symlink, so that changes to the source files will be immediately available to other users of the package on our system:

```bash
pip install -e .
```

## Configuration

The configuration file is put under `~/.config/paper-board/config.ini

Here is an example of configuration

```ini
[weather]
api_token=<OWM API Token>
location=Seattle
```

## Get API credentials

### Open Weather Map API

Get the weather API Key from [Weather API page](https://openweathermap.org/api)
Then, add API Code to your config file.
