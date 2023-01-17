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
  'https://1c30-109-123-255-29.eu.ngrok.io/bin/458578' \
  -H 'accept: application/json'
```
> Request URL: https://1c30-109-123-255-29.eu.ngrok.io/bin/458578
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
  'https://1c30-109-123-255-29.eu.ngrok.io/adyen/' \
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
> Request URL: https://adyen-enc-and-bin-info.herokuapp.com/adyen
__Return__:
```
{
  "card": "adyenjs_0_1_25%24pd91Sl9SF1eTx%2BZrn3b9uL8dh%2BmO6HJrNQsf%2BmQ%2F2185qXMACyys4OCwKEpeBuT9j4%2FdLCfqeVGS0gdRIZRKDLvO689pTqvFnJ1tTiXwEEYkvCJ73bSGjPzPNexi%2FWo3KmoiAPWLwHWf514AKSCb1luoztp%2BZKxpg6IuqwQR%2FtsFBkrq761AQw6TwMtMxSr%2Fzs%2Fl6WjkTOBv5GviiKKHjOCpr1Y5eMv6t%2F9cjuDIYF9AWNx4F9o4qraNeAKl%2BVjs%2Fpm9aFV16QeYWpvjO24Rpb865V6%2BgQJW%2F8I8jRbpy6wlS3Mo%2FOSUBrOZqcrw8GBn8Qtf8q74kUXRdhtywGQ%2Bgg%3D%3D%2465MDJ9nl42hYDvxIYIow9ydXvjc3HPHXZFziT8yCuulYjzpQU7QXPJcev0eP35n5k5KIRbep5zxVX6ZX3n8saXsWwwKiZhonmtPbzSmc6T262Zc%2FJmW8K6mofH7qyteM",
  "month": "adyenjs_0_1_25%24lpdea4MvYqJm4YRdufTpwKGiem3UqLHia4kJ0Q5rb6uvNyKlL9J18M9HPYH%2F3Y37lbmPIgMmGNCYoK5%2BaTj5uquRtQ1njRP55T%2F6EudhpIQMKYaw4M6gQjdIrqosVplnps%2FD%2BnmuwHJM0DWIzZC8z30ZCz4Sl6RFBL3DPj0OhvjR9MvoAUwOHqJYc%2FF9zmtTq8vA5XCYAhVisBiqX7fj547almWBEcthyYw6LEg3BYMcs4MdJahEwUa17zDDKwLlLhvkI3m0qsDc8cTFjmYtnTsxVVSEttbUe0ljQJfVrRRPtcMGHNSA5JzWGf5mMfevjciQeAXRVFolIG6283qUnw%3D%3D%24%2FjDUAJFl4B1563Tw2p76GjeHnz03b0jhFrINlCYln1v81Omn4BbnEGnp7dzD3dpx6krXpg0P%2FCq1i1lEnG4B1v1texUPMUZ9%2Bm6AT0QUI3u%2BeuJ%2BxDs%3D",
  "year": "adyenjs_0_1_25%24btmuqQyBocIYHkfdrzowdn5EeJMsrmMcbSUX6DtlOA4Gu%2BlrNunyCwsovndkApfE6A9PYTCrsqUkJ%2F4iDizHkX4Ri%2FY24UfGjUzDbUjyHzhlM3f3ktgU4afyPT3Nb%2FoMf7gbreBJApdbxxh4Zz5jh%2BOb2znoEMM0MgoQ0HTVDy7CkNEKtbYxA72g1rz32lVJHlnTE7Urd2NkQVR5j6Js9PVkNfwRLiUUnZJN6p68WcShP0nUiptciJnMiP%2F3W6LgsQ9rS9PKCxcySSqXaW2ncgXX2pRgmCLjzR6yHKClzrcc%2BUqQ6D6br7vbACXv8OO877JGZVJp9lEqJ1tyQAZBnA%3D%3D%24s%2BlEPjpYoMMZIH8%2B75KqLOkCnKvajNHrNuEq8YmvCT3nw42cRQOASN5Xd34hWbdStKXQNfOVfD0RT64ebbXLJoHSvgB5nnwwB4Ps4n2aPWXbbK8789fY8w%3D%3D",
  "cvv": "adyenjs_0_1_25%24pwHRvu2ys6zXTUaabbjtXW6kZGZhojK1WoxqSFxkO44vvRZUzaIzWwost4mRvyaTE%2F%2FXv%2FSanWXPW4vCPJzqred%2F2atsz%2FzYuNBbUT9C1%2Bga9rgX7gXKRujS5lZFf18QXlG%2BBDERhtav1CuxbsMTmyaa4QLJ9BwohZgDHvEZW%2BOThw2yQTi5GlgwauTJbiw%2BCYgzKEqk24yeUSLQGKz4yD0R2wvILFJaWzV%2B0NBnMQ8ZWEdtTRL2PY%2BHHb9uwTMBJKcdZn7qDWGT6Acxjh4HMLaI5%2FkgCch6JRsUEq63L6ulqcw6kDYGCaCZ%2BFvPmPssNFzJK6IpX%2F%2BKESxfGPBIRQ%3D%3D%246WruUcmWAV4a2Ve3SKzjTx1usXSSIf3RiZxZkdMly%2Fc97CWO5pRsMiXGUlZyB8KKctoM0iiMacnPcPN%2F%2B1Iamw8z1xriaPCdeCuGCqwGx1o%3D"
}
```
> Return enc_card,enc_month,enc_year,enc_cvv

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

#### • MADE BY > [Roldex](https://github.com/r0ld3x)

## License
[MIT](https://choosealicense.com/licenses/mit/)
