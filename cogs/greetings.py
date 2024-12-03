from discord.ext import commands
import random as rand

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot         

    @commands.slash_command(name="hello", description="say hello to user")
    async def hello(self, ctx):
        # loads greetings from text file
        greetings = []
        file = open("greetings.txt", "r")
        for line in file:
            greetings.append(line)

        idx = rand.randint(0, len(greetings) - 1)
        await ctx.respond(greetings[idx])

def setup(bot):
    bot.add_cog(Greetings(bot))