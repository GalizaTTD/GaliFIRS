from cargo import Cargo

cargo = Cargo(
    id="waste",
    type_name="string(STR_CARGO_NAME_WASTE)",
    unit_name="string(STR_CARGO_NAME_WASTE)",
    type_abbreviation="string(STR_CID_WASTE)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_BULK, CC_PIECE_GOODS, CC_COVERED)",
    cargo_label="WSTE",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_WASTE)",
    penalty_lowerbound="10",
    single_penalty_length="128",
    capacity_multiplier="1",
    price_factor=20,
    icon_indices=(10, 5),
)
