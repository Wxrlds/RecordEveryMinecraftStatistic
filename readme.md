A Minecraft Datapck dedicated towards adding every single Minecraft statistic as a Scoreboard.

It automatically tracks and updates every statistic.

Generator compatible with Minecraft 1.18+

Feel free to join me on Discord for help https://discord.gg/hsae7DJ

## Usage:

Ingame you have to run "/scoreboard objectives setdisplay sidebar [scoreboard name here]" for it to display the desired Scoreboard on the Sidebar.

The scoreboard names consist of a prefix_ and the registry ID but the colon: is replaced with a underscore_.

Prefixes:
- g (for general)
- k (for killed [number of mob])
- b (for broken)
- c (for crafted)
- cu (for custom)
- q (for dropped)
- d (for deaths [by number of mob])
- m (for mined)
- p (for picked up)
- u (for used/placed)

Keep in mind you have to be a server operator to use this command

## Examples for Scoreboard names:

The Scoreboard names are oriented on the Registry ID you get when howering over an item with F3+H enabled/when looking at a block with F3 open


[You can also find a list of all available scores here](https://github.com/Wxrlds/RecordEveryMinecraftStatistic/blob/master/Datapack/data/rems/functions/setup.mcfunction)

- ``g_totalKills`` shows how many Entities you have killed in total

![grafik](https://user-images.githubusercontent.com/42120270/91225660-458e1600-e724-11ea-9655-8b8012192e48.png)

- ``k_minecraft_sheep`` shows how many Sheep you have killed

![grafik](https://user-images.githubusercontent.com/42120270/91225819-7cfcc280-e724-11ea-8bd3-1c10715bbec1.png)

- ``b_minecraft_golden_hoe`` shows how many Golden Hoes you have broken

![grafik](https://user-images.githubusercontent.com/42120270/91225490-f8aa3f80-e723-11ea-83e8-a25058bda633.png)

- ``q_minecraft_ocelot_spawn_egg`` shows how many Ocelet Spawn Eggs you have dropped

![grafik](https://user-images.githubusercontent.com/42120270/91226023-bd5c4080-e724-11ea-9e53-47774dc28c11.png)

## Installation guide:

If you want to add it to a newly generated world, on the world generaton screen you have the possibility to include a datapack by default.
Or on a server, create a folder and name it like the server would (specified in the server.properties) and in this folder create another folder called "datapacks" and place the zip in it.

If you want to add it to an existing world, you open its world folder, enter the datapacks folder and move the zip file in that datapacks folder. Ingame you might have to run ``/reload`` for the pack to be loaded.
The Datapack won't be able to display previously increased statistics and you have to manually add them to your stats if you want both, your ingame statistics and the datapack to display the same score.

## Scoreboard creation guide:

- Install [TellMe](https://www.curseforge.com/minecraft/mc-mods/tellme)
- Use it to dump all blocks, entities, items, stat-types (and manually create a general.csv dump)
- Place the dumped files under MCAllStatsGenerator/dumps
- run main.py found under MCAllStatsGenerator