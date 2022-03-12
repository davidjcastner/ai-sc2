from src.setup import get_random_map, setup, is_valid_map
from sc2.data import Difficulty, Race
from sc2.main import run_game
from sc2.player import Bot, Computer
from sc2 import maps


from src.bots.ProtossBlinkStalker import ProtossBlinkStalker

# class MyBot(BotAI):
#     async def on_start(self) -> None:
#         print('Game started')
#         # Do things here before the game starts

#     async def on_step(self, iteration: int) -> None:
#         if iteration == 0:
#             await self.chat_send('(glhf)')

#         # check if there is a nexus
#         if not self.townhalls.ready:
#             # attempt to build a nexus
#             if self.can_afford(UnitTypeId.NEXUS):
#                 await self.build(UnitTypeId.NEXUS, near=self.game_info.map_center)
#             # attack with probes
#             else:
#                 for unit in self.units:
#                     unit.attack(self.enemy_start_locations[0])
#                 return
#         else:
#             nexus = self.townhalls.ready.random

#         # build order
#         # pylon if supply is low
#         # worker if less than 80
#         # pylon if none
#         # gateway if none
#         # nexus if less than 2
#         # cybernetics core if none
#         # gateway if less than 2
#         # robotics bay if none
#         # twilight council if none
#         # nexus if less than 3
#         # gateway if less than 4
#         # nexus if less than 6
#         # gateway if less than 20

#         # Distribute workers in gas and across bases
#         await self.distribute_workers()

#         # checking for low on supply
#         if (
#             (self.supply_left < 2 and self.already_pending(UnitTypeId.PYLON) == 0)
#             or (self.supply_used > 15 and self.supply_left < 4 and self.already_pending(UnitTypeId.PYLON) < 2)
#         ):
#             if self.can_afford(UnitTypeId.PYLON):
#                 await self.build(UnitTypeId.PYLON, near=nexus)

#         # Train probe on nexuses that are undersaturated (avoiding distribute workers functions)
#         # if nexus.assigned_harvesters < nexus.ideal_harvesters and nexus.is_idle:
#         if (
#             self.supply_workers < 80
#             and self.supply_workers + self.already_pending(UnitTypeId.PROBE) < self.townhalls.amount * 22
#             and nexus.is_idle
#         ):
#             if self.can_afford(UnitTypeId.PROBE):
#                 nexus.train(UnitTypeId.PROBE)

#         # If we have less than 5 nexuses and none pending yet, expand
#         if self.townhalls.ready.amount + self.already_pending(UnitTypeId.NEXUS) < 5:
#             if self.can_afford(UnitTypeId.NEXUS):
#                 await self.expand_now()

#         # Once we have a pylon completed
#         if self.structures(UnitTypeId.PYLON).ready:
#             pylon = self.structures(UnitTypeId.PYLON).ready.random
#             if self.structures(UnitTypeId.GATEWAY).ready:
#                 # If we have gateway completed, build cyber core
#                 if not self.structures(UnitTypeId.CYBERNETICSCORE):
#                     if (
#                         self.can_afford(UnitTypeId.CYBERNETICSCORE)
#                         and self.already_pending(UnitTypeId.CYBERNETICSCORE) == 0
#                     ):
#                         await self.build(UnitTypeId.CYBERNETICSCORE, near=pylon)
#             else:
#                 # If we have no gateway, build gateway
#                 if self.can_afford(UnitTypeId.GATEWAY) and self.already_pending(UnitTypeId.GATEWAY) == 0:
#                     await self.build(UnitTypeId.GATEWAY, near=pylon)

#         # Build gas near completed nexuses once we have a cybercore (does not need to be completed)
#         if self.structures(UnitTypeId.CYBERNETICSCORE):
#             for nexus in self.townhalls.ready:
#                 vgs = self.vespene_geyser.closer_than(15, nexus)
#                 for vg in vgs:
#                     if not self.can_afford(UnitTypeId.ASSIMILATOR):
#                         break

#                     worker = self.select_build_worker(vg.position)
#                     if worker is None:
#                         break

#                     if not self.gas_buildings or not self.gas_buildings.closer_than(1, vg):
#                         worker.build(UnitTypeId.ASSIMILATOR, vg)
#                         worker.stop(queue=True)

#     def on_end(self, result) -> None:
#         print('Game ended.')
#         # Do things here after the game ends


def main() -> None:
    map_name = get_random_map()
    assert is_valid_map(map_name)
    run_game(
        maps.get(map_name),
        [
            Bot(Race.Protoss, ProtossBlinkStalker()),
            Computer(Race.Random, Difficulty.Hard)
        ],
        realtime=True
    )


if __name__ == '__main__':
    setup()
    main()
