from diffusers import DiffusionPipeline

pipeline = DiffusionPipeline.from_pretrained("./stabilityai/stable-diffusion-xl-base-1.0")

prompt = "An astronaut riding a green horse"

images = pipe(prompt=prompt).images[0]