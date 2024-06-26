# Custom biome
Biomes stored as JSON files within a data pack in the path data/<namespace>/worldgen/biome.

## Contents
- 1 JSON format
- 2 History
- 3 External links
- 4 References

## JSON format
- : The root object.
	- has_precipitation: Determines whether or not the biome has precipitation.
	- temperature: Controls gameplay features like grass and foliage color, and a height adjusted temperature (which controls whether raining or snowing ifhas_precipitationistrue, and generation details of some features).
	- temperature_modifier: (optional, defaults to none) Eithernoneorfrozen. Modifies temperature before calculating the height adjusted temperature. Iffrozen, makes some places' temperature high enough to rain (0.2).
	- downfall: Controls grass and foliage color.
	- effects: Ambient effects in this biome.
		- fog_color: (Required, but the normal value for the overworld is 12638463) Decimal value converted from Hex color to use for fog.
		- sky_color: Decimal value converted from Hex color to use for the sky.
		- water_color: (Required, but the normal value is 4159204) Decimal value converted from Hex color to use for water blocks and cauldrons.
		- water_fog_color: (Required, but the normal value is 329011) Decimal value converted from Hex color to use for fog underwater.
		- foliage_color: (optional) Decimal value converted from Hex color to use for tree leaves and vines. If not present, the value depends on downfall and the temperature.
		- grass_color: (optional) Decimal value converted from Hex color to use for grass blocks, short grass, tall grass, ferns, tall ferns, and sugar cane. If not present, the value depends on downfall and temperature.
		- grass_color_modifier: (optional, defaults to none) Can benone,dark_forestorswamp.
		- particle: (optional) Theparticleto use throughout this biome.
			- probability: Controls how often the particle spawns. Value higher than 1 is regarded as 1, lower than 0 is regarded as 0.
			- options: Controls what particle to use. See alsoCommands/particle.
				- type: The namespaced id of the particle type.If type is block, block_marker or falling_dust, additional field are as follows:
				- value: Contains the block state used for the particle.
					- 
					- Block state
				- value: Contains the item data used for the particle.
					- id: Namespaced id of the item to use.
					- Count: The amount of the item.
					- tag: NBT data present on the item in JSON format. SeeNBT format#JSON and NBT.
				- color: Three floats representing the red, green, and blue components of the dust color, each from 0 to 1.
				- scale: Controls the size of the dust particles.If type is dust_color_transition, additional fields are as follows:
				- fromColor: Three floats representing the red, green, and blue components of the start color, each from 0 to 1.
				- toColor: Three floats representing the red, green, and blue components of the end color, each from 0 to 1.
				- scale: Controls the size of the particles.If type is sculk_charge, additional field is as follows:
				- roll: The angle the particle displays at inradians.If type is vibration, additional fields are as follows:
				- destination: The destination.
					- 
					- A position source
				- arrival_in_ticks: The duration of the move.If type is shriek, additional field is as follows:
				- delay: The delay in ticks.
		- ambient_sound: (optional) A namespace ID of the sound event to use for ambient sound. Can also be an object to specify a fixed audible range of the sound.
			- sound_id: A namespace ID of the sound event to use.
			- range: (optional) The fixed audible range of the sound.
		- mood_sound: (optional) Settings formoodsound.
			- sound: A namespace ID of the sound event to use. Can also be an object to specify a fixed range of the sound.
				- sound_id: A namespace ID of the sound event to use.
				- range: (optional) The fixed audible range of the sound.
			- tick_delay: The mininum delay between two plays. See alsoAmbience#Mood_algorithm.
			- block_search_extent: Determines the cubic range of possible positions to find place to play the mood sound. The player is at the center of the cubic range, and the edge length is2 * block_search_extent.
			- offset: The higher the value makes the sound source further away from the player.
		- additions_sound: (optional) Settings for additions sound.
			- sound: A namespace ID of the sound event to use. Can also be an object to specify a fixed range of the sound.
				- sound_id: A namespace ID of the sound event to use.
				- range: (optional) The fixed audible range of the sound.
			- tick_chance: The propability to start playing the sound per tick. Value higher than 1 is regarded as 1, lower than 0 is regarded as 0.
		- music: (optional) Specific music that should be played in the biome.
			- sound: A namespace ID of the sound event to use. Can also be an object to specify a fixed range of the sound.
				- sound_id: A namespace ID of the sound event to use.
				- range: (optional) The fixed audible range of the sound.
			- min_delay: The min delay between two music.
			- max_delay: The max delay between two music.
			- replace_current_music: Whether or not to replace music which is already playing.
	- carvers: Thecarversto use.
		- air:carver(referenced byID orinlined), or carver#tagorlist (containing eitherIDs orinlined objects) (Optional; can be empty) — Carvers for theaircave generation step.
		- liquid:carver(referenced byID orinlined), or carver#tagorlist (containing eitherIDs orinlined objects) (Optional; can be empty) — Carvers for theliquidcave generation step. Currently doesn't work.
	- features: List of generation steps (Can be empty). Usually there are 11 steps, but any amount is possible.
		- each entry of the list:placed feature#tagorlist (containing eitherIDs orinlined objects) — Features to place during that generation step. The same placed features in the same step in two biomes cannot be in different orders. In each step, all feature IDs need to be ordered consistently across biomes. For example, in UNDERGROUND_ORES step of minecraft:plains, ore_dirt is before ore_gravel, so in other biomes' UNDERGROUND_ORES step, if there are ore_dirt and ore_gravel, ore_gravel cannot be after ore_dirt.
	- creature_spawn_probability: (optional) Higher value results in more creatures spawned in world generation. Must be between 0.0 and 0.9999999 (both inclusive).
	- spawners: (Required, but can be empty. If this object doesn't contain a certain category, mobs in this category do not spawn.) Entity spawning settings.
		- <mob category>: (Can be empty. If empty, mobs in this category do not spawn.) The key must be one ofmonster,creature,ambient,water_creature,underground_water_creature,water_ambient,misc, oraxolotls. A list of spawner data objects, one for each mob which should spawn in this biome.
			- : The spawner data for a single mob.
				- type: The namespaced entity id of the mob.
				- weight: How often this mob should spawn, higher values produce more spawns.
				- minCount: The minimum count of mobs to spawn in a pack. Must be greater than 0.
				- maxCount: The maximum count of mobs to spawn in a pack. Must be greater than 0. And must be not less thanminCount.
	- spawn_costs: (Required, but can be empty. Only mobs listed here use the spawn cost mechanism) SeeSpawn#Spawn costsfor details.
		- <entity id>: The namespaced entity id of the mob.
			- energy_budget: New mob's maximum potential.
			- charge: New mob's charge.

An interactive widget is being loaded. If this does not work for you, please reload the page or check if JavaScript is enabled.
