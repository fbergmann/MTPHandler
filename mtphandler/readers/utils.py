from mtphandler.model import Well

# regex patterns
WELL_ID_PATTERN = r"[A-H][0-9]{1,2}"


def xy_to_id(x: int, y: int) -> str:
    """Well coordinates to well ID"""
    return f"{chr(y + 65)}{x+1}"


def id_to_xy(well_id: str) -> tuple[int, int]:
    """Well ID to well coordinates"""
    return int(well_id[1:]) - 1, ord(well_id[0].upper()) - 65

    def get_well(self, id: str) -> Well:
        for well in self.plate.wells:
            if well.id.lower() == id.lower():
                return well

        raise ValueError(f"Well {id} not found")


if __name__ == "__main__":
    print(xy_to_id(0, 0))
    print(id_to_xy("A1"))
    print(id_to_xy("H12"))
    print(id_to_xy("C3"))
