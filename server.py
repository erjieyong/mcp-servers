from browser_use import Agent, ChatGoogle
import os
import asyncio

# Read GOOGLE_API_KEY into env
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = (
    "/Users/jieyonger/Documents/keys/neon-partition-436203-q0-eb14c2c1e336.json"
)


async def main():
    # Initialize the model
    llm = ChatGoogle(
        model="gemini-2.5-flash",
        vertexai=True,
        project="neon-partition-436203-q0",
        # Make sure this is the correct location for your GCP project
        location="asia-southeast1",
    )

    # Create agent with the model
    agent = Agent(task="what's today's latest news?", llm=llm)

    await agent.run()


if __name__ == "__main__":
    asyncio.run(main())
