from fastapi import FastAPI, Response, Query
from fastapi.responses import StreamingResponse
import time
import string
import secrets
import asyncio
import psutil

app = FastAPI(title="radi8's api", description="radi8's multi-tool api")
startTime = time.time()


@app.get("/")
def root():
    return {
        "status": "ok",
        "version": 0.5,
        "uptime": time.time() - startTime,
        "docs": "/docs",
    }


@app.get("/meminfo")
def meminfo():
    memory = psutil.virtual_memory()
    return {"total": memory.total, "available": memory.available, "used": memory.used}


@app.get("/password")
def generatePassword(
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
def generatePin(length: int = Query(4, gt=3, lt=7)):
    digits = string.digits
    pin = "".join(secrets.choice(digits) for _ in range(length))

    return Response(content=pin)


@app.get("/rainbow")
async def rainbow():
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
        for _ in range(1):
            for i in range(len(rainbow_colors)):
                color_index = i % len(rainbow_colors)
                color = rainbow_colors[color_index]
                yield color + "███████████\033[0m\n"
                await asyncio.sleep(delay)

    return StreamingResponse(generate_rainbow(), media_type="text/plain")


@app.get("/fakefact")
def fakefact():
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
    )
    return Response(content=secrets.choice(facts))


@app.get("/kidsaremuchmore")
def kidsAreMuchMore():
    return Response(
        content="Kids are much more accepting of other people than adults are."
    )


