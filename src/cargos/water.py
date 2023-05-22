from cargo import Cargo

cargo = Cargo(
    id="water",
    type_name="TTD_STR_CARGO_PLURAL_WATER",
    unit_name="TTD_STR_CARGO_SINGULAR_WATER",
    type_abbreviation="TTD_STR_ABBREV_WATER",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_EXPRESS, CC_LIQUID, CC_REFRIGERATED)",
    cargo_label="WATR",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_LITERS",
    items_of_cargo="TTD_STR_QUANTITY_WATER",
    penalty_lowerbound="0",
    single_penalty_length="16",
    capacity_multiplier="1",
    price_factor=70,
    icon_indices=(1, 5),
)
