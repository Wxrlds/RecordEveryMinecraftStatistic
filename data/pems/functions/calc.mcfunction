scoreboard players add @a[scores={pems_calc_cu_minecraft_aviate_one_m=100..}] pems_cu_minecraft_aviate_one_m 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_aviate_one_m=100..}] pems_calc_cu_minecraft_aviate_one_m 100
scoreboard players add @a[scores={pems_calc_cu_minecraft_aviate_one_km=100000..}] pems_cu_minecraft_aviate_one_km 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_aviate_one_km=100000..}] pems_calc_cu_minecraft_aviate_one_km 100000

scoreboard players add @a[scores={pems_calc_cu_minecraft_boat_one_m=100..}] pems_cu_minecraft_boat_one_m 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_boat_one_m=100..}] pems_calc_cu_minecraft_boat_one_m 100
scoreboard players add @a[scores={pems_calc_cu_minecraft_boat_one_km=100000..}] pems_cu_minecraft_boat_one_km 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_boat_one_km=100000..}] pems_calc_cu_minecraft_boat_one_km 100000

scoreboard players add @a[scores={pems_calc_cu_minecraft_fly_one_m=100..}] pems_cu_minecraft_fly_one_m 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_fly_one_m=100..}] pems_calc_cu_minecraft_fly_one_m 100
scoreboard players add @a[scores={pems_calc_cu_minecraft_fly_one_km=100000..}] pems_cu_minecraft_fly_one_km 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_fly_one_km=100000..}] pems_calc_cu_minecraft_fly_one_km 100000

scoreboard players add @a[scores={pems_calc_cu_minecraft_horse_one_m=100..}] pems_cu_minecraft_horse_one_m 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_horse_one_m=100..}] pems_calc_cu_minecraft_horse_one_m 100
scoreboard players add @a[scores={pems_calc_cu_minecraft_horse_one_km=100000..}] pems_cu_minecraft_horse_one_km 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_horse_one_km=100000..}] pems_calc_cu_minecraft_horse_one_km 100000

scoreboard players add @a[scores={pems_calc_cu_minecraft_minecart_one_m=100..}] pems_cu_minecraft_minecart_one_m 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_minecart_one_m=100..}] pems_calc_cu_minecraft_minecart_one_m 100
scoreboard players add @a[scores={pems_calc_cu_minecraft_minecart_one_km=100000..}] pems_cu_minecraft_minecart_one_km 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_minecart_one_km=100000..}] pems_calc_cu_minecraft_minecart_one_km 100000

scoreboard players add @a[scores={pems_calc_cu_minecraft_pig_one_m=100..}] pems_cu_minecraft_pig_one_m 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_pig_one_m=100..}] pems_calc_cu_minecraft_pig_one_m 100
scoreboard players add @a[scores={pems_calc_cu_minecraft_pig_one_km=100000..}] pems_cu_minecraft_pig_one_km 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_pig_one_km=100000..}] pems_calc_cu_minecraft_pig_one_km 100000

scoreboard players add @a[scores={pems_calc_cu_minecraft_play_time=1200..}] pems_cu_minecraft_play_time_min 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_play_time=1200..}] pems_calc_cu_minecraft_play_time 1200

scoreboard players add @a[scores={pems_calc_cu_minecraft_sneak_time=1200..}] pems_cu_minecraft_sneak_time_min 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_sneak_time=1200..}] pems_calc_cu_minecraft_sneak_time 1200

scoreboard players add @a[scores={pems_calc_cu_minecraft_sprint_one_m=100..}] pems_cu_minecraft_sprint_one_m 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_sprint_one_m=100..}] pems_calc_cu_minecraft_sprint_one_m 100
scoreboard players add @a[scores={pems_calc_cu_minecraft_sprint_one_km=100000..}] pems_cu_minecraft_sprint_one_km 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_sprint_one_km=100000..}] pems_calc_cu_minecraft_sprint_one_km 100000

scoreboard players add @a[scores={pems_calc_cu_minecraft_strider_one_m=100..}] pems_cu_minecraft_strider_one_m 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_strider_one_m=100..}] pems_calc_cu_minecraft_strider_one_m 100
scoreboard players add @a[scores={pems_calc_cu_minecraft_strider_one_km=100000..}] pems_cu_minecraft_strider_one_km 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_strider_one_km=100000..}] pems_calc_cu_minecraft_strider_one_km 100000

scoreboard players add @a[scores={pems_calc_cu_minecraft_swim_one_m=100..}] pems_cu_minecraft_swim_one_m 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_swim_one_m=100..}] pems_calc_cu_minecraft_swim_one_m 100
scoreboard players add @a[scores={pems_calc_cu_minecraft_swim_one_km=100000..}] pems_cu_minecraft_swim_one_km 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_swim_one_km=100000..}] pems_calc_cu_minecraft_swim_one_km 100000

execute as @a[scores={cu_minecraft_time_since_death=0}] run scoreboard players set @s pems_cu_minecraft_time_since_death_min 0
scoreboard players add @a[scores={pems_calc_cu_minecraft_time_since_death=1200..}] pems_cu_minecraft_time_since_death_min 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_time_since_death=1200..}] pems_calc_cu_minecraft_time_since_death 1200

execute as @a[scores={cu_minecraft_time_since_rest=0}] run scoreboard players set @s pems_cu_minecraft_time_since_rest_min 0
scoreboard players add @a[scores={pems_calc_cu_minecraft_time_since_rest=1200..}] pems_cu_minecraft_time_since_rest_min 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_time_since_rest=1200..}] pems_calc_cu_minecraft_time_since_rest 1200

scoreboard players add @a[scores={pems_calc_cu_minecraft_walk_on_water_one_m=100..}] pems_cu_minecraft_walk_on_water_one_m 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_walk_on_water_one_m=100..}] pems_calc_cu_minecraft_walk_on_water_one_m 100
scoreboard players add @a[scores={pems_calc_cu_minecraft_walk_on_water_one_km=100000..}] pems_cu_minecraft_walk_on_water_one_km 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_walk_on_water_one_km=100000..}] pems_calc_cu_minecraft_walk_on_water_one_km 100000

scoreboard players add @a[scores={pems_calc_cu_minecraft_walk_one_m=100..}] pems_cu_minecraft_walk_one_m 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_walk_one_m=100..}] pems_calc_cu_minecraft_walk_one_m 100
scoreboard players add @a[scores={pems_calc_cu_minecraft_walk_one_km=100000..}] pems_cu_minecraft_walk_one_km 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_walk_one_km=100000..}] pems_calc_cu_minecraft_walk_one_km 100000

scoreboard players add @a[scores={pems_calc_cu_minecraft_walk_under_water_one_m=100..}] pems_cu_minecraft_walk_under_water_one_m 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_walk_under_water_one_m=100..}] pems_calc_cu_minecraft_walk_under_water_one_m 100
scoreboard players add @a[scores={pems_calc_cu_minecraft_walk_under_water_one_km=100000..}] pems_cu_minecraft_walk_under_water_one_km 1
scoreboard players remove @a[scores={pems_calc_cu_minecraft_walk_under_water_one_km=100000..}] pems_calc_cu_minecraft_walk_under_water_one_km 100000