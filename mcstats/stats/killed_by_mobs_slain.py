from mcstats import mcstats

mobList = [
    "minecraft:zombie",
    "minecraft:iron_golem",
    "minecraft:zombified_piglin",
    "minecraft:piglin",
    "minecraft:hoglin",
    "minecraft:ravager",
    "minecraft:wither_skeleton",
    "minecraft:zoglin",
    "minecraft:zombie_villager"
]

mcstats.registry.append(
    mcstats.MinecraftStat(
        'killed_by_mobs_slain',
        {
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:killed_by'], mobList)
        mcstats.StatReader()
    ))
