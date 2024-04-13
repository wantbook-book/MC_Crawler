# Hunger
Hunger is a player-specific feature of Minecraft that regulates player's certain abilities (health regeneration and the ability to sprint), the value of which is managed by the player's activity.

## Contents
- 1 Description
- 2 Mechanics
	- 2.1 Effects of hunger
	- 2.2 Exhaustion level increase
	- 2.3 Food level and saturation level restoration
- 3 Food poisoning
- 4 Achievements
- 5 Video
- 6 History
- 7 Issues
- 8 References

## Description
The player's hunger value is shown on the heads-up display in the form of a hunger bar (aka food bar), which is similar to the health bar. It is located above the hotbar, opposite to health bar and represented by ten ham shanks ( × 10). One half of a ham shank () represents one hunger point or half-unit of hunger, thus the full bar consists of twenty hunger points. It is replenished by eating food, and decreased by player's actions such as sprinting, digging or attacking.

Various levels of player's hunger control health regeneration (or depletion) and the ability to sprint. When hunger is at least 18 (), the player's health regenerates. If it falls to 6 (), the player loses the ability to sprint. If the hunger bar is at zero, the player's health depletes. The specific effects are described in the Effects of hunger section. The hunger value does not drain on Peaceful difficulty and regenerates if it is not at the maximum value.

An important aspect of hunger not shown on the hunger bar is called food saturation and controls the decreasing of the hunger value. It depends on what the player has eaten last. There is also a food exhaustion value that controls the decreasing of the food saturation level. How exactly they control the overall hunger value is described in more depth in the Mechanics section.

See also:  § Food poisoning

Certain foods have a chance of inflicting the Hunger effect on the player upon consumption, causing the player's food bar to deplete faster and turn a yellow-green color (). These foods are pufferfish, raw chicken (30% chance), and rotten flesh (80% chance). A husk can also give the player the Hunger effect upon being attacked by one.

## Mechanics
The hunger system utilizes four variables to control players' abilities, the values of which are stored in the player.dat format:

- foodLevel: The player's current hunger level, shown on the hunger bar. Its initial value onworldcreation or respawn is20 ( × 10).
- foodSaturationLevel: The player's current saturation level, which determines how fastfoodLeveldepletes and is controlled by the kinds of food the player has eaten. Its maximum value always equalsfoodLevel's value and decreases withfoodLevel. Its initial value on world creation or respawn is 5.
- foodTickTimer: This variable is used whenfoodLeveleither exceeds 17 (), or is at zero. It increases on everytick, and whenever it reaches 80 (4 seconds), it resets to zero and 1is added or deducted, depending on whether the player is saturated or starving. If the player has a full20 ( × 10),1⁄6of 1times the player'sfoodSaturationLevelis restored, up to a maximum of 1, whenfoodTickTimerreaches 10 (1⁄2second), andfoodTickTimeris reset to zero.
- foodExhaustionLevel: The player's current exhaustion level, which determines how fast thefoodSaturationLeveldepletes. Its value is increased by the player's actions (seeExhaustion level increasefor specific values). The initial value is zero. When it reaches a value of at least 4, the total value is decreased by 4 and one point is subtracted fromfoodSaturationLevel, orfoodLeveliffoodSaturationLevelis at zero.

The above variables can be queried in-game with the following command: /data get entity <player's name> <variable>‌[Java Edition  only].

As a visible sign that the saturation is used up, the hunger bar starts to shake or jitter periodically. When the saturation level is at zero, once the exhaustion value reaches 4, the total hunger value is decreased by 1 (). Eating food replenishes both hunger and saturation levels (see Food level and saturation level restoration for specific values), with the hunger level being replenished first, which also increases the maximum allowed saturation level. For example, if a golden carrot (giving 6 () and 14.4 saturation points) is eaten by a player whose hunger bar is at 9 () and saturation is below 1, its value increases to 15 (), and the golden carrot's saturation potential is fully used. However, if the hunger level is 8 (), its value increases to 14 () and only 14 saturation points are used.

### Effects of hunger
Various hunger levels lead to various effects on the player:

