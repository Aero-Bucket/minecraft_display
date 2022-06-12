# as /give will summon item at player position,
# need to check if item is thrown by player before setblock
# ab_placepos 0=place in front of head, 1=place under foot
execute store success score ab_dummy ab_fromplayer run data get entity @s Thrower
execute if score ab_dummy ab_fromplayer matches 1 if score ab_setting ab_placepos matches 0 run execute as @p at @s run setblock ^ ^1 ^1 minecraft:obsidian keep
execute if score ab_dummy ab_fromplayer matches 1 if score ab_setting ab_placepos matches 1 run execute as @p at @s run setblock ~ ~-1 ~ minecraft:obsidian keep
kill @s