@app.get("/amogus")
def amogus():
    amogusANSI = """        \033[49m            \033[38;2;0;0;0;49m▄▄\033[38;2;0;0;0;48;2;12;12;12m▄\033[48;2;0;0;0m       \033[38;2;0;0;0;49m▄▄▄\033[49m          \033[m
        \033[49m          \033[38;2;0;0;0;49m▄\033[48;2;0;0;0m  \033[38;2;218;37;29;48;2;0;0;0m▄▄▄\033[48;2;218;37;29m    \033[38;2;218;37;29;48;2;4;0;0m▄\033[38;2;218;37;29;48;2;0;0;0m▄▄▄\033[48;2;0;0;0m   \033[38;2;0;0;0;49m▄\033[38;2;167;167;167;49m▄\033[49m      \033[m
        \033[49m         \033[48;2;0;0;0m  \033[38;2;218;37;29;48;2;0;0;0m▄\033[48;2;218;37;29m             \033[38;2;218;37;29;48;2;1;0;0m▄\033[38;2;218;37;29;48;2;0;0;0m▄\033[48;2;0;0;0m  \033[38;2;0;0;0;48;2;85;85;85m▄\033[49m     \033[m
        \033[49m        \033[48;2;0;0;0m  \033[38;2;122;2;54;48;2;0;0;0m▄\033[48;2;218;37;29m      \033[38;2;0;0;0;48;2;218;37;29m▄▄▄▄▄▄▄▄▄▄▄\033[48;2;0;0;0m   \033[49m    \033[m
        \033[49m       \033[38;2;32;32;32;49m▄\033[48;2;0;0;0m  \033[48;2;122;2;54m \033[48;2;218;37;29m    \033[48;2;0;0;0m    \033[38;2;145;200;219;48;2;0;0;0m▄▄▄▄▄▄▄▄▄▄\033[48;2;0;0;0m   \033[38;2;0;0;0;49m▄\033[49m  \033[m
        \033[49m       \033[48;2;0;0;0m  \033[38;2;13;1;3;48;2;0;0;0m▄\033[48;2;122;2;54m \033[48;2;218;37;29m   \033[38;2;0;0;0;48;2;177;30;23m▄\033[48;2;0;0;0m  \033[48;2;72;99;109m \033[38;2;72;99;109;48;2;145;200;219m▄\033[48;2;145;200;219m   \033[38;2;152;203;221;48;2;149;202;221m▄\033[48;2;255;255;255m      \033[38;2;255;255;255;48;2;145;200;219m▄\033[48;2;145;200;219m \033[38;2;145;200;219;48;2;0;0;0m▄\033[48;2;0;0;0m  \033[49m \033[m
        \033[49m  \033[38;2;0;0;0;49m▄▄▄\033[48;2;0;0;0m    \033[48;2;122;2;54m  \033[48;2;218;37;29m   \033[48;2;0;0;0m   \033[48;2;72;99;109m  \033[38;2;136;187;205;48;2;145;200;219m▄\033[48;2;145;200;219m      \033[38;2;145;200;219;48;2;174;215;228m▄\033[38;2;145;200;219;48;2;253;254;254m▄\033[38;2;145;200;219;48;2;255;255;255m▄\033[38;2;145;200;219;48;2;197;226;236m▄\033[48;2;145;200;219m  \033[38;2;145;200;219;48;2;0;0;0m▄\033[48;2;0;0;0m  \033[m
        \033[49m \033[48;2;0;0;0m  \033[38;2;218;37;29;48;2;0;0;0m▄▄▄▄\033[48;2;0;0;0m  \033[48;2;122;2;54m  \033[48;2;218;37;29m   \033[48;2;0;0;0m   \033[48;2;72;99;109m   \033[38;2;72;99;109;48;2;119;164;180m▄\033[38;2;72;99;109;48;2;145;200;219m▄▄▄▄▄▄▄▄▄▄▄\033[38;2;32;44;49;48;2;72;99;109m▄\033[48;2;0;0;0m  \033[m
        \033[38;2;0;0;0;48;2;54;54;54m▄\033[48;2;0;0;0m  \033[48;2;218;37;29m   \033[38;2;8;1;1;48;2;186;31;24m▄\033[48;2;0;0;0m  \033[48;2;122;2;54m  \033[48;2;218;37;29m   \033[38;2;218;37;29;48;2;108;18;14m▄\033[48;2;0;0;0m   \033[38;2;0;0;0;48;2;72;99;109m▄\033[48;2;72;99;109m           \033[38;2;0;0;0;48;2;72;99;109m▄▄\033[48;2;0;0;0m  \033[49;38;2;0;0;0m▀\033[m
        \033[48;2;0;0;0m  \033[38;2;122;2;54;48;2;2;0;0m▄\033[38;2;122;2;54;48;2;199;30;34m▄\033[48;2;122;2;54m  \033[48;2;0;0;0m   \033[48;2;122;2;54m  \033[48;2;218;37;29m    \033[38;2;218;37;29;48;2;0;0;0m▄\033[48;2;0;0;0m     \033[38;2;0;0;0;48;2;72;99;109m▄▄▄▄▄▄\033[48;2;0;0;0m      \033[49m  \033[m
        \033[48;2;0;0;0m  \033[48;2;122;2;54m    \033[48;2;0;0;0m   \033[48;2;122;2;54m  \033[48;2;218;37;29m      \033[38;2;218;37;29;48;2;71;12;9m▄\033[38;2;218;37;29;48;2;0;0;0m▄▄\033[48;2;0;0;0m     \033[38;2;218;37;29;48;2;0;0;0m▄▄▄▄▄\033[48;2;218;37;29m \033[48;2;0;0;0m  \033[49m  \033[m
        \033[48;2;0;0;0m  \033[48;2;122;2;54m    \033[38;2;1;0;0;48;2;0;0;0m▄\033[48;2;0;0;0m  \033[48;2;122;2;54m   \033[48;2;218;37;29m                  \033[38;2;132;5;51;48;2;218;37;29m▄\033[48;2;0;0;0m  \033[49m  \033[m
        \033[48;2;0;0;0m  \033[48;2;122;2;54m    \033[38;2;9;0;4;48;2;8;1;2m▄\033[48;2;0;0;0m  \033[48;2;122;2;54m   \033[38;2;202;31;33;48;2;218;37;29m▄\033[48;2;218;37;29m                 \033[48;2;122;2;54m \033[48;2;0;0;0m  \033[49m  \033[m
        \033[48;2;0;0;0m  \033[48;2;122;2;54m    \033[38;2;131;8;46;48;2;88;8;25m▄\033[48;2;0;0;0m  \033[48;2;122;2;54m    \033[48;2;218;37;29m                \033[38;2;122;2;54;48;2;218;37;29m▄\033[48;2;122;2;54m \033[48;2;0;0;0m  \033[49m  \033[m
        \033[48;2;0;0;0m  \033[48;2;122;2;54m     \033[48;2;0;0;0m  \033[48;2;122;2;54m     \033[38;2;149;12;47;48;2;218;37;29m▄\033[48;2;218;37;29m             \033[38;2;210;34;31;48;2;218;37;29m▄\033[48;2;122;2;54m  \033[48;2;0;0;0m  \033[49m  \033[m
        \033[48;2;0;0;0m  \033[38;2;128;5;50;48;2;122;2;54m▄\033[48;2;122;2;54m    \033[48;2;0;0;0m  \033[48;2;122;2;54m       \033[38;2;122;2;54;48;2;154;14;45m▄\033[38;2;122;2;54;48;2;218;37;29m▄▄▄▄▄▄▄▄▄▄\033[48;2;122;2;54m    \033[48;2;0;0;0m  \033[49m  \033[m
        \033[49;38;2;0;0;0m▀\033[48;2;0;0;0m  \033[48;2;122;2;54m    \033[48;2;0;0;0m  \033[48;2;122;2;54m                     \033[48;2;0;0;0m  \033[38;2;63;63;63;48;2;0;0;0m▄\033[49m  \033[m
        \033[49m \033[49;38;2;0;0;0m▀\033[48;2;0;0;0m   \033[38;2;0;0;0;48;2;4;0;2m▄\033[38;2;0;0;0;48;2;4;0;1m▄\033[48;2;0;0;0m  \033[48;2;122;2;54m        \033[38;2;0;0;0;48;2;122;2;54m▄▄▄▄▄▄▄▄▄▄\033[48;2;122;2;54m   \033[48;2;0;0;0m  \033[49m   \033[m
        \033[49m   \033[49;38;2;36;36;36m▀\033[49;38;2;0;0;0m▀▀▀\033[48;2;0;0;0m  \033[48;2;122;2;54m        \033[48;2;0;0;0m  \033[49;38;2;0;0;0m▀▀\033[48;2;0;0;0m   \033[38;2;122;2;54;48;2;0;0;0m▄\033[48;2;122;2;54m    \033[38;2;0;0;0;48;2;123;2;53m▄\033[48;2;0;0;0m  \033[49m   \033[m
        \033[49m       \033[48;2;0;0;0m  \033[38;2;46;3;15;48;2;128;6;47m▄\033[48;2;122;2;54m       \033[48;2;0;0;0m  \033[49m  \033[48;2;0;0;0m   \033[48;2;122;2;54m     \033[48;2;0;0;0m  \033[38;2;20;20;20;48;2;0;0;0m▄\033[49m   \033[m
        \033[49m       \033[48;2;0;0;0m   \033[48;2;122;2;54m       \033[48;2;0;0;0m  \033[49m   \033[48;2;0;0;0m  \033[48;2;122;2;54m     \033[48;2;0;0;0m  \033[49m    \033[m
        \033[49m       \033[38;2;54;58;59;48;2;129;129;129m▄\033[48;2;0;0;0m  \033[38;2;0;0;0;48;2;122;2;54m▄\033[38;2;124;3;53;48;2;122;2;54m▄\033[48;2;122;2;54m   \033[38;2;0;0;0;48;2;122;2;54m▄\033[38;2;0;0;0;48;2;8;1;2m▄\033[48;2;0;0;0m  \033[38;2;54;58;59;48;2;65;68;69m▄\033[38;2;54;58;59;48;2;64;67;68m▄\033[38;2;54;58;59;48;2;89;94;94m▄\033[38;2;54;58;59;48;2;0;0;0m▄\033[48;2;0;0;0m       \033[38;2;54;58;59;48;2;0;0;0m▄\033[49m    \033[m
        \033[49m   \033[38;2;56;60;61;49m▄\033[48;2;54;58;59m    \033[38;2;54;58;59;48;2;5;5;6m▄\033[38;2;54;58;59;48;2;0;0;0m▄\033[48;2;0;0;0m      \033[38;2;24;26;27;48;2;0;0;0m▄\033[38;2;54;58;59;48;2;0;0;0m▄\033[48;2;54;58;59m                \033[38;2;54;58;59;49m▄\033[m
        \033[49m     \033[49;38;2;54;58;59m▀▀▀▀▀\033[38;2;57;61;62;48;2;54;58;59m▄\033[48;2;54;58;59m                \033[38;2;57;61;62;48;2;54;58;59m▄\033[49;38;2;54;58;59m▀▀▀▀▀\033[49m  \033[m
    """  # fix: read from ./ansi/amogus.txt and have it display properly
    return Response(content=amogusANSI, media_type="text/plain")
