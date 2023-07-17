from fastapi import FastAPI, Response, Query
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.routing import APIRoute
from typing import List
import time
import string
import secrets
import asyncio
import psutil
import ansi
import json

app = FastAPI(title="radi8's api", description="radi8's multi-tool api")
startTime = time.time()


@app.get("/")
async def root():
    return {
        "status": "ok",
        "version": 0.8,  # probably
        "uptime": time.time() - startTime,
        "docs": "/docs",
    }


@app.get("/routes")
def getRoutes():
    routes = []
    for route in app.routes:
        routeInfo = {}
        routeInfo["path"] = route.path
        routeInfo["methods"] = route.methods
        routes.append(routeInfo)
    return JSONResponse(content=jsonable_encoder(routes))


@app.get("/meminfo")
async def meminfo():
    memory = psutil.virtual_memory()
    return {"total": memory.total, "available": memory.available, "used": memory.used}


@app.get("/password")
async def generatePassword(
    length: int = Query(8, gt=0, lt=256),
    includeUppercase: bool = True,
    includeLowercase: bool = True,
    includeDigits: bool = True,
    includePunctuation: bool = True,
):
    if not any([includeUppercase, includeLowercase, includeDigits, includePunctuation]):
        return {"error": "at least one option must be enabled"}

    chars = ""
    password = ""

    if includeUppercase:
        chars += string.ascii_uppercase
        password += secrets.choice(string.ascii_uppercase)
    if includeLowercase:
        chars += string.ascii_lowercase
        password += secrets.choice(string.ascii_lowercase)
    if includeDigits:
        chars += string.digits
        password += secrets.choice(string.digits)
    if includePunctuation:
        chars += string.punctuation
        password += secrets.choice(string.punctuation)

    remainingLength = length - len(password)
    password += "".join(secrets.choice(chars) for _ in range(remainingLength))

    passwordList = list(password)
    secrets.SystemRandom().shuffle(passwordList)
    shuffledPassword = "".join(passwordList)

    return Response(content=shuffledPassword)


@app.get("/pin")
async def generatePin(length: int = Query(4, gt=3, lt=7)):
    digits = string.digits
    pin = "".join(secrets.choice(digits) for _ in range(length))

    return Response(content=pin)


@app.get("/rainbow")
async def rainbow(times: int = 0):
    rainbow_colors = [
        "\033[38;5;196m",  # red
        "\033[38;5;202m",  # orange
        "\033[38;5;226m",  # yellow
        "\033[38;5;118m",  # green
        "\033[38;5;45m",  # blue
        "\033[38;5;99m",  # indigo
        "\033[38;5;201m",  # violet
    ]
    delay = 0.5

    async def generate_rainbow():
        if times == 0:
            while True:
                for i in range(len(rainbow_colors)):
                    color_index = i % len(rainbow_colors)
                    color = rainbow_colors[color_index]
                    yield color + "███████████\033[0m\n"
                    await asyncio.sleep(delay)
        else:
            for _ in range(times):
                for i in range(len(rainbow_colors)):
                    color_index = i % len(rainbow_colors)
                    color = rainbow_colors[color_index]
                    yield color + "███████████\033[0m\n"
                    await asyncio.sleep(delay)

    return StreamingResponse(generate_rainbow(), media_type="text/plain")


@app.get("/fakefact")
async def fakefact():
    facts = (
        "Salty water boils quicker",
        "You swallow on average 8 spiders every year",
        "If you drop a penny for the Empire State you can kill someone",
        "Mt. Everest is the tallest mountain in the world",
        "The world is flat",
        "Blood without oxygen is blue",
        "Tomatoes are vegatables",
        "Humans only use 10% of their brains",
        "Coffee stunts your growth",
        "Coffee helps you sober up",
        "Bananas are actually an herb",
        "Zebras are just horses with stripes",
        "The Loch Ness Monster is real",
        "Napoleon Bonaparte was extremely short",
        "Microwaving food removes its nutrients",
        "The Moon landng was faked",
        "Thyme is technically a tree",
        "There are more than 30 blimps in the world",
        "Gold nuggets were named after chicken nuggets - not the other way around",
        "The first video uploaded to YouTube was taken down in 2016 for ToS violation",
        "Your kneecap is the roundest part in your body",
        "Bubbles have a seam",
        "Peppermint can't be smelt by guinea pigs",
        "NASA made powdered water",
        "Thomas Edison invented the first light bulb",
        "Electromagnetic radiation from cell phones and microwaves cause cancer",
        "1/4 of the US population doesn't believe in the moon",
        "Purified water is more dangerous to our health than tap water",
        "The sea is only 4% water",
        "This fact has a higher chance to appear than the others",
        "Pickles are legal tender in Arkansas",
        "Half-Life 4 will come out",
        "Lemons are named after the color - not the other way around",
        "Bees violate the laws of physics by flying",
        "The term 'petabyte' was invented when a small COD patch was released",
        "In one of the first revisions of the ASCII standard, the lowercase letter z was left out. It was shortly fixed",
        "This statement is false",
        "If only slightly chemically altered, lemons are combustible",
        "Adults are much more accepting of other people than kids are",
        "The xbox 360 was origanally named the xbox 0, anticipating the xbox 1. No one is quite sure why it was changed",
        "Doom can be run on moon rocks, but its highly discouraged due to moon rock poisoning",
        "None of these facts are portal references",
        "jeffalo is the only CEO that isnt a lizard person",
        "Watermelons are 91.5% fire",
        "The color green doesn't exist",
    )
    return Response(content=secrets.choice(facts))


@app.get("/kidsaremuchmore")
async def kidsAreMuchMore():
    return Response(
        content="Kids are much more accepting of other people than adults are."
    )


@app.get("/amogus")
async def amogus():
    return Response(content=ansi.amogus, media_type="text/plain")


@app.get("/jeffalo")
async def jeffalo():
    return Response(content=ansi.jeffalo, media_type="text/plain")


@app.get("/flags")
def flags():
    return list(ansi.flags.keys())


@app.get("/flags/{flag}")
async def prideflag(flag: str):
    try:
        return Response(content=ansi.flags[flag], media_type="text/plain")
    except:
        return {"error": "flag not found"}
