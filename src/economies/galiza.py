from economy import Economy

economy = Economy(
    id="GALIZA",
    numeric_id=7,
    # as of May 2015 the following cargos must have fixed positions if used by an economy:
    # passengers: 0, mail: 2, goods 5, food 11
    # keep the rest of the cargos alphabetised
    # bump the min. compatible version if this list changes
    cargos=[
        "passengers",  # 0 fixed position
        "alcohol",
        "mail",  # 2 fixed position
        "beans",
        "chemicals",
        "goods",  # 5 fixed position
        "logs",
        "grain",
        "livestock",
        "engineering_supplies",
        "farm_supplies",
        "food",  # 11 fixed position
        "fish",
        "timber",
        "wool",
        "milk",
        "fruits",
        "coal",
        "plant_fibres",
        "peat",
        "petrol",  # 20
        "recyclables",
        "scrap_metal",
        "glass",
        "sand",
        "electrical_parts",  # 25
        "vehicle_bodies",
        "vehicle_engines",
        "vehicle_parts",
        "tyres",
        "vehicles",  # 30
        "rubber",
        "steel",
        "iron_ore",
        "copper_ore",
        "copper",  # 35
        "building_materials",
        "pyrite_ore",
        "zinc",
        "stone",
        "clay",  # 40
        "water",
        "hydrogen",
        "waste",
    ],
    # as of April 2021 this cargoflow graph is really as optimised as can be
    # the main driver is preventing ugly appearance of the edges that converge on food, most of the layout is arranged around preventing that
    cargoflow_graph_tuning={
        # "group_edges_subgraphs": [],
        # "ranking_subgraphs": [],
        # "clusters": []
        "group_edges_subgraphs": [
            # ["textile_mill", "dairy_farm"],
        ],
        "ranking_subgraphs": [
            ("source", ["pyrite_mine", "copper_mine"]),
            ("same", ["integrated_steel_mill", "pyrite_smelter",
             "copper_smelter", "recycling_depot"]),
            ("same", ["textile_mill", "furniture_factory"]),
            ("same", ["paper_mill", "sawmill", "power_plant", "biorefinery"]),
            ("same", ["forest", "glass_works"]),



            ("same", ["rubber", "vehicles", "goods"]),
            ("same", ["supply_yard", "assembly_plant"]),
            (
                "sink",
                [
                    "T_town_industries",
                    "T_towns_food",
                    "T_towns_vehicles",
                    "T_towns_alcohol",
                ],
            ),
        ],
        "clusters": [
            {"nodes": ["body_plant", "engine_plant", "tyre_plant",
                       "component_factory"], "rank": "same"},
            {"nodes": ["grain", "fruits", "beans"],
                "rank": "same", "color": "white"},
            {"nodes": ["copper_ore", "pyrite_ore", "iron_ore",
                       "scrap_metal"], "rank": "same", "color": "white"},
        ],
    },
)

# some deliberate overlapping of biomes for mixing at boundaries
economy.add_biome(
    "galiza",
    min_x_percent=0,
    max_x_percent=55,
    min_y_percent=0,
    max_y_percent=75,
)
economy.add_biome(
    "asturias",
    min_x_percent=55,
    max_x_percent=100,
    min_y_percent=0,
    max_y_percent=40,
)
economy.add_biome(
    "castela",
    min_x_percent=60,
    max_x_percent=100,
    min_y_percent=40,
    max_y_percent=100,
)
economy.add_biome(
    "portugal",
    min_x_percent=0,
    max_x_percent=60,
    min_y_percent=75,
    max_y_percent=100,
)
