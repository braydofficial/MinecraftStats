from mcstats import mcstats

mining_blocks = [
    "minecraft:obsidian",
    "minecraft:ancient_debris",
    "minecraft:coal_ore",
    "minecraft:deepslate_coal_ore",
    "minecraft:iron_ore",
    "minecraft:deepslate_iron_ore",
    "minecraft:copper_ore",
    "minecraft:diamond_ore",
    "minecraft:deepslate_diamond_ore",
    "minecraft:gold_ore",
    "minecraft:deepslate_gold_ore",
    "minecraft:nether_gold_ore",
    "minecraft:emerald_ore",
    "minecraft:deepslate_emerald_ore",
    "minecraft:lapis_ore",
    "minecraft:deepslate_lapis_ore",
    "minecraft:redstone_ore",
    "minecraft:deepslate_redstone_ore",
    "minecraft:nether_quartz_ore",
    "minecraft:pointed_dripstone",
    "minecraft:stone",
    "minecraft:andesite",
    "minecraft:blackstone",
    "minecraft:basalt",
    "minecraft:calcite",
    "minecraft:deepslate",
    "minecraft:diorite",
    "minecraft:dripstone",
    "minecraft:granite",
    "minecraft:smooth_basalt",
    "minecraft:tuff",
    "minecraft:infested_.+"
]

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_miningblocks',
        {
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:mined'], mining_blocks)
    )
)