- When the hunger bar is at 20 () and there is any saturation left, health regenerates 1every1⁄2second.‌[Java Edition  only]
- When the hunger bar is at 18 () or more, health slowly regenerates 1every 4 seconds.
- When the hunger bar is at 17 () points or below, the player does not naturally regenerate health.
- If the hunger bar is at6 ()points or below, then the player cannot sprint.
- When the hunger bar is at0 (), the player's health depletes at a rate of 1every 4 seconds (this makessleepingimpossible). On Easydifficulty, the player's health stops dropping at 10, on Normal, it stops at 1, and on Hard, it keeps draining until either the player eats something or starves to death.Resistanceandarmordo not reduce starvation damage.[1]

Switching to Peaceful difficulty eliminates all penalties above, and rapidly restores the player's hunger bar and health.

### Exhaustion level increase
Any action not listed here does not increase exhaustion level. For example, normal walking doesn't increase exhaustion, and therefore does not decrease saturation or the food bar.

| Action                                                                                   | Exhaustionlevel increase | Units                                               |
|------------------------------------------------------------------------------------------|--------------------------|-----------------------------------------------------|
| Swimming                                                                                 | 0.01                     | per meter                                           |
| Breakinga block                                                                          | 0.005                    | per block broken                                    |
| Sprinting                                                                                | 0.1                      | per meter                                           |
| Jumping                                                                                  | 0.05                     | per jump                                            |
| Attacking anentity                                                                       | 0.1                      | per attack landed                                   |
| Takingdamagethat is normallyprotected by armor                                           | 0.1                      | per distinct instance of damage being received      |
| Hunger                                                                                   | 0.005                    | per tick, per Hunger status effect level            |
| Jumping while sprinting                                                                  | 0.2                      | per jump                                            |
| Regenerating health by having× 9or higher andhavinggamerulenaturalRegenerationset totrue | 6.0                      | per 1healed                                         |
| Hungerfromraw chickenorrotten flesh, or taking damage fromhusks.                         | 3.0                      | full 0:30 duration of Hunger I, at 0.1 per second   |
| Hungerfrompufferfish                                                                     | 4.5                      | full 0:15 duration of Hunger III, at 0.3 per second |

