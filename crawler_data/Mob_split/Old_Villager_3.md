### Regeneration
When a villager gives off particles from a new trade, they get 10 seconds of Regeneration I, which gives them 4.

Commands or external editors can help villagers get new trades. 

If a villager unintentionally picks up certain seeds or crops, it throws it to another villager to simulate trading between the villagers.

## Data values
### ID
Java Edition:

| Name     | Identifier | Translation key           |
|----------|------------|---------------------------|
| Villager | villager   | entity.minecraft.villager |

Bedrock Edition:

| Name     | Identifier | Numeric ID | Translation key      |
|----------|------------|------------|----------------------|
| Villager | villager   | 15         | entity.villager.name |

### Entity data
See also: Chunk format

Villagers have entity data associated with them that contains various properties.




 Entity data
Tags common to all entities
Tags common to all mobs
Additional fields for mobs that can breed
 Profession: The ID of the texture used for this villager. This also influences trading options.
 Riches: Currently unused. Increases by the number of emeralds traded to a villager any time they are traded.
 Career: The ID of this villager's career. This also influences trading options and the villager's name in the GUI (if it does not have a CustomName). If 0, the next time offers are refreshed, the game assigns a new Career and resets CareerLevel to 1.
 CareerLevel: The current level of this villager's trading options. Influences the trading options generated by the villager; if it is greater than their career's maximum level, no new offers are generated. Increments when a trade causes offers to be refreshed. If 0, the next trade to do this assigns a new Career and sets CareerLevel to 1. Set to a high enough level causes no new trades to release (Career must be set to 1 or above).
 Willing: 1 or 0 (true/false) - true if the villager is willing to mate. Becomes true after certain trades (those which would cause offers to be refreshed), and false after mating.
 Inventory: Each compound tag in this list is an item in the villager's inventory, up to a maximum of 8 slots. Items in two or more slots that can be stacked together are automatically condensed into one slot. If there are more than 8 slots, the last slot is removed until the total is 8. If there are 9 slots but two previous slots can be condensed, the last slot remains after the two other slots are combined.
 An item in the inventory, excluding the Slot tag.
Tags common to all items
 Offers: Is generated when the trading menu is opened for the first time.
 Recipes: List of trade options.
 A trade option.
 rewardExp: 1 or 0 (true/false) - true if this trade provides XP orb drops. All trades from naturally-generated villagers in Java Edition reward XP orbs.
 maxUses: The maximum number of times this trade can be used before it is disabled. Increases by a random amount from 2 to 12 when offers are refreshed.
 uses: The number of times this trade has been used. The trade becomes disabled when this is greater or equal to maxUses.
 buy: The first 'cost' item, without the Slot tag.
Tags common to all items
 buyB: May not exist. The second 'cost' item, without the Slot tag.
Tags common to all items
 sell: The item being sold for each set of cost items, without the Slot tag.
Tags common to all items


