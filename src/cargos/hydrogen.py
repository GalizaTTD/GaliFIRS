from cargo import Cargo

cargo = Cargo(
    id="hydrogen",
    type_name="string(STR_CARGO_NAME_HYDROGEN)",
    unit_name="string(STR_CARGO_NAME_HYDROGEN)",
    type_abbreviation="string(STR_CID_HYDROGEN)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_LIQUID)",
    cargo_label="H2__",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="string(STR_CARGO_UNIT_HYDROGEN)",
    penalty_lowerbound="22",
    single_penalty_length="44",
    price_factor=136,
    capacity_multiplier="1",
    icon_indices=(11, 5),
)
