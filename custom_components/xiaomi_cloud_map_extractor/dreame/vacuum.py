from custom_components.xiaomi_cloud_map_extractor.common.map_data import MapData
from custom_components.xiaomi_cloud_map_extractor.common.vacuum_v2 import XiaomiCloudVacuumV2
from custom_components.xiaomi_cloud_map_extractor.dreame.map_data_parser import MapDataParserDreame
from custom_components.xiaomi_cloud_map_extractor.types import Colors, Drawables, ImageConfig, Sizes, Texts


class DreameVacuum(XiaomiCloudVacuumV2):

    def __init__(self, connector, country, user_id, device_id, model):
        super().__init__(connector, country, user_id, device_id, model)

    def get_map_archive_extension(self) -> str:
        return "b64"

    def decode_map(self,
                   raw_map: bytes,
                   colors: Colors,
                   drawables: Drawables,
                   texts: Texts,
                   sizes: Sizes,
                   image_config: ImageConfig) -> MapData:
        # with open('/config/map_data_dreame.vacuum.p2029.b64', 'rb') as f:
        #     raw_map_file = f.read()
        #     raw_map_string = raw_map_file.decode()
        #     return MapDataParserDreame.decode_map(raw_map_string, colors, drawables, texts, sizes, image_config)
        raw_map_string = raw_map.decode()
        return MapDataParserDreame.decode_map(raw_map_string, colors, drawables, texts, sizes, image_config)
