from typing import Optional
from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from mongo_db import db, get_iso
import re
from pydantic import BaseModel
from py_adyen_encrypt import encryptor
import urllib


def adyen_enc(cc, mes, ano, cvv, ADYEN_KEY, adyen_version):
    enc = encryptor(ADYEN_KEY)
    enc.adyen_version = adyen_version
    enc.adyen_public_key = ADYEN_KEY

    card = enc.encrypt_card(card=cc, cvv=cvv, month=mes, year=ano)
    month = card['month']
    year = card['year']
    cvv = card['cvv']
    card = card['card']

    card = urllib.parse.quote_plus(card)
    Month = urllib.parse.quote_plus(month)
    Year = urllib.parse.quote_plus(year)
    cvv = urllib.parse.quote_plus(cvv)
    return card, Month, Year,cvv


app = FastAPI(debug=True, 
              title="Bin lookup And Adyen Generator Ny Roldexverse.", 
              redoc_url=None,
              description=" Feel free to use. made by @roldexverse for roldexverse subscribers.")


async def find_bin(id) -> object:
    find = await db.bins.find_one({'number':int(id)})
    print(find)
    if find is None:
        return None
    else:
        return find


class UnicornException(Exception):
    def __init__(self, name: str,  message: str):
        self.name = name
        self.message = message


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={'success': False, "message": exc.message},
    )


@app.get("/bin/{bin}")
async def bin(bin):
    price = ''.join(re.findall("\d+", bin))
    if len(price) == 0:
        raise HTTPException(
            status_code=404, detail="Give me 6 digits Numbers.")
    elif len(price) < 6:
        raise HTTPException(
            status_code=404, detail="Give me 6 numbers atleast.")
    bin = price[:6]
    bin_data = await find_bin(bin)
    if bin_data is None:
        raise HTTPException(status_code=404, detail="Bin Not Found")
    return {
        'bin': bin_data['number'],
        'bank': bin_data['bank'],
        'country_iso': bin_data['country'],
        'country': get_iso(bin_data['country']),
        'flag': bin_data['flag'],
        'vendor': bin_data['vendor'],
        'type': bin_data['type'],
        'level': bin_data['level'],
    }


@app.get("/")
async def bin(bin):
    return {
        "Made by":  'https://t.me/r0ld3x',
        'Github': 'https://github.com/r0ld3x',
        'Telegram': 'https://t.me/RoldexVerse',
        'Docs': 'https://roldexverseapi.herokuapp.com/docs'
    }

class Item(BaseModel):
    card: str
    month: str
    year: str
    cvv: str
    adyen_version: str
    adyen_key: str

,.
@app.post("/adyen/")
async def adyen(item: Item):
    cc, mes, ano, cvv = adyen_enc(
        item.card, item.month, item.year, item.cvv, item.adyen_key, item.adyen_version)
    return {
        'card': cc,
        'month': mes,
        'year': ano,
        'cvv': cvv
    }
