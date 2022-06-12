BANNERS = {
    0 : {
        "id": "black_banner",
        "tag": "display:{Name:'{\"text\":\"0000\"}'}"
    },

    1 : {
        "id": "black_banner",
        "tag": "display:{Name:'{\"text\":\"0001\"}'},BlockEntityTag:{Patterns:[{Pattern:bo,Color:4},{Pattern:ld,Color:15},{Pattern:lud,Color:15}]}"
    },

    2 : {
        "id": "yellow_banner",
        "tag": "display:{Name:'{\"text\":\"0010\"}'},BlockEntityTag:{Patterns:[{Pattern:ss,Color:15},{Pattern:vh,Color:15},{Pattern:cs,Color:15},{Pattern:bo,Color:15}]}"
    },

    3 : {
        "id": "black_banner",
        "tag": "display:{Name:'{\"text\":\"0011\"}'},BlockEntityTag:{Patterns:[{Pattern:ss,Color:4},{Pattern:vh,Color:15}]}"
    },

    4 : {
        "id": "yellow_banner",
        "tag": "display:{Name:'{\"text\":\"0100\"}'},BlockEntityTag:{Patterns:[{Pattern:ss,Color:15},{Pattern:vhr,Color:15},{Pattern:cs,Color:15},{Pattern:bo,Color:15}]}"
    },

    5 : {
        "id": "black_banner",
        "tag": "display:{Name:'{\"text\":\"0101\"}'},BlockEntityTag:{Patterns:[{Pattern:bo,Color:4},{Pattern:cs,Color:4},{Pattern:ls,Color:15},{Pattern:bts,Color:15},{Pattern:tts,Color:15}]}"
    },

    6 : {
        "id": "black_banner",
        "tag": "display:{Name:'{\"text\":\"0110\"}'},BlockEntityTag:{Patterns:[{Pattern:ss,Color:4},{Pattern:ls,Color:15},{Pattern:rs,Color:15}]}"
    },

    7 : {
        "id": "black_banner",
        "tag": "display:{Name:'{\"text\":\"0111\"}'},BlockEntityTag:{Patterns:[{Pattern:ss,Color:4},{Pattern:ls,Color:15}]}"
    },

    8 : {
        "id": "black_banner",
        "tag": "display:{Name:'{\"text\":\"1000\"}'},BlockEntityTag:{Patterns:[{Pattern:bo,Color:4},{Pattern:rd,Color:15},{Pattern:rud,Color:15}]}"
    },

    9 : {
        "id": "black_banner",
        "tag": "display:{Name:'{\"text\":\"1001\"}'},BlockEntityTag:{Patterns:[{Pattern:bo,Color:4},{Pattern:tt,Color:15},{Pattern:bt,Color:15}]}"
    },

    10 : {
        "id": "black_banner",
        "tag": "display:{Name:'{\"text\":\"1010\"}'},BlockEntityTag:{Patterns:[{Pattern:bo,Color:4},{Pattern:rs,Color:15},{Pattern:cs,Color:4},{Pattern:bts,Color:15},{Pattern:tts,Color:15}]}"
    },

    11 : {
        "id": "black_banner",
        "tag": "display:{Name:'{\"text\":\"1011\"}'},BlockEntityTag:{Patterns:[{Pattern:ss,Color:4},{Pattern:vh,Color:15},{Pattern:bo,Color:4},{Pattern:bts,Color:15},{Pattern:tts,Color:15}]}"
    },

    12 : {
        "id": "black_banner",
        "tag": "display:{Name:'{\"text\":\"1100\"}'},BlockEntityTag:{Patterns:[{Pattern:ss,Color:4},{Pattern:vhr,Color:15}]}"
    },

    13 : {
        "id": "black_banner",
        "tag": "display:{Name:'{\"text\":\"1101\"}'},BlockEntityTag:{Patterns:[{Pattern:ss,Color:4},{Pattern:vhr,Color:15},{Pattern:bo,Color:4},{Pattern:bts,Color:15},{Pattern:tts,Color:15}]}"
    },

    14 : {
        "id": "black_banner",
        "tag": "display:{Name:'{\"text\":\"1110\"}'},BlockEntityTag:{Patterns:[{Pattern:ss,Color:4},{Pattern:rs,Color:15}]}"
    },

    15 : {
        "id": "black_banner",
        "tag": "display:{Name:'{\"text\":\"1111\"}'},BlockEntityTag:{Patterns:[{Pattern:ss,Color:4}]}"
    },

}

# format variable: text, items
CHEST = "chest{{display:{{Name:\'{{\"text\":\"{text}\"}}\'}},BlockEntityTag:{{Items:[{items}]}}}}"

# format variable: slot, id, count, tag
CHEST_ITEM = "{{Slot:{slot}b,id:\"{id}\",Count:{count}b,tag:{{{tag}}}}}"

# format variable: text, items
SHULKER_BOX = "display:{{Name:\'{{\"text\":\"{text}\"}}\'}},BlockEntityTag:{{Items:[{items}]}}"


# demo for using template strings
if __name__ == "__main__":
    eg = CHEST.format(
        text="hi", 
        items=",".join([
            CHEST_ITEM.format(
                slot=1,
                id="shulker_box",
                count=1,
                tag=SHULKER_BOX.format(
                    text="hello",
                    items=",".join([
                        CHEST_ITEM.format(
                            slot=1,
                            id=BANNERS[5]["id"],
                            count=1,
                            tag=BANNERS[5]["tag"]
                            )
                        ])
                    )
                )
            ])
        )

    print(f"give @p {eg}")