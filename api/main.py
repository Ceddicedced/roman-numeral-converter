from fastapi import FastAPI, HTTPException

from roman_numerals_converter import (
    convert_from_roman,
    convert_to_roman,
    random_roman,
    replace_roman_numerals_in_text,
)

app = FastAPI()


@app.get("/to-roman/{number}")
async def to_roman_endpoint(number: int):
    try:
        return {"result": convert_to_roman(number)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@app.get("/from-roman/{roman}")
async def from_roman_endpoint(roman: str):
    try:
        return {"result": convert_from_roman(roman)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@app.get("/replace-roman")
async def replace_roman_endpoint(text: str):
    return {"result": replace_roman_numerals_in_text(text)}


@app.get("/random-roman/")
async def random_roman_endpoint(min_value: int = 1, max_value: int = 3999):
    try:
        roman, random = random_roman(min_value, max_value)
        return {
            "result": roman,
            "min": min_value,
            "max": max_value,
            "random": random,
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
