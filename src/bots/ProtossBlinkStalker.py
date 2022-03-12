from sc2.bot_ai import BotAI
# from sc2.ids.ability_id import AbilityId
# from sc2.ids.buff_id import BuffId
# from sc2.ids.unit_typeid import UnitTypeId


class ProtossBlinkStalker(BotAI):
    # async def on_start(self) -> None:
    #     print('Game started')
    #     # Do things here before the game starts

    # def on_end(self, result) -> None:
    #     print('Game ended.')
    #     # Do things here after the game ends

    async def on_step(self, iteration: int) -> None:
        # good manners
        if iteration == 0:
            await self.chat_send('(glhf)')

        self.units

        # self._client.debug_sphere_out(self.townhalls[0], 2, color=(0, 255, 255))
