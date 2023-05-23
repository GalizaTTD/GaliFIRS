from industry import IndustryPrimaryNoSupplies, TileLocationChecks

industry = IndustryPrimaryNoSupplies(
    id="water_plant",
    accept_cargo_types=[],
    prod_cargo_types_with_multipliers=[
        ("WATR", 20),
    ],
    prob_in_game="4",
    prob_map_gen="7",
    map_colour="189",
    location_checks=dict(same_type_distance=18),
    prospect_chance="0.75",
    name="TTD_STR_INDUSTRY_NAME_WATER_SUPPLY",
    nearby_station_name="string(STR_STATION_HEAVY_INDUSTRY_2)",
    # deliberately low fund cost; there is some remaining weirdness on cost because this is a non-growable primary, but eh, live with it
    fund_cost_multiplier="45",
)

industry.enable_in_economy(
    "GALIZA",
    locate_in_specific_biomes=[
        "galiza",
        "asturias",
        "portugal",
    ],
)

industry.add_tile(
    id="water_plant_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="dirty_concrete",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")

spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 106, -31, -73)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 64, -31, -32)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 84, -31, -52)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 64, -31, -32)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 10, 64, 64, -31, -32)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 10, 64, 64, -31, -32)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 10, 64, 64, -31, -32)],
)

industry.add_spritelayout(
    id="water_plant_spritelayout_separation_tower",
    tile="water_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="water_plant_spritelayout_large_shed",
    tile="water_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=6,
)
industry.add_spritelayout(
    id="water_plant_spritelayout_purification_unit",
    tile="water_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="water_plant_spritelayout_horizontal_tanks",
    tile="water_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="water_plant_spritelayout_storage_tank_blue",
    tile="water_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="water_plant_spritelayout_storage_tank_yellow",
    tile="water_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="water_plant_spritelayout_empty",
    tile="water_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
)

industry.add_industry_layout(
    id="water_plant_industry_layout_1",
    layout=[
        (0, 0, "water_plant_spritelayout_large_shed"),
        (0, 1, "water_plant_spritelayout_horizontal_tanks"),
        (1, 0, "water_plant_spritelayout_purification_unit"),
        (1, 1, "water_plant_spritelayout_separation_tower"),
        (2, 0, "water_plant_spritelayout_horizontal_tanks"),
        (2, 1, "water_plant_spritelayout_empty"),
        (3, 0, "water_plant_spritelayout_storage_tank_blue"),
        (3, 1, "water_plant_spritelayout_storage_tank_yellow"),
    ],
)
industry.add_industry_layout(
    id="water_plant_industry_layout_2",
    layout=[
        (0, 0, "water_plant_spritelayout_storage_tank_blue"),
        (0, 1, "water_plant_spritelayout_storage_tank_yellow"),
        (1, 0, "water_plant_spritelayout_large_shed"),
        (1, 1, "water_plant_spritelayout_empty"),
        (2, 0, "water_plant_spritelayout_purification_unit"),
        (2, 1, "water_plant_spritelayout_separation_tower"),
        (3, 0, "water_plant_spritelayout_horizontal_tanks"),
        (3, 1, "water_plant_spritelayout_horizontal_tanks"),
    ],
)
industry.add_industry_layout(
    id="water_plant_industry_layout_3",
    layout=[
        (0, 0, "water_plant_spritelayout_large_shed"),
        (0, 1, "water_plant_spritelayout_horizontal_tanks"),
        (0, 2, "water_plant_spritelayout_horizontal_tanks"),
        (0, 3, "water_plant_spritelayout_storage_tank_yellow"),
        (1, 0, "water_plant_spritelayout_purification_unit"),
        (1, 1, "water_plant_spritelayout_separation_tower"),
        (1, 2, "water_plant_spritelayout_empty"),
        (1, 3, "water_plant_spritelayout_storage_tank_blue"),
    ],
)
industry.add_industry_layout(
    id="water_plant_industry_layout_4",
    layout=[
        (0, 0, "water_plant_spritelayout_storage_tank_yellow"),
        (0, 1, "water_plant_spritelayout_large_shed"),
        (0, 2, "water_plant_spritelayout_purification_unit"),
        (0, 3, "water_plant_spritelayout_separation_tower"),
        (1, 0, "water_plant_spritelayout_storage_tank_blue"),
        (1, 1, "water_plant_spritelayout_empty"),
        (1, 2, "water_plant_spritelayout_horizontal_tanks"),
        (1, 3, "water_plant_spritelayout_horizontal_tanks"),
    ],
)
industry.add_industry_layout(
    id="water_plant_industry_layout_5",
    layout=[
        (0, 0, "water_plant_spritelayout_large_shed"),
        (0, 1, "water_plant_spritelayout_empty"),
        (0, 2, "water_plant_spritelayout_storage_tank_yellow"),
        (1, 0, "water_plant_spritelayout_purification_unit"),
        (1, 1, "water_plant_spritelayout_separation_tower"),
        (1, 2, "water_plant_spritelayout_storage_tank_blue"),
        (2, 0, "water_plant_spritelayout_horizontal_tanks"),
        (2, 1, "water_plant_spritelayout_horizontal_tanks"),
    ],
)
