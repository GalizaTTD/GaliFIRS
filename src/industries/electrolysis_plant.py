from industry import IndustrySecondary, TileLocationChecks

# this industry overlaps with chemical plant somewhat, but blah blah blah

industry = IndustrySecondary(
    id="electrolysis_plant",
    accept_cargos_with_input_ratios=[
        ("WATR", 8),
    ],
    prod_cargo_types_with_output_ratios=[
        ("H2__", 6),
    ],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="173",
    name="string(STR_IND_ELECTROLYSIS_PLANT)",
    nearby_station_name="string(STR_STATION_ELECTROLYSIS_PLANT)",
    fund_cost_multiplier="170",
    intro_year=2020,
    provides_snow=True,
)

industry.enable_in_economy(
    "GALIZA",
)

industry.add_tile(
    id="electrolysis_plant_tile_1",
    animation_length=7,
    animation_looping=True,
    animation_speed=3,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="dirty_concrete",
)
spriteset_ground_overlay = industry.add_spriteset(
    type="empty",
)

spriteset_1 = industry.add_spriteset(
    sprites=[(80, 10, 64, 114, -31, -88)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(150, 10, 64, 114, -31, -83)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(220, 10, 64, 114, -31, -83)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(290, 10, 64, 114, -31, -83)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(360, 10, 64, 66, -31, -35)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(430, 10, 64, 66, -31, -35)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(500, 10, 64, 66, -31, -35)],
)
spriteset_8 = industry.add_spriteset(
    sprites=[(570, 10, 64, 66, -31, -35)],
)
spriteset_9 = industry.add_spriteset(
    sprites=[(640, 10, 64, 66, -31, -35)],
)
spriteset_10 = industry.add_spriteset(
    sprites=[(710, 10, 64, 66, -31, -35)],
)
sprite_smoke_1 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=5,
    yoffset=0,
    zoffset=69,
    animation_frame_offset=1,
)
sprite_smoke_2 = industry.add_smoke_sprite(
    smoke_type="white_smoke_big",
    xoffset=9,
    yoffset=0,
    zoffset=69,
)

industry.add_spritelayout(
    id="electrolysis_plant_spritelayout_1",
    tile="electrolysis_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    smoke_sprites=[sprite_smoke_1, sprite_smoke_2],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=1,
)
industry.add_spritelayout(
    id="electrolysis_plant_spritelayout_2",
    tile="electrolysis_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=2,
)
industry.add_spritelayout(
    id="electrolysis_plant_spritelayout_3",
    tile="electrolysis_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=3,
)
industry.add_spritelayout(
    id="electrolysis_plant_spritelayout_4",
    tile="electrolysis_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=4,
)
industry.add_spritelayout(
    id="electrolysis_plant_spritelayout_5",
    tile="electrolysis_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
    fences=["nw", "ne"],
    add_to_object_num=5,
)
industry.add_spritelayout(
    id="electrolysis_plant_spritelayout_6",
    tile="electrolysis_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
    fences=["nw", "ne"],
    add_to_object_num=6,
)
industry.add_spritelayout(
    id="electrolysis_plant_spritelayout_7",
    tile="electrolysis_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=7,
)
industry.add_spritelayout(
    id="electrolysis_plant_spritelayout_8",
    tile="electrolysis_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_8],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=8,
)
industry.add_spritelayout(
    id="electrolysis_plant_spritelayout_9",
    tile="electrolysis_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_9],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=9,
)
industry.add_spritelayout(
    id="electrolysis_plant_spritelayout_10",
    tile="electrolysis_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_10],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=10,
)
industry.add_spritelayout(
    id="electrolysis_plant_spritelayout_concrete",
    tile="electrolysis_plant_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[],
    fences=["nw", "ne", "se", "sw"],
    add_to_object_num=11,
)

