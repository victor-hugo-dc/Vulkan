from discord.ext.commands import Context
from discord import Client
from Handlers.AbstractHandler import AbstractHandler
from Handlers.HandlerResponse import HandlerResponse
from Parallelism.ProcessManager import ProcessManager
from Parallelism.Commands import VCommands, VCommandsType


class ResetHandler(AbstractHandler):
    def __init__(self, ctx: Context, bot: Client) -> None:
        super().__init__(ctx, bot)

    async def run(self) -> HandlerResponse:
        # Get the current process of the guild
        processManager = ProcessManager()
        processContext = processManager.getRunningPlayerContext(self.guild)
        if processContext:
            command = VCommands(VCommandsType.RESET, None)
            queue = processContext.getQueue()
            queue.put(command)

        return HandlerResponse(self.ctx)
