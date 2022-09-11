execute as @a[x_rotation=-90,scores={dems_cu_minecraft_sneak_time=1..},nbt={SelectedItemSlot:0}] run scoreboard objectives setdisplay sidebar.team.white pems_cu_minecraft_play_time_min

execute as @a[x_rotation=-90,scores={dems_cu_minecraft_sneak_time=1..},nbt={SelectedItemSlot:1}] run scoreboard objectives setdisplay sidebar.team.white cu_minecraft_deaths

execute as @a[x_rotation=-90,scores={dems_cu_minecraft_sneak_time=1..},nbt={SelectedItemSlot:2}] run scoreboard objectives setdisplay sidebar.team.white pems_cu_minecraft_time_since_death_min

execute as @a[x_rotation=-90,scores={dems_cu_minecraft_sneak_time=1..},nbt={SelectedItemSlot:3}] run scoreboard objectives setdisplay sidebar.team.white g_level

execute as @a[x_rotation=-90,scores={dems_cu_minecraft_sneak_time=1..},nbt={SelectedItemSlot:4}] run scoreboard objectives setdisplay sidebar.team.white pems_cu_minecraft_aviate_one_km

execute as @a[x_rotation=-90,scores={dems_cu_minecraft_sneak_time=1..},nbt={SelectedItemSlot:5}] run scoreboard objectives setdisplay sidebar.team.white g_totalKillCount

execute as @a[x_rotation=-90,scores={dems_cu_minecraft_sneak_time=1..},nbt={SelectedItemSlot:6}] run scoreboard objectives setdisplay sidebar.team.white cu_minecraft_jump

execute as @a[x_rotation=-90,scores={dems_cu_minecraft_sneak_time=1..},nbt={SelectedItemSlot:7}] run scoreboard objectives setdisplay sidebar.team.white c_minecraft_crafting_table

execute as @a[x_rotation=-90,scores={dems_cu_minecraft_sneak_time=1..},nbt={SelectedItemSlot:8}] run scoreboard objectives setdisplay sidebar.team.white m_minecraft_stone


team leave @a[team=dems_statistics]
team join dems_statistics @a[x_rotation=-90,scores={dems_cu_minecraft_sneak_time=1..}]
scoreboard players set @a[scores={dems_cu_minecraft_sneak_time=1..}] dems_cu_minecraft_sneak_time 0