industry.add_industry_layout(
    id="electrolysis_plant_industry_layout_1",
    layout=[
        (0, 0, "electrolysis_plant_spritelayout_1"),
        (0, 1, "electrolysis_plant_spritelayout_4"),
        (0, 2, "electrolysis_plant_spritelayout_8"),
        (1, 0, "electrolysis_plant_spritelayout_6"),
        (1, 1, "electrolysis_plant_spritelayout_3"),
        (1, 2, "electrolysis_plant_spritelayout_9"),
        (2, 0, "electrolysis_plant_spritelayout_5"),
        (2, 1, "electrolysis_plant_spritelayout_2"),
        (2, 2, "electrolysis_plant_spritelayout_7"),
        (3, 0, "electrolysis_plant_spritelayout_10"),
        (3, 1, "electrolysis_plant_spritelayout_concrete"),
        (3, 2, "electrolysis_plant_spritelayout_7"),
    ],
)
industry.add_industry_layout(
    id="electrolysis_plant_industry_layout_2",
    layout=[
        (0, 0, "electrolysis_plant_spritelayout_1"),
        (0, 1, "electrolysis_plant_spritelayout_6"),
        (1, 0, "electrolysis_plant_spritelayout_4"),
        (1, 1, "electrolysis_plant_spritelayout_5"),
        (2, 0, "electrolysis_plant_spritelayout_3"),
        (2, 1, "electrolysis_plant_spritelayout_10"),
        (3, 0, "electrolysis_plant_spritelayout_2"),
        (3, 1, "electrolysis_plant_spritelayout_7"),
        (4, 0, "electrolysis_plant_spritelayout_8"),
        (4, 1, "electrolysis_plant_spritelayout_9"),
    ],
)
industry.add_industry_layout(
    id="electrolysis_plant_industry_layout_3",
    layout=[
        (0, 1, "electrolysis_plant_spritelayout_4"),
        (1, 0, "electrolysis_plant_spritelayout_8"),
        (1, 1, "electrolysis_plant_spritelayout_3"),
        (1, 2, "electrolysis_plant_spritelayout_7"),
        (1, 3, "electrolysis_plant_spritelayout_6"),
        (2, 0, "electrolysis_plant_spritelayout_9"),
        (2, 1, "electrolysis_plant_spritelayout_2"),
        (2, 2, "electrolysis_plant_spritelayout_1"),
        (2, 3, "electrolysis_plant_spritelayout_5"),
    ],
)
industry.add_industry_layout(
    id="electrolysis_plant_industry_layout_4",
    layout=[
        (0, 1, "electrolysis_plant_spritelayout_4"),
        (1, 0, "electrolysis_plant_spritelayout_1"),
        (1, 1, "electrolysis_plant_spritelayout_3"),
        (1, 2, "electrolysis_plant_spritelayout_6"),
        (1, 3, "electrolysis_plant_spritelayout_8"),
        (2, 0, "electrolysis_plant_spritelayout_7"),
        (2, 1, "electrolysis_plant_spritelayout_2"),
        (2, 2, "electrolysis_plant_spritelayout_5"),
        (2, 3, "electrolysis_plant_spritelayout_9"),
    ],
)
industry.add_industry_layout(
    id="electrolysis_plant_industry_layout_5",
    layout=[
        (0, 0, "electrolysis_plant_spritelayout_4"),
        (0, 1, "electrolysis_plant_spritelayout_7"),
        (1, 0, "electrolysis_plant_spritelayout_3"),
        (1, 1, "electrolysis_plant_spritelayout_7"),
        (2, 0, "electrolysis_plant_spritelayout_2"),
        (2, 1, "electrolysis_plant_spritelayout_6"),
        (3, 0, "electrolysis_plant_spritelayout_1"),
        (3, 1, "electrolysis_plant_spritelayout_5"),
        (4, 0, "electrolysis_plant_spritelayout_8"),
        (4, 1, "electrolysis_plant_spritelayout_6"),
        (5, 0, "electrolysis_plant_spritelayout_8"),
        (5, 1, "electrolysis_plant_spritelayout_5"),
        (6, 0, "electrolysis_plant_spritelayout_9"),
        (6, 1, "electrolysis_plant_spritelayout_10"),
    ],
)
industry.add_industry_layout(
    id="electrolysis_plant_industry_layout_6",
    layout=[
        (0, 0, "electrolysis_plant_spritelayout_4"),
        (0, 1, "electrolysis_plant_spritelayout_8"),
        (0, 2, "electrolysis_plant_spritelayout_8"),
        (1, 0, "electrolysis_plant_spritelayout_3"),
        (1, 1, "electrolysis_plant_spritelayout_6"),
        (1, 2, "electrolysis_plant_spritelayout_6"),
        (2, 0, "electrolysis_plant_spritelayout_2"),
        (2, 1, "electrolysis_plant_spritelayout_5"),
        (2, 2, "electrolysis_plant_spritelayout_5"),
        (3, 0, "electrolysis_plant_spritelayout_1"),
        (3, 1, "electrolysis_plant_spritelayout_10"),
        (3, 2, "electrolysis_plant_spritelayout_concrete"),
        (4, 0, "electrolysis_plant_spritelayout_7"),
        (4, 1, "electrolysis_plant_spritelayout_7"),
        (4, 2, "electrolysis_plant_spritelayout_9"),
    ],
)
industry.add_industry_layout(
    id="electrolysis_plant_industry_layout_7",
    layout=[
        (0, 0, "electrolysis_plant_spritelayout_4"),
        (0, 1, "electrolysis_plant_spritelayout_1"),
        (0, 2, "electrolysis_plant_spritelayout_8"),
        (0, 3, "electrolysis_plant_spritelayout_10"),
        (1, 0, "electrolysis_plant_spritelayout_3"),
        (1, 1, "electrolysis_plant_spritelayout_6"),
        (1, 2, "electrolysis_plant_spritelayout_8"),
        (1, 3, "electrolysis_plant_spritelayout_6"),
        (2, 0, "electrolysis_plant_spritelayout_2"),
        (2, 1, "electrolysis_plant_spritelayout_5"),
        (2, 2, "electrolysis_plant_spritelayout_9"),
        (2, 3, "electrolysis_plant_spritelayout_5"),
        (3, 0, "electrolysis_plant_spritelayout_7"),
        (3, 1, "electrolysis_plant_spritelayout_7"),
        (3, 2, "electrolysis_plant_spritelayout_9"),
        (3, 3, "electrolysis_plant_spritelayout_10"),
    ],
)
