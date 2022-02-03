# Bin Info And Adyen Cse Enc Python

> I api for getting bin info and getting encrypted card details for adyen.

![GitHub stars](https://img.shields.io/github/stars/r0ld3x/adyen-enc-and-bin-info)
![GitHub forks](https://img.shields.io/github/forks/r0ld3x/adyen-enc-and-bin-info)
[![Maintenance](https://img.shields.io/badge/maintained-yes-green.svg)](https://github.com/r0ld3x/adyen-enc-and-bin-info/commits/master)
[![Website shields.io](https://img.shields.io/badge/website-up-yellow)](http://varadbhogayata.github.io/)
[![Ask Me Anything !](https://img.shields.io/badge/ask%20me-Telegram-blue.svg)](https://www.linkedin.com/in/varadbhogayata/)
[![License](http://img.shields.io/:license-MIT-blue.svg?style=flat-square)](http://badges.mit-license.org)

## Installation
> Local Installation
```
git clone http://www.github.com/r0ld3x/adyen-enc-and-bin-info
cd adyen-enc-and-bin-info
pip install -r requirements.txt
uvicorn index:app
```

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/r0ld3x/adyen-enc-and-bin-info.git)


## Usage
> website.com = your heroku website name

**BIN INFO**:-
```curl
https://website.com/bin/123456
```
> Return status code 200 if success else return 404 if bin not found

**ADYEN ENC**:-
```curl
https://website.com/adyen
METHOD = POST
post_data = {
  "card": "string", #card 123456789123456
  "month": "string", #month 01
  "year": "string", #year 22
  "cvv": "string", #cvv 123
  "adyen_version": "string", #adyen key, looks like this: "10001|A2370..."
  "adyen_key": "string", #_0_25
}
```
> Return enc_card,enc_month,enc_year,enc_cvv

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

#### • MADE BY > [Roldex](https://github.com/r0ld3x)

## License
[MIT](https://choosealicense.com/licenses/mit/)
