import asyncio
from src.novelai.client import NAIClient
from src.novelai import Metadata, Host, Resolution

NSFW_TAGS_FILE = "anti_entropy/data/nsfw_tags.txt"
DEFAULT_NEGATIVE_PROMPT = "nsfw, bad anatomy"


async def main():

    # You can change the host to your own host
    Host.CUSTOM.value.url = "http://127.0.0.1:5000"
    client = NAIClient(token="123456")

    await client.init(timeout=60)

    # For resolution preset, please choose between SMALL_PORTRAIT, SMALL_LANDSCAPE, SMALL_SQUARE. NORMAL_PORTRAIT, NORMAL_LANDSCAPE, NORMAL_SQUARE. otherwise, it will charge your opus.
    metadata = Metadata(
        prompt="aponia (honkai impact), best quality, amazing quality, very aesthetic, absurdres",
        negative_prompt=DEFAULT_NEGATIVE_PROMPT,
        res_preset=Resolution.NORMAL_PORTRAIT.value,
        n_samples=1,
        scale=6.0,
        steps=28,  # please choose between 1 to 28, otherwise, it will charge Opus.
        qualityToggle=True,
        ucPreset=0,
    )

    print(f"Estimated Anlas cost: {metadata.calculate_cost(is_opus=True)}")

    # Choose host between "Host.API" and "Host.WEB"
    # Both of two hosts work the same for all actions mentioned below
    output = await client.generate_image(
        metadata, host=Host.CUSTOM, verbose=False, is_opus=False
    )

    for image in output:
        image.save(path="output images", verbose=True)


asyncio.run(main())
