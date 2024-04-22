# Polished Blackstone Wall
A polished blackstone wall is a polished blackstone variant of a wall.

## Contents
- 1 Obtaining
	- 1.1 Breaking
	- 1.2 Crafting
	- 1.3 Stonecutting
- 2 Usage
	- 2.1 Note blocks
- 3 Sounds
- 4 Data values
	- 4.1 ID
	- 4.2 Block states
- 5 History
- 6 Issues

## Obtaining
### Breaking
Polished blackstone walls can be mined using any pickaxe. If mined without a pickaxe, they drop nothing.

| Block     | Polished Blackstone Wall |
|-----------|--------------------------|
| Hardness  | 2                        |
| Tool      |                          |
|           | Breakingtime (sec)[A]    |
| Default   | 10                       |
| Wooden    | 1.5                      |
| Stone     | 0.75                     |
| Iron      | 0.5                      |
| Diamond   | 0.4                      |
| Netherite | 0.35                     |
| Golden    | 0.25                     |

1. ↑Times are for unenchanted tools as used by players with no status effects, measured in seconds. For more information, see Breaking Speed.

### Crafting
| Ingredients         | Crafting recipe |
|---------------------|-----------------|
| Polished Blackstone | 6               |

### Stonecutting
| Ingredients                          | Cutting recipe |
|--------------------------------------|----------------|
| Blackstoneor<br/>Polished Blackstone |                |

## Usage
For information about the placement mechanics of all walls, see Wall § Usage.

### Note blocks
Polished blackstone walls can be placed under note blocks to produce "bass drum" sounds.

## Data values
### ID
Java Edition:

| Name                     | Identifier                | Form         | Block tags | Item tags | Translation key                           |
|--------------------------|---------------------------|--------------|------------|-----------|-------------------------------------------|
| Polished Blackstone Wall | `polishd_blackstone_wall` | Block & Item | `walls`    | `walls`   | `block.minecraft.polishd_blackstone_wall` |

Bedrock Edition:

| Name                     | Identifier                 | Numeric ID | Form                       | Item ID[i 1]   | Translation key                      |
|--------------------------|----------------------------|------------|----------------------------|----------------|--------------------------------------|
| Polished Blackstone Wall | `polished_blackstone_wall` | `552`      | Block & Giveable Item[i 2] | Identical[i 3] | `tile.polished_blackstone_wall.name` |

1. ↑ID of block's direct item form, which is used in savegame files and addons.
2. ↑Available with /give command.
3. ↑The block's direct item form has the same id as the block.

### Block states
Java Edition

| Name        | Default value | Allowed values              | Description                                                  |
|-------------|---------------|-----------------------------|--------------------------------------------------------------|
| east        | `none`        | `low`<br/>`none`<br/>`tall` | How the wall extends from the center post to the east.       |
| north       | `none`        | `low`<br/>`none`<br/>`tall` | How the wall extends from the center post to the north.      |
| south       | `none`        | `low`<br/>`none`<br/>`tall` | How the wall extends from the center post to the south.      |
| up          | `true`        | `false`<br/>`true`          | When true, the wall has a center post.                       |
| waterlogged | `false`       | `false`<br/>`true`          | Whether or not there's water in the same place as this wall. |
| west        | `none`        | `low`<br/>`none`<br/>`tall` | How the wall extends from the center post to the west.       |

Bedrock Edition

| Name                       | Metadata Bits | Default value | Allowed values                | Values forMetadata Bits | Description                                             |
|----------------------------|---------------|---------------|-------------------------------|-------------------------|---------------------------------------------------------|
| wall_connection_type_east  | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the east.  |
| wall_connection_type_north | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the north. |
| wall_connection_type_south | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the south. |
| wall_connection_type_west  | Not Supported | `none`        | `none`<br/>`short`<br/>`tall` | `Unsupported`           | How the wall extends from the center post to the west.  |
| wall_post_bit              | Not Supported | `true`        | `false`<br/>`true`            | `Unsupported`           | Whether or not the wall has a center post.              |


