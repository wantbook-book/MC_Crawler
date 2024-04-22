# Statistics
Statistics is a game feature that allows players to track certain tasks in the form of numerical data.

Statistics are present only in Java Edition. Bedrock Edition has no equivalent of statistics in-game, but a part of statistics can be viewed on the Xbox Console Companion app.

## Contents
- 1 Statistics screen
- 2 Resource location
	- 2.1 Statistic types and names
	- 2.2 List of custom statistic names
- 3 Storage
- 4 History
- 5 Issues
- 6 Gallery
- 7 References

## Statistics screen
In statistics screen, statistics are divided into three sections: 

- General– The General screen displays a multitude of generic statistics that are listed in the table below.
- Items– The Items screen displays the number of times different items and blocks have been depleted, crafted, used to destroy blocks, picked up and dropped.
- Mobs– The Mob screen shows for each different type of mobs or other living entities (players,armor stands) how many the player has killed, or the number of deaths caused by those mobs.

The buttons at the top of the Items screen can be used to sort the list. The General and Mobs screens are sorted alphabetically.

## Resource location
The resource locations of statistics are unique. They are the only combination resource locations in the game.

The resource locations of statistics are in form of NAMESPACE:PATH as well, however, in which NAMESPACE is the resource location of a statistic type in form of namespace.path, NAME is the resource location of a statistic name in form of namespace.path.

That means, the resource locations of statistics are in form of A.B:C.D, in which:

- Ais the namespace of statistic type.
- Bis the path of statistic type.
- Cis the namespace of statistic name.
- Dis the path of statistic name.

For both two namespaces, it can be omitted if it is minecraft. For example, the following four locations work the same:

- minecraft.mined:minecraft.stone
- mined:minecraft.stone
- minecraft.mined:stone
- mined:stone

### Statistic types and names
Statistics are divided into some types. For general statistics, their type is called minecraft:custom. For item statistics, their types are minecraft:mined, minecraft:broken, minecraft:crafted, minecraft:used, minecraft:picked_up, and minecraft:dropped. For mob statistics, their types are minecraft:killed and minecraft:killed_by. 

| Statistic type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Resource location   |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| CUSTOM           | A multitude of generic statistics related to a player's actions. Players' statistics increase automatically when they perform the action relevant to the statistic names.The statistic name for CUSTOM is used to specify the action for statistics. See #List of custom statistic names below.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | minecraft:custom    |
| BLOCK_MINED      | Statistic related to the number of blocks a player mined. Players' statistic increases when the player mines a block of the specified type, only if they use a tool that would normally make the item drop (even if custom loot tables or the doTileDrops game rule being false result in no drops). It never increases for a player in Creative Mode.The statistic name for BLOCK_MINED is used to specify the type of blocks. It can be the resource location of any block.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | minecraft:mined     |
| ITEM_BROKEN      | Statistics related to the number of items a player ran their durability negative. Players' statistic increases when a player runs the durability of one item of the specified type negative. Durability runs negative when the item's durability loss–condition is met and the item already has a durability of 0.The statistic name for ITEM_BROKEN is used to specify the type of items. It can be the resource location of any item or block for which items exist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | minecraft:broken    |
| ITEM_CRAFTED     | Statistics related to the number of items crafted, smelted, etc. Players' statistic increases by an amount equal to the number of items crafted or smelted, upon removing a block or item from the output of an interface, like a crafting table, a furnace, or a villager's output slot.The statistic name for ITEM_CRAFTED is used to specify the type of items. It can be the resource location of any item or block for which items exist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | minecraft:crafted   |
| ITEM_USED        | Statistics related to the number of block or item used. Players' statistic increases when a player uses a block or item. "Use" is defined as when:A shovel, a pickaxe, an axe, flint and steel, shears, a hoe, a bow, or a sword would normally consume durability Players' statistics do not increase when armor consumes durability. Instead, they increase when armor is equipped directly with use. Players' statistics increase even if no durability is consumed, like when a torch is destroyed with an item that takes the destroy key to use (e.g. pickaxes).<br/>For the fishing rod, carrot on a stick and warped fungus on a stick, the use key is used.<br/>A block is placed<br/>A painting, item frame, snowball, egg, spawn egg, any type of minecart or boat, eye of ender, ender pearl, bow, any type of throwable potion, Bottle o' Enchanting, or fishing rod spawns an entity<br/>A cocoa pod is planted on a jungle log, or bone meal is used to grow plants like crops, grass, and saplings<br/>A potion, bucket of milk, or any food (save cake) is consumed<br/>An empty map, empty bucket, lava bucket, water bucket, milk bucket, book and quill, or potion turns into a new item Players' statistics do not increase when a bowl becomes mushroom stew or a bucket becomes milk.<br/>A music disc is placed in a jukebox<br/>Players' statistics do not increase when items are used on mobs—whether to name, tame, feed, breed, saddle, leash, shear, dye, milk, or gather stew from—when leather armor is washed in a cauldron, and instances mentioned above.The statistic name for ITEM_USED is used to specify the type of items. It can be the resource location of any item or block for which items exist. | minecraft:used      |
| ITEM_PICKED_UP   | Statistics related to the number of dropped items a player picked up. Players' statistic increases when the player picks up a dropped item of the specified type.The statistic name for ITEM_PICKED_UP is used to specify the type of items. It can be the resource location of any item or block for which items exist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | minecraft:picked_up |
| ITEM_DROPPED     | Statistics related to the number of items that droped. Players' statistic increases when a player drops an item of the specified type from inventory.The statistic name for ITEM_DROPPED is used to specify the type of items. It can be the resource location of any item or block for which items exist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | minecraft:dropped   |
| ENTITY_KILLED    | Statistics related to the number of entities a player killed. Players' statistic increases when a player kills an entity of the specified type.The statistic name for ENTITY_KILLED is used to specify the type of entities. It can be the resource location of any entity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | minecraft:killed    |
| ENTITY_KILLED_BY | Statistics related to the times of a player being killed by entities. Players' statistic increases when the player is killed by an entity of the specified type.The statistic name for ENTITY_KILLED is used to specify the type of entities. It can be the resource location of any entity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | minecraft:killed_by |