### Food level and saturation level restoration
Main article: Food
| Name                                      | Icon | Food points | Saturation restored          | Effective quality[note 1]    | Saturation ratio             | Effect(s)                                                                                                                                                                                   | Source(s)                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------|------|-------------|------------------------------|------------------------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Apple                                     |      | 4 ()        | 2.4                          | 6.4                          | 0.6                          | None                                                                                                                                                                                        | Destroyed/despawned oak or dark oak leaves Stronghold altar and storeroom, village weaponsmith and plains house, igloo and bonus chests Receive 4 for 1 emerald at apprentice-level trade of farmer villager                                                                                                |
| Baked Potato                              |      | 5 ()        | 6                            | 11                           | 1.2                          | None                                                                                                                                                                                        | Cookingapotatoin afurnace,smoker, orcampfire                                                                                                                                                                                                                                                                |
| Beetroot                                  |      | 1 ()        | 1.2                          | 2.2                          | 1.2                          | None                                                                                                                                                                                        | Harvesting beetroot crops Farmer villager who drop beetroot after harvesting beetroot crop                                                                                                                                                                                                                  |
| Beetroot Soup                             |      | 6 ()        | 7.2                          | 13.2                         | 1.2                          | None                                                                                                                                                                                        | Crafting a bowl together with beetroots village snowy tundra house chest                                                                                                                                                                                                                                    |
| Bread                                     |      | 5 ()        | 6                            | 11                           | 1.2                          | None                                                                                                                                                                                        | Crafting from wheat Dungeon, stronghold altar and storeroom, village, mineshaft, woodland mansion and bonus chests Receive 6 for 1 emerald at novice-level trade of farmer villager Farmer villager who drop bread after harvesting wheat Raid gift from farmer villager‌[Java Edition  only]               |
| Cake(slice)                               |      | 2 ()        | 0.4                          | 2.4                          | 0.2                          | None                                                                                                                                                                                        | Consumeone slice ofcake                                                                                                                                                                                                                                                                                     |
| Cake(whole)                               |      | 14 ( × 7)   | 2.8                          | 16.8                         | 0.2                          | None                                                                                                                                                                                        | Crafting from wheat, eggs, sugar, and milk Receive 1 for 1 emerald at expert-level trade of farmer villager Buried treasure chest‌[Bedrock Edition  only]                                                                                                                                                   |
| Carrot                                    |      | 3 ()        | 3.6                          | 6.6                          | 1.2                          | None                                                                                                                                                                                        | Killing zombies Harvesting carrot crops pillager outpost and Shipwreck supply chest bonus chest‌[Bedrock Edition  only] Farmer villager who drop carrot after harvesting carrot crop                                                                                                                        |
| Chorus Fruit                              |      | 4 ()        | 2.4                          | 6.4                          | 0.6                          | The player may be teleported randomly, as described atEnderman#Teleportation.                                                                                                               | Breakingchorus plants. Found inThe End.                                                                                                                                                                                                                                                                     |
| Cooked Chicken                            |      | 6 ()        | 7.2                          | 13.2                         | 1.2                          | None                                                                                                                                                                                        | Cooking a raw chicken Killing chickens with fire Receive 8 for 1 emerald at novice-level trade from Butcher villager Raid gift from butcher villager‌[Java Edition  only]                                                                                                                                   |
| Cooked Cod                                |      | 5 ()        | 6                            | 11                           | 1.2                          | None                                                                                                                                                                                        | Cooking a raw cod Killing cod with fire‌[Java Edition  only] Killing dolphin with fire Rare drop from guardians and elder guardians when killed with fire‌[Java Edition  only] Receive 6 for 1 emerald + 6 raw cod at novice-level trade from fisherman villager buried treasure chest‌[Java Edition  only] |
| Cooked Mutton                             |      | 6 ()        | 9.6                          | 15.6                         | 1.6                          | None                                                                                                                                                                                        | Cooking raw mutton Killing sheep with fire Raid gift from butcher villager‌[Java Edition  only]                                                                                                                                                                                                             |
| Cooked Porkchop                           |      | 8 ()        | 12.8                         | 20.8                         | 1.6                          | None                                                                                                                                                                                        | Cooking a raw porkchop Killing pigs or hoglins with fire Receive 5 for 1 emerald at apprentice-level trade from butcher villager Raid gift from butcher villager‌[Java Edition  only]                                                                                                                       |
| Cooked Rabbit                             |      | 5 ()        | 6                            | 11                           | 1.2                          | None                                                                                                                                                                                        | Cooking raw rabbit Killing rabbits with fire Raid gift from butcher villager‌[Java Edition  only]                                                                                                                                                                                                           |
| Cooked Salmon                             |      | 6 ()        | 9.6                          | 15.6                         | 1.6                          | None                                                                                                                                                                                        | Cooking a raw salmon Killing salmon with fire‌[Java Edition  only] buried treasure chest‌[Java Edition  only] Receive 6 for 1 emerald + 1 raw salmon at apprentice-level trade from fisherman villager                                                                                                      |
| Cookie                                    |      | 2 ()        | 0.4                          | 2.4                          | 0.2                          | None                                                                                                                                                                                        | Crafting from wheat and cocoa beans Receive 18 for 3 emerald at journeyman-level trade from farmer villager                                                                                                                                                                                                 |
| Dried Kelp                                |      | 1 ()        | 0.6‌[JE  only]0.2‌[BE  only] | 1.6‌[JE  only]1.2‌[BE  only] | 0.6‌[JE  only]0.2‌[BE  only] | None                                                                                                                                                                                        | Smelting kelp in a furnace, smoker, or campfire Crafting from dried kelp block Raid gift from farmer villager‌[Java Edition  only]                                                                                                                                                                          |
| Enchanted Golden Apple                    |      | 4 ()        | 9.6                          | 13.6                         | 2.4                          | *RegenerationII for 20 seconds‌[Java Edition  only]Regeneration V for 30 seconds‌[Bedrock Edition  only] Absorption IV for 2 minutes Resistance for 5 minutes Fire Resistance for 5 minutes | Desert pyramid, dungeon, woodland mansion, mineshaft, and ancient city chests. This is the only food item in the game that is not renewable.                                                                                                                                                                |
| Golden Apple                              |      | 4 ()        | 9.6                          | 13.6                         | 2.4                          | *RegenerationII for 5 secondsAbsorption for 2 minutes                                                                                                                                       | Crafting from an apple and gold ingots Desert pyramid, dungeon, mineshaft, stronghold altar, woodland mansion, igloo, and big ocean ruins chests                                                                                                                                                            |
| Glow Berries                              |      | 2 ()        | 0.4                          | 2.4                          | 0.2                          | None                                                                                                                                                                                        | Collected from cave vines                                                                                                                                                                                                                                                                                   |
| Golden Carrot                             |      | 6 ()        | 14.4                         | 20.4                         | 2.4                          | None                                                                                                                                                                                        | Crafting a carrot with gold nuggets Receive 3 for 3 emerald at master-level trade from farmer villager                                                                                                                                                                                                      |
| Honey Bottle                              |      | 6 ()        | 1.2                          | 7.2                          | 0.2                          | ClearsPoison                                                                                                                                                                                | Crafting from honey block Collecting from beehives or bee nests                                                                                                                                                                                                                                             |
| Melon Slice                               |      | 2 ()        | 1.2                          | 3.2                          | 0.6                          | None                                                                                                                                                                                        | Harvesting a melon block                                                                                                                                                                                                                                                                                    |
| Mushroom Stew                             |      | 6 ()        | 7.2                          | 13.2                         | 1.2                          | None                                                                                                                                                                                        | Crafting with a bowl and one of each mushroom Using a bowl on a mooshroom                                                                                                                                                                                                                                   |
| Poisonous Potato                          |      | 2 ()        | 1.2                          | 3.2                          | 0.6                          | Poisonfor 5 seconds (60% chance)                                                                                                                                                            | Harvesting potato crops Shipwreck supply chest                                                                                                                                                                                                                                                              |
| Potato                                    |      | 1 ()        | 0.6                          | 1.6                          | 0.6                          | None                                                                                                                                                                                        | Killing zombies Harvesting potato crops Farmer villager who drop potato after harvesting potato crop bonus chest‌[Bedrock Edition  only] village plains and taiga house, pillager outpost, and shipwreck supply chest                                                                                       |
| Pufferfish                                |      | 1 ()        | 0.2                          | 1.2                          | 0.2(−4.8)[note 2]            | *HungerIII for 15 secondsNausea for 15 seconds Poison II for 60 seconds                                                                                                                     | Fishing Killing pufferfish Rare drop from guardians and elder guardian                                                                                                                                                                                                                                      |
| Pumpkin Pie                               |      | 8 ()        | 4.8                          | 12.8                         | 0.6                          | None                                                                                                                                                                                        | Crafting with a pumpkin, an egg, and sugar Receive 4 for 1 emerald at apprentice-level trade from farmer villager village taiga house chest Raid gift from farmer villager‌[Java Edition  only]                                                                                                             |
| Rabbit Stew                               |      | 10 ()       | 12                           | 22                           | 1.2                          | None                                                                                                                                                                                        | Crafting with a bowl, carrot, baked potato, mushroom, and cooked rabbit Receive 1 for 1 emerald at novice-level trade from butcher villager                                                                                                                                                                 |
| Raw Beef                                  |      | 3 ()        | 1.8                          | 4.8                          | 0.6                          | None                                                                                                                                                                                        | Killing cows, red mooshrooms, and brown mooshroom village butcher chest                                                                                                                                                                                                                                     |
| Raw Chicken                               |      | 2 ()        | 1.2                          | 3.2                          | 0.6(-2.075)[note 2]          | Hungerfor 30 seconds (30% chance)                                                                                                                                                           | Killing chickens Cat gift                                                                                                                                                                                                                                                                                   |
| Raw Cod                                   |      | 2 ()        | 0.4                          | 2.4                          | 0.2                          | None                                                                                                                                                                                        | Fishing Killing cod, guardians, elder guardians, dolphins, polar bears Rare drop from guardians and elder guardians village fisher barrel Raid gift from fisherman villager‌[Java Edition  only]                                                                                                            |
| Raw Mutton                                |      | 2 ()        | 1.2                          | 3.2                          | 0.6                          | None                                                                                                                                                                                        | Killing sheep village butcher chest                                                                                                                                                                                                                                                                         |
| Raw Porkchop                              |      | 3 ()        | 1.8                          | 4.8                          | 0.6                          | None                                                                                                                                                                                        | Killing pigs or hoglins village butcher chest                                                                                                                                                                                                                                                               |
| Raw Rabbit                                |      | 3 ()        | 1.8                          | 4.8                          | 0.6                          | None                                                                                                                                                                                        | Killing rabbits                                                                                                                                                                                                                                                                                             |
| Raw Salmon                                |      | 2 ()        | 0.4                          | 2.4                          | 0.2                          | None                                                                                                                                                                                        | Fishing Killing salmon and polar bears Rare drop from guardians and elder guardians Raid gift from fisherman villager‌[Java Edition  only] village fisher barrel‌[Java Edition  only] bonus chest                                                                                                           |
| Rotten Flesh                              |      | 4 ()        | 0.8                          | 4.8                          | 0.2(-1.8)[note 2]            | Hungerfor 30 seconds (80% chance)                                                                                                                                                           | Killing zombies, zombified piglins, zombie villagers, husks, drowned, and zombie horses dungeon, igloo, woodland mansion, small ocean ruins, village temple, shipwreck supply, desert, and jungle pyramid chests Caught as junk from fishing Cat gift                                                       |
| Spider Eye                                |      | 2 ()        | 3.2                          | 5.2                          | 1.6(-2.2)[note 3]            | Poisonfor 5 seconds                                                                                                                                                                         | Killing spiders and cave spiders Killing a witch                                                                                                                                                                                                                                                            |
| Steak                                     |      | 8 ()        | 12.8                         | 20.8                         | 1.6                          | None                                                                                                                                                                                        | Cooking raw beef Killing cows, red mooshrooms, or brown mooshrooms with fire Raid gift from butcher villager‌[Java Edition  only]                                                                                                                                                                           |
| Suspicious Stew                           |      | 6 ()        | 7.2                          | 13.2                         | 1.2                          | The following for 3-11 seconds, depending on the flower used:Regeneration Jump Boost Poison Wither Weakness Blindness Fire Resistance Saturation Night Vision                               | Crafting with a bowl, red mushroom, brown mushroom, and any flower Feed brown mooshroom any flower then using a bowl on brown mooshroom Receive 1 for 1 emerald at expert-level trade of farmer villager, excluding Fire Resistance and Wither.                                                             |
| Suspicious Stew(Together with Saturation) |      | 13 ( × 6.5) | 21.2                         | 34.2                         | 1.6307692307692              | Effect ofSaturationalready added to total points restored                                                                                                                                   | Crafting with a bowl, red mushroom, brown mushroom, and Dandelion or Blue Orchid Feed brown mooshroom a dandelion or blue orchid then using a bowl on brown mooshroom Receive 1 for 1 emerald at expert-level trade of farmer villager                                                                      |
| Sweet Berries                             |      | 2 ()        | 0.4‌[JE  only]1.2‌[BE  only] | 2.4‌[JE  only]3.2‌[BE  only] | 0.2‌[JE  only]0.6‌[BE  only] | None                                                                                                                                                                                        | Breaking sweet berry bushes Picking ripe berries from sweet berry bushes (right-click) Taiga village house chests.‌[Java Edition  only]                                                                                                                                                                     |
| Tropical Fish                             |      | 1 ()        | 0.2                          | 1.2                          | 0.2                          | None                                                                                                                                                                                        | Fishing Killing tropical fish Rare drop from guardians and elder guardians                                                                                                                                                                                                                                  |


↑ Food Points + Saturation, which gives roughly how long the food can last. See hunger for details.  This value is reduced if the player is near the food or saturation cap, as excess points of either type are wasted.

↑ a b c Average expected food quality if food poisoning isn't cured. Food poisoning lasts 30 seconds from the last food that inflicted it, and drains nearly 2 shanks of hunger over that duration.  The loss comes from saturation before visible hunger.

↑ Food quality if poison isn't cured; healing the damage from poison quickly drains the hunger bar.




## Food poisoning
Main article: Hunger (status effect)