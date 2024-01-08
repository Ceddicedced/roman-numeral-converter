import logging

from fastapi import FastAPI, HTTPException

from roman_numerals_converter import (
    convert_from_roman,
    convert_to_roman,
    random_roman,
    replace_integers_with_roman_numerals,
    replace_roman_numerals_with_integers_in_text,
)

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/to-roman/{number}")
async def to_roman_endpoint(number: int):
    logger.info(f"Converting to Roman: {number}")
    try:
        result = convert_to_roman(number)
        logger.info(f"Result: {result}")
        return {"result": result}
    except ValueError as e:
        logger.error(f"Error in converting to Roman: {e}")
        raise HTTPException(status_code=400, detail=str(e)) from e


@app.get("/from-roman/{roman}")
async def from_roman_endpoint(roman: str):
    logger.info(f"Converting from Roman: {roman}")
    try:
        result = convert_from_roman(roman)
        logger.info(f"Result: {result}")
        return {"result": result}
    except ValueError as e:
        logger.error(f"Error in converting from Roman: {e}")
        raise HTTPException(status_code=400, detail=str(e)) from e


@app.get("/replace-roman")
async def replace_roman_endpoint(text: str):
    logger.info(f"Replacing Roman numerals in text: {text}")
    result = replace_roman_numerals_with_integers_in_text(text)
    logger.info(f"Result: {result}")
    return {"result": result}


@app.get("/replace-integers")
async def replace_integers_endpoint(text: str):
    logger.info(f"Replacing integers in text: {text}")
    result = replace_integers_with_roman_numerals(text)
    logger.info(f"Result: {result}")
    return {"result": result}


@app.get("/random-roman/")
async def random_roman_endpoint(min_value: int = 1, max_value: int = 3999):
    logger.info(f"Generating random Roman numeral between {min_value} and {max_value}")
    try:
        roman, random = random_roman(min_value, max_value)
        logger.info(f"Result: {roman}, Random: {random}")
        return {
            "result": roman,
            "min": min_value,
            "max": max_value,
            "random": random,
        }
    except ValueError as e:
        logger.error(f"Error in generating random Roman: {e}")
        raise HTTPException(status_code=400, detail=str(e)) from e
