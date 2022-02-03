# Bin Info And Adyen Cse Enc Python

> api for getting bin info and getting encrypted card details for adyen.

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
curl -X 'GET' \
  'https://adyen-enc-and-bin-info.herokuapp.com/bin/458578' \
  -H 'accept: application/json'
```
> Request URL: https://adyen-enc-and-bin-info.herokuapp.com/bin/458578
__Return__: 
```
{
  "bin": "458578",
  "bank": "PJSC CB EUROBANK",
  "country_iso": "UA",
  "country": "UA",
  "flag": "🇺🇦",
  "vendor": "VISA",
  "type": "DEBIT",
  "level": "CLASSIC",
  "prepaid": false
}
```
> Return status code 200 if success else return 404 if bin not found

**ADYEN ENC**:-
```curl
curl -X 'POST' \
  'https://adyen-enc-and-bin-info.herokuapp.com/adyen/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "card": 5415900002240330,
  "month":7,
  "year": 2024,
  "cvv": 544,
  "adyen_key": "10001|E9DB107F38F77A23A8822CB39CDA57D971F8CA05D91C5EAA3B621F7E0CFD3E8A2C877AD39DBA8C9189EA5820EEC8483A9069BA005964200FD5FB8EFEE6F5E232EDA7915538BEB30D7F5B8FC5A12337B1E05A168760183E599571F8B43E79CCD3223C666A1FA234D2174092852D86BF751CBAAB18DD9B829B489CB43F16B3D1C70191AA12045CFFEC049030801A3891B56A43D2E6CD634E4DC403CA922D44B43498244E13BA90B6D083F5BDCF1D8D41A34B2B46D28ACBD634DD25A5037F53D8911A57D11292FB9E388C6F3A66DCB218FDC12B4EDF12F1EC130ED2423882FEF9ADAD6E27620D26CCA117BFBE2D7501BD45FDF8ED2A433A42C298A9A07B34D73CB5",
  "adyen_version": "_0_1_25"
}'
```
> Request URL: https://adyen-enc-and-bin-info.herokuapp.com/bin/458578
> Return enc_card,enc_month,enc_year,enc_cvv

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

#### • MADE BY > [Roldex](https://github.com/r0ld3x)

## License
[MIT](https://choosealicense.com/licenses/mit/)
