from openai import OpenAI
client = OpenAI(api_key="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")

res = client.images.generate(
  model="dall-e-3",
  prompt="A cute baby sea otter",
  n=1,
  size="1024x1024"
)

print(res)
