function rems:setup

team add dems_statistics
team modify dems_statistics color white

scoreboard objectives add dems_cu_minecraft_sneak_time minecraft.custom:minecraft.sneak_time

scoreboard objectives setdisplay list g_health
scoreboard objectives setdisplay belowName g_health